# routers/ai.py — análisis con Claude API usando streaming

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database import get_db
from app.models.candidato import Candidato, Propuesta
from app.config import get_settings
from app.pdf_reader import extraer_plan_gobierno
import anthropic
import json

router = APIRouter(prefix="/api/ai", tags=["Análisis IA"])
settings = get_settings()


async def stream_claude(prompt: str, model: str = "claude-haiku-4-5-20251001"):
    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

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

    # Extraer plan de gobierno del PDF oficial JNE
    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = f"""Eres un analista político peruano independiente y riguroso.
Analiza al candidato presidencial {candidato.nombre} de \
{candidato.partido.nombre} para las elecciones peruanas del \
12 de abril de 2026.

PLAN DE GOBIERNO OFICIAL (fuente: JNE - Voto Informado):
{plan_gobierno}

INSTRUCCIONES DE BÚSQUEDA WEB — ejecuta estas búsquedas:
1. "{candidato.nombre} perfil académico universidad estudios"
2. "{candidato.nombre} trayectoria laboral cargos públicos empresas"
3. "{candidato.nombre} congresista proyectos de ley aprobados presentados"
4. "{candidato.nombre} casos corrupción investigaciones judiciales fiscalía"
5. "{candidato.nombre} escándalos cuestionamientos éticos "
        "2020 2021 2022 2023 2024 2025"
6. "{candidato.nombre} logros obras resultados gestión"
7. "{candidato.nombre} investigación periodística IDL OjoPúblico Hildebrandt"

FORMATO DE RESPUESTA — usa exactamente esta estructura:

## 👤 PERFIL ACADÉMICO Y PROFESIONAL
- Estudios universitarios y postgrados
- Trayectoria laboral (empresas, cargos, fechas)
- Si fue/es congresista: desde cuándo, proyectos presentados y aprobados

## 📋 PLAN DE GOBIERNO — PROPUESTAS CLAVE
Lista las 5-6 propuestas más importantes por eje temático
(economía, seguridad, educación, salud, corrupción).
Evalúa brevemente la viabilidad de cada una basándote
en experiencias internacionales similares.

## ✅ ASPECTOS POSITIVOS
3 puntos positivos con evidencia concreta y fuente.

## ⚠️ ASPECTOS NEGATIVOS Y RIESGOS
3 puntos negativos, investigaciones judiciales o
cuestionamientos éticos. Cita la fuente específica.
No omitas información negativa relevante.

## 🔍 INVESTIGACIONES PERIODÍSTICAS
Menciona investigaciones de IDL-Reporteros, OjoPúblico,
La República, El Comercio, Hildebrandt, etc.
con la fuente y año específicos.

## 📊 CONCLUSIÓN NEUTRAL
Párrafo balanceado sin recomendar por quién votar.
El ciudadano decide con información completa.

IMPORTANTE:
- Sé directo y sin eufemismos
- Cita fuentes específicas
- No omitas información negativa relevante
- No recomiendas por quién votar"""

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
