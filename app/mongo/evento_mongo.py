# app/mongo/evento_mongo.py
from beanie import Document
from datetime import date
from typing import Optional

class EventoMongo(Document):
    nombre: str
    id_tipo: int
    fecha_inicio: date
    fecha_fin: date
    id_usuario: Optional[str]
    id_unidad_academica: Optional[str]

    class Settings:
        name = "eventos_mongo"
