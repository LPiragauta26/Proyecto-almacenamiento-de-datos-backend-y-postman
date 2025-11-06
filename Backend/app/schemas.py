# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    codigo: str
    nombre: str
    apellido: str
    email: str
    telefono: Optional[str] = None
    rol: str
    estado: Optional[str] = "Activo"

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_registro: datetime

    class Config:
        orm_mode = True


class EventoBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    tipo: str
    fecha_inicio: datetime
    fecha_fin: datetime
    id_lugar: Optional[int] = None
    estado: Optional[str] = "Registrado"

class EventoCreate(EventoBase):
    pass

class EventoResponse(EventoBase):
    id_evento: int

    class Config:
        orm_mode = True
