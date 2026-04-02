# routers/temas.py — endpoint de temas

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.candidato import Tema

router = APIRouter(
    prefix="/api/temas",
    tags=["Temas"]
)


@router.get("/")
async def get_temas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tema))
    temas = result.scalars().all()
    return [
        {
            "id": t.id,
            "nombre": t.nombre,
            "descripcion": t.descripcion,
            "icono": t.icono
        }
        for t in temas
    ]
