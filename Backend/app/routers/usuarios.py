# app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models
from app.database import get_db
from pydantic import BaseModel
from typing import List

# --- Configuración del router ---
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# --- Esquemas Pydantic ---
class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    rol: str = "Estudiante"
    estado: str = "Activo"

class UsuarioRespuesta(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True  # Para compatibilidad con Pydantic v2

# --- ENDPOINTS ---

# Obtener todos los usuarios
@router.get("/", response_model=List[UsuarioRespuesta])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

# Crear un usuario nuevo
@router.post("/", response_model=UsuarioRespuesta)
def crear_usuario(usuario: UsuarioBase, db: Session = Depends(get_db)):
    # Verificar si el correo ya existe
    correo_existente = db.query(models.Usuario).filter(models.Usuario.correo == usuario.correo).first()
    if correo_existente:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    
    nuevo = models.Usuario(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        correo=usuario.correo,
        rol=usuario.rol,
        estado=usuario.estado
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener un usuario por su ID
@router.get("/{id_usuario}", response_model=UsuarioRespuesta)
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Actualizar un usuario existente
@router.put("/{id_usuario}", response_model=dict)
def actualizar_usuario(id_usuario: int, usuario_actualizado: UsuarioBase, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar si el correo ya está en uso por otro usuario
    correo_existente = db.query(models.Usuario).filter(
        models.Usuario.correo == usuario_actualizado.correo,
        models.Usuario.id_usuario != id_usuario
    ).first()
    if correo_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado por otro usuario")

    usuario.nombre = usuario_actualizado.nombre
    usuario.apellido = usuario_actualizado.apellido
    usuario.correo = usuario_actualizado.correo
    usuario.rol = usuario_actualizado.rol
    usuario.estado = usuario_actualizado.estado
    db.commit()
    db.refresh(usuario)
    return {"mensaje": "Usuario actualizado correctamente"}

# Eliminar un usuario
@router.delete("/{id_usuario}", response_model=dict)
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        db.delete(usuario)
        db.commit()
    except IntegrityError:
        db.rollback()  # Revertir la transacción
        raise HTTPException(
            status_code=400,
            detail="No se puede eliminar el usuario porque tiene eventos asociados"
        )

    return {"mensaje": f"Usuario con ID {id_usuario} eliminado correctamente"}
