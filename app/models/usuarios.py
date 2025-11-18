from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import BIGINT
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    apellido = Column(String(60), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    rol = Column(Enum('Docente','Estudiante','Secretario','Administrador'), nullable=False)
    estado = Column(Enum('Activo','Inactivo'), nullable=False, default='Activo')
