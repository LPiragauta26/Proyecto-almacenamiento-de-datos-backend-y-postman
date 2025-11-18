# app/mongo/test_conexion.py
import asyncio
from app.mongo.conexion import iniciar_mongo, mongo_db

async def test():
    await iniciar_mongo()
    print("Bases de datos disponibles:", await mongo_db.list_collection_names())

asyncio.run(test())
