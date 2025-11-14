from sqlalchemy import Column, String, Integer, BigInteger, Text, Enum, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


# ============================
#        USUARIO
# ============================
class Usuario(Base):
    __tablename__ = "usuario"   # Debe coincidir EXACTO con MySQL

    id_usuario = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    apellido = Column(String(60), nullable=False)
    correo = Column(String(120), unique=True)
    rol = Column(Enum('Docente', 'Estudiante', 'Secretario', 'Administrador'))
    estado = Column(Enum('Activo', 'Inactivo'), default='Activo')


# ============================
#   UNIDAD ACADÉMICA
# ============================
class UnidadAcademica(Base):
    __tablename__ = "unidad_academica"

    id_unidad_academica = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    id_facultad = Column(BigInteger, ForeignKey("facultad.id_facultad"))


# ============================
#          EVENTO
# ============================
class Evento(Base):
    __tablename__ = "evento"  # EXACTO al SQL

    id_evento = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(60), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)

    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"), nullable=False)
    id_unidad_academica = Column(BigInteger, ForeignKey("unidad_academica.id_unidad_academica"), nullable=False)

    usuario = relationship("Usuario")
    unidad_academica = relationship("UnidadAcademica")
