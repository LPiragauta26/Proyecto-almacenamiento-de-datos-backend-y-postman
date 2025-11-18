from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.eventos import Evento  # asegurarse que el nombre del archivo sea singular
from app import schemas

router = APIRouter(prefix="/eventos", tags=["Eventos"])

# Dependencia de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# LISTAR TODOS LOS EVENTOS
# =========================
@router.get("/", response_model=list[schemas.EventoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Evento).all()

# =========================
# OBTENER EVENTO POR ID
# =========================
@router.get("/{id_evento}", response_model=schemas.EventoOut)
def obtener(id_evento: int, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento

# =========================
# CREAR EVENTO
# =========================
@router.post("/", response_model=schemas.EventoOut)
def crear(data: schemas.EventoCreate, db: Session = Depends(get_db)):
    nuevo = Evento(
        nombre=data.nombre,
        id_tipo=data.id_tipo,
        fecha_inicio=data.fecha_inicio,
        fecha_fin=data.fecha_fin,
        id_usuario=data.id_usuario,
        id_unidad_academica=data.id_unidad_academica
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# =========================
# ACTUALIZAR EVENTO
# =========================
@router.put("/{id_evento}", response_model=schemas.EventoOut)
def actualizar(id_evento: int, data: schemas.EventoUpdate, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    # Actualizamos solo los campos que vienen en la request
    for field, value in data.dict(exclude_unset=True).items():
        setattr(evento, field, value)

    db.commit()
    db.refresh(evento)
    return evento

# =========================
# ELIMINAR EVENTO
# =========================
@router.delete("/{id_evento}")
def eliminar(id_evento: int, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    db.delete(evento)
    db.commit()
    return {"mensaje": "Evento eliminado correctamente"}
