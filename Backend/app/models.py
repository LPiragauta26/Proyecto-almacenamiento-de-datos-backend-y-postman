# app/models.py
from sqlalchemy import Column, String, Integer, BigInteger, Text, Enum, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "Usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(120), unique=True)
    rol = Column(Enum('Docente', 'Estudiante', 'Administrador', name='rol_enum'), default='Estudiante')
    estado = Column(Enum('Activo', 'Inactivo', name='estado_enum'), default='Activo')

class Lugar(Base):
    __tablename__ = "Lugar"
    id_lugar = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    capacidad = Column(Integer)
    tipo = Column(Enum("Auditorio", "Laboratorio", "Salon"), nullable=False)
    ubicacion = Column(String(255))

class Evento(Base):
    __tablename__ = "Evento"
    id_evento = Column(BigInteger, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text)
    tipo = Column(Enum("Academico", "Ludico"), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    id_lugar = Column(BigInteger, ForeignKey("Lugar.id_lugar"), nullable=True)
    estado = Column(Enum("Registrado", "Pendiente", "Aprobado", "Rechazado"), default="Registrado", nullable=False)

    lugar = relationship("Lugar")
