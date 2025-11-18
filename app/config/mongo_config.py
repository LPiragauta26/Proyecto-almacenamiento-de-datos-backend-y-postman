from motor.motor_asyncio import AsyncIOMotorClient

# Connection string actualizado
MONGO_URL = "mongodb+srv://admin:Clarent12@cluster0.smbqnrq.mongodb.net/sigeu_mongo?retryWrites=true&w=majority&appName=Cluster0"

# Crear cliente de MongoDB
client = AsyncIOMotorClient(MONGO_URL)

# Seleccionar base de datos
db_mongo = client["sigeu_mongo"]

