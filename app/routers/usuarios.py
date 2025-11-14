# app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas  # Se importa schemas
from app.database import get_db
from typing import List

# Se elimina el prefijo de aquí
router = APIRouter(tags=["Usuarios"])

# --- Se eliminan las definiciones de UsuarioBase y UsuarioRespuesta ---
# Ya están en app/schemas.py

@router.get("/", response_model=List[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@router.post("/", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Se usa el esquema de Pydantic v2 para crear el modelo
    nuevo = models.Usuario(**usuario.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{id_usuario}", response_model=schemas.UsuarioResponse)
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}