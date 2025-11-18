from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.evaluaciones import Evaluacion
from app.schemas import EvaluacionCreate, EvaluacionUpdate, EvaluacionOut

router = APIRouter(prefix="/evaluaciones", tags=["Evaluaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Listar todas las evaluaciones
@router.get("/", response_model=list[EvaluacionOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Evaluacion).all()

# Obtener una evaluación por ID
@router.get("/{id}", response_model=EvaluacionOut)
def obtener(id: int, db: Session = Depends(get_db)):
    evaluacion = db.query(Evaluacion).filter(Evaluacion.id_evaluacion == id).first()
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")
    return evaluacion

# Crear evaluación
@router.post("/", response_model=EvaluacionOut)
def crear(data: EvaluacionCreate, db: Session = Depends(get_db)):
    nueva = Evaluacion(
        id_evento=data.id_evento,
        estado=data.estado,
        justificacion=data.justificacion
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# Actualizar evaluación
@router.put("/{id}", response_model=EvaluacionOut)
def actualizar(id: int, data: EvaluacionUpdate, db: Session = Depends(get_db)):
    evaluacion = db.query(Evaluacion).filter(Evaluacion.id_evaluacion == id).first()
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")

    if data.id_evento is not None:
        evaluacion.id_evento = data.id_evento
    if data.estado is not None:
        evaluacion.estado = data.estado
    if data.justificacion is not None:
        evaluacion.justificacion = data.justificacion

    db.commit()
    db.refresh(evaluacion)
    return evaluacion

# Eliminar evaluación
@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    evaluacion = db.query(Evaluacion).filter(Evaluacion.id_evaluacion == id).first()
    if not evaluacion:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")

    db.delete(evaluacion)
    db.commit()
    return {"mensaje": "Evaluación eliminada correctamente"}
