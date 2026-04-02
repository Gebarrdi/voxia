# services/candidato_service.py — lógica de negocio de candidatos
# El intermediario entre el router y el repository

from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.candidato_repository import CandidatoRepository
from app.models.candidato import Candidato


class CandidatoService:

    def __init__(self, db: AsyncSession):
        # Crea el repository pasándole la sesión de BD
        self.repository = CandidatoRepository(db)

    async def get_all(self) -> list[Candidato]:
        # Por ahora solo delega al repository
        # Aquí podrías agregar lógica extra: filtros, ordenamiento, etc.
        return await self.repository.get_all()

    async def get_by_id(self, candidato_id: int) -> Candidato | None:
        return await self.repository.get_by_id(candidato_id)
