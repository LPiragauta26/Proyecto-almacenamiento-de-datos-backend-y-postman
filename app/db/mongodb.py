from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config.mongo_config import settings
from app.db.modelsregistry import document_models

class DataBase:
    client: AsyncIOMotorClient | None = None

db = DataBase()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    await init_beanie(database=db.client[settings.MONGO_DB_NAME], document_models=document_models)

async def close_mongo_connection():
    if db.client:
        db.client.close()

