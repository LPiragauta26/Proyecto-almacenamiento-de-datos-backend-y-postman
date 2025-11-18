# app/routers/eventos_mongo_router.py
from fastapi import APIRouter, HTTPException
from app.mongo.evento_mongo import EventoMongo

router = APIRouter(prefix="/eventos", tags=["Eventos Mongo"])

@router.post("/")
async def crear_evento(evento: EventoMongo):
    evento = await evento.insert()
    return {"id": str(evento.id)}

@router.get("/")
async def listar_eventos():
    eventos = await EventoMongo.find_all().to_list()
    return eventos

@router.get("/{evento_id}")
async def obtener_evento(evento_id: str):
    evento = await EventoMongo.get(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento

@router.put("/{evento_id}")
async def actualizar_evento(evento_id: str, datos: EventoMongo):
    evento = await EventoMongo.get(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    await evento.update({"$set": datos.dict(exclude_unset=True)})
    return {"status": "Evento actualizado"}

@router.delete("/{evento_id}")
async def eliminar_evento(evento_id: str):
    evento = await EventoMongo.get(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    await evento.delete()
    return {"status": "Evento eliminado"}
