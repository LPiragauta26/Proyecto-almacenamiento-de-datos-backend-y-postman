# app/mongo/usuario_mongo.py
from beanie import Document

class UsuarioMongo(Document):
    nombre: str
    apellido: str
    correo: str
    rol: str
    estado: str = "Activo"

    class Settings:
        name = "usuarios_mongo"