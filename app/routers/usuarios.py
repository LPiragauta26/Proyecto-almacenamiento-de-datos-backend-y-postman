from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuarios import Usuario
from app import schemas

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Listar usuarios
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

# Obtener por ID
@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear usuario
@router.post("/")
def crear(data: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo = Usuario(
        nombre=data.nombre,
        apellido=data.apellido,
        correo=data.correo,
        rol=data.rol,
        estado=data.estado
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Actualizar usuario
@router.put("/{id}")
def actualizar(id: int, data: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar solo los campos que llegan
    if data.nombre is not None:
        usuario.nombre = data.nombre
    if data.apellido is not None:
        usuario.apellido = data.apellido
    if data.correo is not None:
        usuario.correo = data.correo
    if data.rol is not None:
        usuario.rol = data.rol
    if data.estado is not None:
        usuario.estado = data.estado

    db.commit()
    db.refresh(usuario)
    return usuario

# Eliminar usuario
@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}
