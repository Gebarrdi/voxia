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
3. "{candidato.nombre} congresista proyectos de ley aprobados \
presentados"
4. "{candidato.nombre} casos corrupción investigaciones judiciales \
fiscalía"
5. "{candidato.nombre} escándalos cuestionamientos éticos 2020 2021 \
2022 2023 2024 2025"
6. "{candidato.nombre} logros obras resultados gestión"
7. "{candidato.nombre} investigación periodística IDL OjoPúblico \
Hildebrandt"

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

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    prompt = f"""Eres un analista político peruano independiente y riguroso.
Compara a estos dos candidatos presidenciales para las \
elecciones peruanas 2026.

CANDIDATO A: {candidato_a.nombre} ({candidato_a.partido.nombre})
PLAN DE GOBIERNO A:
{plan_a}

CANDIDATO B: {candidato_b.nombre} ({candidato_b.partido.nombre})
PLAN DE GOBIERNO B:
{plan_b}

INSTRUCCIONES DE BÚSQUEDA — ejecuta estas búsquedas:
1. "{candidato_a.nombre} propuestas 2026 historial antecedentes"
2. "{candidato_b.nombre} propuestas 2026 historial antecedentes"

IMPORTANTE: Responde ÚNICAMENTE con un JSON válido, sin texto adicional,
sin bloques de código, sin explicaciones. Solo el JSON puro.

{{
  "temas": {{
    "Economía": {{
      "puntaje_a": 7,
      "puntaje_b": 6,
      "ganador": "A",
      "resumen_a": "propuesta económica de A en 2-3 líneas",
      "resumen_b": "propuesta económica de B en 2-3 líneas",
      "analisis_expertos": (
          "análisis técnico para politólogos, economistas "
          "en 4-5 líneas con evidencia y fuentes"
      ),
      "explicacion_ciudadano": (
          "explicación simple para el ciudadano en 1-2 "
          "líneas sin tecnicismos"
      )
    }},
    "Seguridad": {{
      "puntaje_a": 8,
      "puntaje_b": 5,
      "ganador": "B",
      "resumen_a": "propuesta de seguridad de A en 2-3 líneas",
      "resumen_b": "propuesta de seguridad de B en 2-3 líneas",
      "analisis_expertos": "análisis técnico en 4-5 líneas",
      "explicacion_ciudadano": "explicación simple en 1-2 líneas"
    }},
    "Educación": {{
      "puntaje_a": 6,
      "puntaje_b": 8,
      "ganador": "A",
      "resumen_a": "...",
      "resumen_b": "...",
      "analisis_expertos": "...",
      "explicacion_ciudadano": "..."
    }},
    "Salud": {{
      "puntaje_a": 7,
      "puntaje_b": 7,
      "ganador": "empate",
      "resumen_a": "...",
      "resumen_b": "...",
      "analisis_expertos": "...",
      "explicacion_ciudadano": "..."
    }},
    "Transporte": {{
      "puntaje_a": 5,
      "puntaje_b": 8,
      "ganador": "B",
      "resumen_a": "...",
      "resumen_b": "...",
      "analisis_expertos": "...",
      "explicacion_ciudadano": "..."
    }},
    "Tecnología": {{
      "puntaje_a": 6,
      "puntaje_b": 7,
      "ganador": "A",
      "resumen_a": "...",
      "resumen_b": "...",
      "analisis_expertos": "...",
      "explicacion_ciudadano": "..."
    }},
    "Medio Ambiente": {{
      "puntaje_a": 8,
      "puntaje_b": 5,
      "ganador": "A",
      "resumen_a": "...",
      "resumen_b": "...",
      "analisis_expertos": "...",
      "explicacion_ciudadano": "..."
    }},
    "Corrupción": {{
      "puntaje_a": 4,
      "puntaje_b": 7,
      "ganador": "B",
      "resumen_a": "antecedentes y postura de A",
      "resumen_b": "antecedentes y postura de B",
      "analisis_expertos": (
          "análisis técnico de antecedentes y propuestas "
          "anticorrupción con fuentes"
      ),
      "explicacion_ciudadano": "explicación simple para el ciudadano"
    }}
  }},
  "ganador_general": "A",
  "puntaje_total_a": 51,
  "puntaje_total_b": 53,
  "conclusion_expertos": (
      "análisis técnico global para politólogos, abogados, "
      "economistas en 5-6 líneas con evidencia"
  ),
  "conclusion_ciudadano": (
      "resumen simple para el ciudadano promedio en 2-3 "
      "líneas sin tecnicismos"
  ),
  "nota_neutralidad": (
      "Este análisis es informativo y no constituye "
      "recomendación de voto"
  )
}}

Reglas para los puntajes:
- Del 1 al 10 basado en concreción, viabilidad y coherencia de propuestas
- Si no hay propuesta clara en un tema, el puntaje máximo es 4
- El ganador general es quien tiene mayor suma de puntajes
- Si la diferencia total es menor a 3 puntos, es empate"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search"
        }],
        messages=[{"role": "user", "content": prompt}]
    )

    texto = ""
    for block in response.content:
        if hasattr(block, "text"):
            texto += block.text

    try:
        texto_limpio = texto.strip()
        if texto_limpio.startswith("```"):
            texto_limpio = texto_limpio.split("```")[1]
            if texto_limpio.startswith("json"):
                texto_limpio = texto_limpio[4:]
        resultado = json.loads(texto_limpio)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar respuesta de IA: {str(e)}"
        )
