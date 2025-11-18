# app/routers/mongo_test.py
from fastapi import APIRouter
from app.mongo.conexion import mongo_db

router = APIRouter()

@router.get("/test_mongo")
async def test_mongo():
    if mongo_db is None:
        return {"error": "MongoDB NO está conectado"}

    colecciones = await mongo_db.list_collection_names()
    return {"estado": "OK", "colecciones": colecciones}