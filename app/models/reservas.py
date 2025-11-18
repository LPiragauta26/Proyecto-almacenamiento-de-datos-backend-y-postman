from sqlalchemy import Column, BigInteger, ForeignKey
from app.database import Base

class Reserva(Base):
    __tablename__ = "reserva"

    id_reserva = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario", ondelete="CASCADE", onupdate="CASCADE"))
    id_evento = Column(BigInteger, ForeignKey("evento.id_evento", ondelete="CASCADE", onupdate="CASCADE"))

