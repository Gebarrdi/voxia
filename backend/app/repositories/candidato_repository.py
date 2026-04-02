# repositories/candidato_repository.py — acceso a datos de candidatos
# Este es el DAO que ya conocías de Java, pero en Python

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models.candidato import Candidato, PartidoPolitico  # noqa: F401


class CandidatoRepository:

    def __init__(self, db: AsyncSession):
        # Recibe la sesión de BD como dependencia
        self.db = db

    async def get_all(self) -> list[Candidato]:
        # SELECT * FROM candidato JOIN partido_politico
        # selectinload carga la relación partido automáticamente
        result = await self.db.execute(
            select(Candidato).options(
                selectinload(Candidato.partido)
            )
        )
        return result.scalars().all()

    async def get_by_id(self, candidato_id: int) -> Candidato | None:
        # SELECT * FROM candidato WHERE id = candidato_id
        result = await self.db.execute(
            select(Candidato)
            .options(
                selectinload(Candidato.partido),
                selectinload(Candidato.propuestas),
                selectinload(Candidato.antecedentes)
            )
            .where(Candidato.id == candidato_id)
        )
        return result.scalar_one_or_none()  # None si no existe
