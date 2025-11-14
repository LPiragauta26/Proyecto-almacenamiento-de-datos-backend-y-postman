# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios, eventos

app = FastAPI(
    title="Gestión de Eventos Universitarios",
    description="API para gestionar usuarios, eventos y unidades académicas.",
    version="1.0.0"
)

# Configuración CORS (permite conexiones desde el navegador)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Gestión de Eventos"}

# Registrar rutas
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])