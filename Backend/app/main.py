from fastapi import FastAPI
from app.routers import usuarios
from app.database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir el router de usuarios
app.include_router(usuarios.router)

@app.get("/")
def root():
    return {"mensaje": "API de Gestión de Usuarios activa"}