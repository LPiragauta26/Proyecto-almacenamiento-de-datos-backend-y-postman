from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://admin:Clarent12@cluster0.smbqnrq.mongodb.net/sigeu_mongo?retryWrites=true&w=majority&appName=Cluster0")
client = AsyncIOMotorClient(MONGO_URI)
db = client.sigeu_mongo  # nombre de tu base de datos
