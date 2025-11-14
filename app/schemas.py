from pydantic import BaseModel
from typing import Optional
from datetime import date

# -------------------------------
#           USUARIOS
# -------------------------------
class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    rol: Optional[str] = "Estudiante"
    estado: Optional[str] = "Activo"

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True


# -------------------------------
#            EVENTOS
# -------------------------------
class EventoBase(BaseModel):
    nombre: str
    tipo: str
    fecha_inicio: date
    fecha_fin: date
    id_usuario: int
    id_unidad_academica: int

class EventoCreate(EventoBase):
    pass

class EventoResponse(EventoBase):
    id_evento: int

    class Config:
        from_attributes = True