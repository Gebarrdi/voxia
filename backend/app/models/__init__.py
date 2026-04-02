# E importa todos los modelos para que SQLAlchemy los registre

from app.models.candidato import (  # noqa: F401
    PartidoPolitico,
    Candidato,
    Tema,
    Propuesta,
    Antecedente
)
