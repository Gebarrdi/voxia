# routers/candidatos.py — endpoints de candidatos
# Aquí viven las rutas que el frontend va a llamar

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.candidato_service import CandidatoService
from app.schemas.candidato import CandidatoListSchema, CandidatoDetailSchema

# El router agrupa todos los endpoints de candidatos
# prefix — todas las rutas empiezan con /api/candidatos
# tags — agrupa los endpoints en el Swagger
router = APIRouter(
    prefix="/api/candidatos",
    tags=["Candidatos"]
)


@router.get("/", response_model=list[CandidatoListSchema])
async def get_candidatos(db: AsyncSession = Depends(get_db)):
    # Depends(get_db) — FastAPI inyecta la sesión automáticamente
    # Es el mismo concepto que @Autowired en Spring Boot
    service = CandidatoService(db)
    return await service.get_all()


@router.get("/{candidato_id}", response_model=CandidatoDetailSchema)
async def get_candidato(
    candidato_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = CandidatoService(db)
    candidato = await service.get_by_id(candidato_id)

    # Si no existe devuelve 404 — exactamente como definimos en el contrato
    if not candidato:
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )
    return candidato
