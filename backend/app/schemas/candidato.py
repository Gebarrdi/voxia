# schemas/candidato.py — esquemas Pydantic para validar datos
# Define qué datos entran y salen de la API (el "contrato" en código)

from pydantic import BaseModel
from typing import Optional


# Schema de partido político (solo lectura)
class PartidoSchema(BaseModel):
    id: int
    nombre: str
    siglas: str
    logo_url: Optional[str] = None

    class Config:
        from_attributes = True  # permite convertir objetos SQLAlchemy a JSON


# Schema básico de candidato — para la lista
class CandidatoListSchema(BaseModel):
    id: int
    nombre: str
    foto_url: Optional[str] = None
    partido: PartidoSchema

    class Config:
        from_attributes = True


# Schema completo de candidato — para el perfil
class CandidatoDetailSchema(BaseModel):
    id: int
    nombre: str
    foto_url: Optional[str] = None
    biografia: Optional[str] = None
    fuente_jne: Optional[str] = None
    partido: PartidoSchema

    class Config:
        from_attributes = True
