from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# ============================================================
# USUARIOS
# ============================================================

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    rol: Optional[str] = "Estudiante"
    estado: Optional[str] = "Activo"

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    correo: Optional[EmailStr]
    rol: Optional[str]
    estado: Optional[str]

class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    correo: EmailStr
    rol: str
    estado: str

    class Config:
        from_attributes = True


# ============================================================
# EVENTOS
# ============================================================

class EventoCreate(BaseModel):
    nombre: str
    id_tipo: int
    fecha_inicio: date
    fecha_fin: date
    id_usuario: int
    id_unidad_academica: int

class EventoUpdate(BaseModel):
    nombre: Optional[str] = None
    id_tipo: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    id_usuario: Optional[int] = None
    id_unidad_academica: Optional[int] = None

class EventoOut(BaseModel):
    id_evento: int
    nombre: str
    id_tipo: int
    fecha_inicio: date
    fecha_fin: date
    id_usuario: int
    id_unidad_academica: int

    class Config:
        from_attributes = True


# ============================================================
# RESERVAS
# ============================================================

class ReservaBase(BaseModel):
    id_usuario: int
    id_evento: int

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id_reserva: int

    class Config:
        from_attributes = True


# ============================================================
# EVALUACIONES
# ============================================================

class EvaluacionBase(BaseModel):
    id_evento: int
    estado: str              # Aprobado, Pendiente, Rechazado
    justificacion: Optional[str] = None

class EvaluacionCreate(EvaluacionBase):
    pass  # ya no tiene usuario_id

class EvaluacionUpdate(BaseModel):
    id_evento: Optional[int] = None
    estado: Optional[str] = None
    justificacion: Optional[str] = None

class EvaluacionOut(EvaluacionBase):
    id_evaluacion: int

    class Config:
        from_attributes = True
