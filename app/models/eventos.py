# models/eventos.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Evento(Base):
    __tablename__ = "evento"

    id_evento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    id_tipo = Column(Integer, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    id_usuario = Column(Integer, nullable=False)
    id_unidad_academica = Column(Integer, nullable=False)
