from sqlalchemy import Column, Enum, Text, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT
from app.database import Base

class Evaluacion(Base):
    __tablename__ = "evaluacion"

    id_evaluacion = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    id_evento = Column(BIGINT(unsigned=True), ForeignKey("evento.id_evento", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    estado = Column(Enum('Pendiente','Aprobado','Rechazado'), nullable=False)
    justificacion = Column(Text)
