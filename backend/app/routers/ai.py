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


@router.post("/viabilidad/{candidato_id}")
async def analizar_viabilidad(
    candidato_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Candidato)
        .options(selectinload(Candidato.partido))
        .where(Candidato.id == candidato_id)
    )
    candidato = result.scalar_one_or_none()

    if not candidato:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = f"""Eres un economista y analista de políticas públicas peruano,
independiente y riguroso. Analiza la VIABILIDAD del plan de gobierno de
{candidato.nombre} ({candidato.partido.nombre}) para las elecciones 2026.

PLAN DE GOBIERNO OFICIAL (fuente: JNE):
{plan_gobierno}

INSTRUCCIONES DE BÚSQUEDA — ejecuta estas búsquedas:
1. "{candidato.nombre} propuestas económicas viabilidad 2026"
2. "Peru contexto económico fiscal 2026 presupuesto"
3. Busca experiencias internacionales de las propuestas más ambiciosas

FORMATO DE RESPUESTA:

## 💰 VIABILIDAD ECONÓMICA
¿Las propuestas económicas son fiscalmente sostenibles?
¿Hay fuentes de financiamiento identificadas?

## 🌍 COMPARACIÓN INTERNACIONAL
Para las 2-3 propuestas más importantes, casos de países
que implementaron políticas similares y sus resultados reales.

## ⚡ PROPUESTAS DE ALTO IMPACTO
Las 3 propuestas más ambiciosas evaluadas:
- ¿Es técnicamente factible?
- ¿Tiene precedentes exitosos?
- ¿Cuáles son los riesgos principales?

## 📊 VEREDICTO FINAL
Calificación: Alta / Media / Baja viabilidad — con justificación.

Sé directo, usa evidencia real, cita fuentes."""

    return StreamingResponse(
        stream_claude(prompt, model="claude-sonnet-4-20250514"),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )


@router.post("/comparar/{candidato_a_id}/{candidato_b_id}")
async def comparar_candidatos(
    candidato_a_id: int,
    candidato_b_id: int,
    db: AsyncSession = Depends(get_db)
):
    result_a = await db.execute(
        select(Candidato).options(selectinload(Candidato.partido))
        .where(Candidato.id == candidato_a_id)
    )
    result_b = await db.execute(
        select(Candidato).options(selectinload(Candidato.partido))
        .where(Candidato.id == candidato_b_id)
    )
    candidato_a = result_a.scalar_one_or_none()
    candidato_b = result_b.scalar_one_or_none()

    if not candidato_a or not candidato_b:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    plan_a = extraer_plan_gobierno(candidato_a.nombre)
    plan_b = extraer_plan_gobierno(candidato_b.nombre)

    prompt = f"""Eres un analista político peruano independiente y riguroso.
Compara a estos dos candidatos presidenciales para las elecciones 2026.

CANDIDATO A: {candidato_a.nombre} ({candidato_a.partido.nombre})
PLAN DE GOBIERNO A:
{plan_a}

CANDIDATO B: {candidato_b.nombre} ({candidato_b.partido.nombre})
PLAN DE GOBIERNO B:
{plan_b}

INSTRUCCIONES DE BÚSQUEDA:
1. "{candidato_a.nombre} propuestas 2026 historial"
2. "{candidato_b.nombre} propuestas 2026 historial"

FORMATO DE RESPUESTA — compara por cada eje temático:

## ⚖️ COMPARACIÓN: {candidato_a.nombre} vs {candidato_b.nombre}

### 💰 ECONOMÍA
**{candidato_a.nombre}:** propuesta económica en 2-3 líneas
**{candidato_b.nombre}:** propuesta económica en 2-3 líneas
**Diferencia clave:** qué los distingue en este eje

### 🔒 SEGURIDAD
**{candidato_a.nombre}:** propuesta en 2-3 líneas
**{candidato_b.nombre}:** propuesta en 2-3 líneas
**Diferencia clave:** qué los distingue

### 📚 EDUCACIÓN
**{candidato_a.nombre}:** propuesta en 2-3 líneas
**{candidato_b.nombre}:** propuesta en 2-3 líneas
**Diferencia clave:** qué los distingue

### 🏥 SALUD
**{candidato_a.nombre}:** propuesta en 2-3 líneas
**{candidato_b.nombre}:** propuesta en 2-3 líneas
**Diferencia clave:** qué los distingue

### ⚖️ CORRUPCIÓN
**{candidato_a.nombre}:** postura y antecedentes en 2-3 líneas
**{candidato_b.nombre}:** postura y antecedentes en 2-3 líneas
**Diferencia clave:** qué los distingue

### 🌿 MEDIO AMBIENTE
**{candidato_a.nombre}:** propuesta en 2-3 líneas
**{candidato_b.nombre}:** propuesta en 2-3 líneas
**Diferencia clave:** qué los distingue

### 📊 CONCLUSIÓN
Párrafo final balanceado destacando las diferencias más importantes.
No recomiendas por quién votar."""

    return StreamingResponse(
        stream_claude(prompt, model="claude-sonnet-4-20250514"),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )
