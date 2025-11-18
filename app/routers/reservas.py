from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.reservas import Reserva
from app.schemas import ReservaCreate, ReservaResponse

router = APIRouter(prefix="/reservas", tags=["Reservas"])


# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# LISTAR TODAS LAS RESERVAS
@router.get("/", response_model=list[ReservaResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Reserva).all()


# OBTENER UNA RESERVA POR ID
@router.get("/{id_reserva}", response_model=ReservaResponse)
def obtener(id_reserva: int, db: Session = Depends(get_db)):
    return db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()


# CREAR RESERVA
@router.post("/", response_model=ReservaResponse)
def crear(data: ReservaCreate, db: Session = Depends(get_db)):
    nuevo = Reserva(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ACTUALIZAR RESERVA
@router.put("/{id_reserva}")
def actualizar(id_reserva: int, data: ReservaCreate, db: Session = Depends(get_db)):
    db.query(Reserva).filter(Reserva.id_reserva == id_reserva).update(data.dict())
    db.commit()
    return {"mensaje": "Reserva actualizada"}


# ELIMINAR RESERVA
@router.delete("/{id_reserva}")
def eliminar(id_reserva: int, db: Session = Depends(get_db)):
    db.query(Reserva).filter(Reserva.id_reserva == id_reserva).delete()
    db.commit()
    return {"mensaje": "Reserva eliminada"}
