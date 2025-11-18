# app/mongo/conexion.py
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os
from dotenv import load_dotenv

# Modelos Mongo
from app.mongo.usuario_mongo import UsuarioMongo
from app.mongo.evento_mongo import EventoMongo

load_dotenv()

MONGO_URL = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "sigeu_mongo")

mongo_client: AsyncIOMotorClient | None = None

async def iniciar_mongo():
    global mongo_client
    try:
        mongo_client = AsyncIOMotorClient(MONGO_URL)
        # Inicializar Beanie
        await init_beanie(
            database=mongo_client[MONGO_DB_NAME],
            document_models=[UsuarioMongo, EventoMongo]
        )
        print("✅ Conectado e inicializado MongoDB correctamente")
    except Exception as e:
        print("❌ Error conectando a Mongo:", e)

async def cerrar_mongo():
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("🔒 Conexión Mongo cerrada")
