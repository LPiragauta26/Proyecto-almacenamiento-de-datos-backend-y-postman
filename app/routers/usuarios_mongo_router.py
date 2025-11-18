# app/routers/usuarios_mongo_router.py
from fastapi import APIRouter, HTTPException
from app.mongo.usuario_mongo import UsuarioMongo

router = APIRouter(prefix="/usuarios", tags=["Usuarios Mongo"])

@router.post("/")
async def crear_usuario(usuario: UsuarioMongo):
    usuario = await usuario.insert()
    return {"id": str(usuario.id)}

@router.get("/")
async def listar_usuarios():
    usuarios = await UsuarioMongo.find_all().to_list()
    return usuarios

@router.get("/{usuario_id}")
async def obtener_usuario(usuario_id: str):
    usuario = await UsuarioMongo.get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}")
async def actualizar_usuario(usuario_id: str, datos: UsuarioMongo):
    usuario = await UsuarioMongo.get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    await usuario.update({"$set": datos.dict(exclude_unset=True)})
    return {"status": "Usuario actualizado"}

@router.delete("/{usuario_id}")
async def eliminar_usuario(usuario_id: str):
    usuario = await UsuarioMongo.get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    await usuario.delete()
    return {"status": "Usuario eliminado"}
