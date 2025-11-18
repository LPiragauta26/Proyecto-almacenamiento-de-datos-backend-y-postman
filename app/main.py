from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# SQL
from app.database import Base, engine
from app import models
from app.routers.usuarios import router as usuarios_router
from app.routers.eventos import router as eventos_router
from app.routers.reservas import router as reservas_router
from app.routers.evaluaciones import router as evaluaciones_router

# Mongo
from app.mongo.conexion import iniciar_mongo, cerrar_mongo
from app.routers.usuarios_mongo_router import router as usuarios_mongo_router
from app.routers.eventos_mongo_router import router as eventos_mongo_router

# Cargar variables de entorno
load_dotenv()

# Crear tablas SQL
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestión de Eventos Universitarios",
    description="API completa con CRUD SQL y Mongo",
    version="1.0.0"
)

# ============================================================
# Eventos de inicio y cierre
# ============================================================

@app.on_event("startup")
async def startup_event():
    await iniciar_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await cerrar_mongo()

# ============================================================
# Middleware
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# Ruta raíz
# ============================================================

@app.get("/")
def root():
    return {"mensaje": "API Gestión de Eventos funcionando 🚀"}

# ============================================================
# Routers SQL
# ============================================================

app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(eventos_router, prefix="/eventos", tags=["Eventos"])
app.include_router(reservas_router, prefix="/reservas", tags=["Reservas"])
app.include_router(evaluaciones_router, prefix="/evaluaciones", tags=["Evaluaciones"])

# ============================================================
# Routers Mongo
# ============================================================

app.include_router(usuarios_mongo_router, prefix="/mongo/usuarios", tags=["Usuarios Mongo"])
app.include_router(eventos_mongo_router, prefix="/mongo/eventos", tags=["Eventos Mongo"])
