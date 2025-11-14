# app/routers/eventos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.get("/", response_model=list[schemas.EventoResponse])
def listar_eventos(db: Session = Depends(database.get_db)):
    return db.query(models.Evento).all()

@router.post("/", response_model=schemas.EventoResponse)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(database.get_db)):
    # Se usa .model_dump() en lugar de .dict()
    nuevo = models.Evento(**evento.model_dump()) 
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{id_evento}", response_model=schemas.EventoResponse)
def obtener_evento(id_evento: int, db: Session = Depends(database.get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento

@router.put("/{id_evento}", response_model=schemas.EventoResponse)
def actualizar_evento(id_evento: int, datos: schemas.EventoCreate, db: Session = Depends(database.get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    # Se usa .model_dump() en lugar de .dict()
    for campo, valor in datos.model_dump().items():
        setattr(evento, campo, valor)
    db.commit()
    db.refresh(evento)
    return evento

@router.delete("/{id_evento}")
def eliminar_evento(id_evento: int, db: Session = Depends(database.get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id_evento == id_evento).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    db.delete(evento)
    db.commit()
    return {"mensaje": "Evento eliminado correctamente"}