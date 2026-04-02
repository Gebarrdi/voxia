# routers/comparar.py — endpoint de comparación entre candidatos

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database import get_db
from app.models.candidato import Candidato, Propuesta, Tema

router = APIRouter(
    prefix="/api/comparar",
    tags=["Comparación"]
)


@router.get("/")
async def comparar_candidatos(
    a: int,  # id candidato A — viene como query param: ?a=1&b=2
    b: int,  # id candidato B
    db: AsyncSession = Depends(get_db)
):
    # Validación — no puedes comparar un candidato consigo mismo
    if a == b:
        raise HTTPException(
            status_code=400,
            detail="Selecciona dos candidatos diferentes"
        )

    # Obtener candidato A con sus propuestas y temas
    result_a = await db.execute(
        select(Candidato)
        .options(
            selectinload(Candidato.partido),
            selectinload(Candidato.propuestas)
            .selectinload(Propuesta.tema)
        )
        .where(Candidato.id == a)
    )
    candidato_a = result_a.scalar_one_or_none()

    # Obtener candidato B
    result_b = await db.execute(
        select(Candidato)
        .options(
            selectinload(Candidato.partido),
            selectinload(Candidato.propuestas)
            .selectinload(Propuesta.tema)
        )
        .where(Candidato.id == b)
    )
    candidato_b = result_b.scalar_one_or_none()

    # Verificar que ambos existen
    if not candidato_a:
        raise HTTPException(
            status_code=404,
            detail=f"Candidato {a} no encontrado"
        )
    if not candidato_b:
        raise HTTPException(
            status_code=404,
            detail=f"Candidato {b} no encontrado"
        )

    # Obtener todos los temas
    result_temas = await db.execute(select(Tema))
    temas = result_temas.scalars().all()

    # Construir comparación por tema
    comparacion = {}
    for tema in temas:
        # Buscar propuestas de cada candidato para este tema
        prop_a = [
            p.descripcion for p in candidato_a.propuestas
            if p.tema_id == tema.id
        ]
        prop_b = [
            p.descripcion for p in candidato_b.propuestas
            if p.tema_id == tema.id
        ]
        comparacion[tema.nombre] = {
            "a": prop_a if prop_a else ["Sin propuestas registradas"],
            "b": prop_b if prop_b else ["Sin propuestas registradas"]
        }

    return {
        "candidato_a": {
            "id": candidato_a.id,
            "nombre": candidato_a.nombre,
            "partido": candidato_a.partido.nombre
        },
        "candidato_b": {
            "id": candidato_b.id,
            "nombre": candidato_b.nombre,
            "partido": candidato_b.partido.nombre
        },
        "comparacion": comparacion
    }
