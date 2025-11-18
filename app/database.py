# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Ejemplo: mysql+pymysql://user:pass@host:port/dbname
MYSQL_URL = os.getenv("MYSQL_URL", "mysql+pymysql://root:root@localhost:3306/gestion_eventos")

engine = create_engine(MYSQL_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
try:
    conn = engine.connect()
    print("🔥 Conexión a MySQL exitosa")
    conn.close()
except Exception as e:
    print("❌ Error conectando a MySQL:", e)