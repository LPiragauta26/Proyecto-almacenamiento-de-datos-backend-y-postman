# app/mongo/test_crud.py
import asyncio
from datetime import date
from app.mongo.conexion import iniciar_mongo
from app.mongo.usuario_mongo import UsuarioMongo
from app.mongo.evento_mongo import EventoMongo

async def test_crud():
    await iniciar_mongo()

    # Crear un usuario
    usuario = UsuarioMongo(nombre="Laura", apellido="Piragauta", correo="laura@test.com", rol="Estudiante")
    await usuario.insert()
    print("Usuario creado:", usuario.id)

    # Crear un evento
    evento = EventoMongo(
        nombre="Evento de prueba",
        id_tipo=1,
        fecha_inicio=date.today(),
        fecha_fin=date.today(),
        id_usuario=str(usuario.id),
        id_unidad_academica="1"
    )
    await evento.insert()
    print("Evento creado:", evento.id)

    # Leer el usuario
    usuario_db = await UsuarioMongo.get(usuario.id)
    print("Usuario en DB:", usuario_db)

    # Leer el evento
    evento_db = await EventoMongo.get(evento.id)
    print("Evento en DB:", evento_db)

asyncio.run(test_crud())
