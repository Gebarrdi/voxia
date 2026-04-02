# routers/ai.py — análisis con Claude API usando streaming

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database import get_db
from app.models.candidato import Candidato, Propuesta
from app.config import get_settings
import anthropic
import json

router = APIRouter(prefix="/api/ai", tags=["Análisis IA"])
settings = get_settings()


def build_prompt_pros_contras(candidato: Candidato) -> str:
    # Construye el prompt con la información del candidato
    propuestas_texto = "\n".join([
        f"- [{p.tema.nombre}]: {p.descripcion}"
        for p in candidato.propuestas
    ]) or "No hay propuestas registradas."

    return f"""Eres un analista político neutral. Analiza al siguiente
candidato presidencial peruano de forma objetiva y equilibrada.

Candidato: {candidato.nombre}
Partido: {candidato.partido.nombre}
Biografía: {candidato.biografia or 'No disponible'}

Propuestas principales:
{propuestas_texto}

Proporciona:
1. **PROS**: 3 aspectos positivos fundamentados de su candidatura
2. **CONTRAS**: 3 aspectos negativos o riesgos de su candidatura
3. **CONCLUSIÓN**: Un párrafo neutral de resumen

Sé objetivo, usa evidencia y evita sesgos políticos.
IMPORTANTE: Este análisis es informativo. No constituye
recomendación de voto."""


def build_prompt_viabilidad(propuesta: Propuesta) -> str:
    return f"""Eres un economista y analista de políticas públicas neutral.
Analiza la viabilidad de la siguiente propuesta electoral peruana.

Candidato: {propuesta.candidato.nombre}
Tema: {propuesta.tema.nombre}
Propuesta: {propuesta.descripcion}

Proporciona:
1. **CONTEXTO**: Qué implica esta propuesta
2. **EXPERIENCIAS INTERNACIONALES**: 2-3 casos de países que implementaron
   políticas similares y sus resultados reales
3. **ANÁLISIS DE VIABILIDAD**: Factores económicos, sociales y fiscales
4. **CONCLUSIÓN**: ¿Es viable? ¿Bajo qué condiciones?

Basa tu análisis en evidencia real. Sé neutral y objetivo."""


async def stream_claude(prompt: str, model: str = "claude-haiku-4-5-20251001"):
    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    # Claude con web search — busca información real antes de analizar
    with client.messages.stream(
        model=model,
        max_tokens=4000,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search"
        }],
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for event in stream:
            # Solo enviamos los bloques de texto al frontend
            if hasattr(event, 'type'):
                if event.type == 'content_block_delta':
                    if hasattr(event.delta, 'text'):
                        data = json.dumps({'texto': event.delta.text})
                        yield f"data: {data}\n\n"
    yield "data: [DONE]\n\n"


@router.post("/pros-contras/{candidato_id}")
async def analizar_pros_contras(
    candidato_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Candidato)
        .options(
            selectinload(Candidato.partido),
            selectinload(Candidato.propuestas)
            .selectinload(Propuesta.tema)
        )
        .where(Candidato.id == candidato_id)
    )
    candidato = result.scalar_one_or_none()

    if not candidato:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    prompt = f"""Eres un analista político neutral peruano.
Analiza al candidato presidencial {candidato.nombre} de
{candidato.partido.nombre} para las elecciones peruanas
del 12 de abril de 2026.

INSTRUCCIONES:
1. Usa web_search para buscar información actualizada sobre:
   - "{candidato.nombre} plan de gobierno 2026"
   - "{candidato.nombre} propuestas presidenciales"
   - "{candidato.nombre} antecedentes historial político"
   - "{candidato.nombre} proyectos de ley aprobados"
     (si fue congresista)

2. Con la información encontrada, proporciona:

**PROS** (3 aspectos positivos fundamentados con
evidencia):
- Cada pro debe citar una fuente o dato concreto

**CONTRAS** (3 aspectos negativos o riesgos con
evidencia):
- Cada contra debe citar una fuente o dato concreto

**VIABILIDAD DE PROPUESTAS CLAVE**:
- Menciona 1-2 propuestas específicas de su plan y
  evalúa si son viables

**CONCLUSIÓN**:
- Párrafo neutral de resumen para el ciudadano

IMPORTANTE: Sé objetivo y neutral. No recomiendas por
quién votar. Este análisis es informativo para el
ciudadano peruano."""

    return StreamingResponse(
        stream_claude(prompt, model="claude-haiku-4-5-20251001"),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )


@router.post("/viabilidad/{propuesta_id}")
async def analizar_viabilidad(
    propuesta_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Propuesta)
        .options(
            selectinload(Propuesta.candidato),
            selectinload(Propuesta.tema)
        )
        .where(Propuesta.id == propuesta_id)
    )
    propuesta = result.scalar_one_or_none()

    if not propuesta:
        raise HTTPException(status_code=404, detail="Propuesta no encontrada")

    prompt = f"""Eres un economista y analista de políticas públicas neutral.
Analiza la viabilidad de esta propuesta electoral peruana 2026.

Candidato: {propuesta.candidato.nombre}
Propuesta: {propuesta.descripcion}
Tema: {propuesta.tema.nombre}

INSTRUCCIONES:
1. Usa web_search para buscar:
   - Experiencias internacionales de políticas similares
   - Resultados reales en otros países
   - Contexto económico del Perú relevante

2. Proporciona:
**CONTEXTO**: Qué implica esta propuesta
**EXPERIENCIAS INTERNACIONALES**: 2-3 casos reales con resultados
**ANÁLISIS DE VIABILIDAD**: Factores económicos y sociales
**CONCLUSIÓN**: ¿Es viable? ¿Bajo qué condiciones?

Basa todo en evidencia real. Sé neutral y objetivo."""

    return StreamingResponse(
        stream_claude(prompt, model="claude-sonnet-4-20250514"),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )
