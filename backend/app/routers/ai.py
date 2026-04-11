# routers/ai.py — análisis con Claude API

import asyncio
import json
import re

import anthropic
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.dialects.postgresql import insert as pg_insert

from app.database import get_db
from app.models.candidato import Candidato, Propuesta, CacheAnalisis
from app.config import get_settings
from app.pdf_reader import extraer_plan_gobierno

router = APIRouter(prefix="/api/ai", tags=["Análisis IA"])
settings = get_settings()


def get_apellido(nombre: str) -> str:
    partes = nombre.split()
    if len(partes) >= 3:
        return f"{partes[0]} {partes[2]}"
    elif len(partes) == 2:
        return f"{partes[0]} {partes[1]}"
    return partes[0]


def limpiar_intro(texto: str) -> str:
    """Elimina frases introductorias antes del primer ##."""
    if not texto:
        return texto
    match = re.search(r'^#{1,3} ', texto, re.MULTILINE)
    if match and match.start() > 0:
        texto_antes = texto[:match.start()]
        frases_intro = [
            'voy a', 'busco', 'ahora busco', 'permíteme', 'let me',
            'procedo', 'realiz', 'analiz', 'necesito buscar',
            'a continuación', 'procederé', 'ahora voy', 'buscaré',
            'comenzaré', 'empezaré', 'haré una búsqueda'
        ]
        if any(f in texto_antes.lower() for f in frases_intro):
            return texto[match.start():].strip()
    return texto


async def get_cache(db: AsyncSession, tipo: str, clave: str) -> str | None:
    """Busca en caché. Retorna contenido o None."""
    result = await db.execute(
        select(CacheAnalisis)
        .where(CacheAnalisis.tipo == tipo)
        .where(CacheAnalisis.clave == clave)
    )
    cache = result.scalar_one_or_none()
    return cache.contenido if cache else None


async def set_cache(
    db: AsyncSession, tipo: str, clave: str, contenido: str
) -> None:
    stmt = pg_insert(CacheAnalisis).values(
        tipo=tipo,
        clave=clave,
        contenido=contenido
    ).on_conflict_do_update(
        index_elements=['tipo', 'clave'],  # ← ahora usa ambas columnas
        set_={'contenido': contenido}
    )
    await db.execute(stmt)
    await db.commit()


def collect_claude(prompt: str, model: str) -> str:
    """
    Llama a Claude de forma síncrona y retorna el texto completo.
    Diseñado para correr en asyncio.to_thread().
    """
    ac = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    chunks = []
    with ac.messages.stream(
        model=model,
        max_tokens=6000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for event in stream:
            if hasattr(event, 'type'):
                if event.type == 'content_block_delta':
                    if hasattr(event.delta, 'text'):
                        chunks.append(event.delta.text)
    return "".join(chunks)


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

    clave = str(candidato_id)
    cached = await get_cache(db, "pros_contras", clave)
    if cached:
        print(f"CACHE HIT: pros_contras:{clave}")
        return {"texto": cached}

    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = (
        f"IMPORTANTE: Responde DIRECTAMENTE con el análisis.\n"
        f"- Empieza DIRECTAMENTE con '## 👤 PERFIL ACADÉMICO Y PROFESIONAL'\n"
        f"- NO escribas ninguna frase antes del primer ##\n"
        f"No escribas frases como 'Entendido', 'Voy a realizar',\n"
        f"'Permíteme buscar' o similares. Empieza directo con\n"
        f"## 👤 PERFIL ACADÉMICO Y PROFESIONAL\n\n"
        f"Eres un analista político peruano independiente y riguroso.\n"
        f"Analiza al candidato presidencial {candidato.nombre} de "
        f"{candidato.partido.nombre} para las elecciones peruanas "
        f"del 12 de abril de 2026.\n\n"
        f"PLAN DE GOBIERNO OFICIAL (fuente: JNE - Voto Informado):\n"
        f"{plan_gobierno}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA WEB:\n"
        f'1. "{candidato.nombre} perfil académico universidad estudios"\n'
        f'2. "{candidato.nombre} trayectoria laboral cargos públicos"\n'
        f'3. "{candidato.nombre} congresista proyectos de ley gestión"\n'
        f'4. "{candidato.nombre} antecedentes judiciales penales"\n'
        f'5. "{candidato.nombre} investigación corrupción sentencias"\n'
        f'6. "{candidato.nombre} logros obras resultados gestión"\n'
        f'7. "{candidato.nombre} IDL OjoPúblico Hildebrandt Caretas"\n\n'
        f"FORMATO DE RESPUESTA:\n\n"
        f"## 👤 PERFIL ACADÉMICO Y PROFESIONAL\n"
        f"- Estudios universitarios y postgrados\n"
        f"- Trayectoria laboral (empresas, cargos, fechas)\n"
        f"- Si fue/es congresista: proyectos, asistencia, comisiones\n"
        f"- Cargos públicos previos y resultados\n\n"
        f"## 📋 PROPUESTAS CLAVE DEL PLAN DE GOBIERNO\n"
        f"Lista las 6-7 propuestas más importantes.\n"
        f"SOLO LISTARLAS, no evaluarlas.\n"
        f"- [Eje temático]: descripción concreta\n\n"
        f"## ✅ ASPECTOS POSITIVOS DEL CANDIDATO\n"
        f"3-4 aspectos positivos de la PERSONA (no del plan).\n"
        f"Cada punto debe citar fuente o dato concreto.\n\n"
        f"## ⚠️ ASPECTOS NEGATIVOS Y RIESGOS DEL CANDIDATO\n"
        f"3-4 aspectos negativos de la PERSONA.\n"
        f"Cita fuente específica. No omitas negativos relevantes.\n\n"
        f"## 🔍 INVESTIGACIONES PERIODÍSTICAS\n"
        f"IDL-Reporteros, OjoPúblico, Caretas, La República,\n"
        f"El Comercio, Hildebrandt. Incluye medio, año y hallazgo.\n\n"
        f"## 📊 CONCLUSIÓN NEUTRAL\n"
        f"Párrafo balanceado. Sin evaluar el plan.\n"
        f"Sin recomendar por quién votar.\n\n"
        f"REGLAS DE FORMATO ESTRICTAS:\n"
        f"- Cada punto de lista DEBE estar en UNA SOLA LÍNEA\n"
        f"- CORRECTO: '- **Título:** descripción del hecho'\n"
        f"- INCORRECTO: '-' sola en una línea, con texto abajo\n"
        f"- NUNCA salto de línea entre el guión y el contenido\n"
        f"- Si no hay dato concreto para un punto, omite ese punto\n"
        f"- Analiza al CANDIDATO, no al plan\n"
        f"- Las propuestas solo se listan, no se evalúan\n"
        f"- Sé directo y sin eufemismos\n"
        f"- No omitas antecedentes negativos relevantes\n"
        f"- No recomiendas por quién votar"
    )

    texto = await asyncio.to_thread(
        collect_claude, prompt, "claude-haiku-4-5-20251001"
    )
    texto = limpiar_intro(texto)
    await set_cache(db, "pros_contras", clave, texto)
    return {"texto": texto}


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

    clave = str(candidato_id)
    cached = await get_cache(db, "viabilidad", clave)
    if cached:
        print(f"CACHE HIT: viabilidad:{clave}")
        return {"texto": cached}

    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = (
        f"IMPORTANTE: Responde DIRECTAMENTE con el análisis.\n"
        f"No escribas frases como 'Necesito buscar', 'Permíteme',\n"
        f"'Ahora procederé', 'Entendido' o similares.\n"
        f"Empieza directo con ## 1. [NOMBRE DE LA PROPUESTA]\n\n"
        f"Eres un economista y analista de políticas públicas peruano,\n"
        f"especializado en finanzas públicas y evaluación de programas.\n"
        f"Analiza la VIABILIDAD ESPECÍFICA de cada propuesta del plan\n"
        f"de gobierno de {candidato.nombre} "
        f"({candidato.partido.nombre}).\n\n"
        f"PLAN DE GOBIERNO OFICIAL (fuente: JNE):\n"
        f"{plan_gobierno}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA:\n"
        f'1. "Peru presupuesto fiscal 2026 MEF déficit"\n'
        f'2. "Peru PBI crecimiento inflación informalidad 2025 2026"\n'
        f"3. Para cada propuesta, busca experiencias internacionales\n\n"
        f"TAREA: Identifica las 5-7 propuestas más importantes\n"
        f"y analiza CADA UNA con este formato:\n\n"
        f"## [NÚMERO]. [NOMBRE DE LA PROPUESTA]\n\n"
        f"**Qué propone:** descripción clara en 2-3 líneas.\n\n"
        f"**Costo estimado:** cuánto costaría implementarlo.\n\n"
        f"**Precedentes internacionales:** 1-2 países con\n"
        f"resultados reales y concretos.\n\n"
        f"**Restricciones:** obstáculos en el contexto peruano.\n\n"
        f"**Veredicto:** Alta / Media / Baja viabilidad.\n\n"
        f"---\n\n"
        f"## 📊 VEREDICTO GLOBAL DEL PLAN\n"
        f"Coherencia fiscal. ¿Propuestas consistentes entre sí?\n"
        f"¿Financiamiento realista?\n\n"
        f"REGLAS:\n"
        f"- Sé directo y sin eufemismos\n"
        f"- Usa datos reales: MEF, INEI, BM, FMI, CEPAL\n"
        f"- Si es inviable, dilo claramente"
    )

    texto = await asyncio.to_thread(
        collect_claude, prompt, "claude-sonnet-4-20250514"
    )
    texto = limpiar_intro(texto)
    await set_cache(db, "viabilidad", clave, texto)
    return {"texto": texto}


@router.post("/comparar/{candidato_a_id}/{candidato_b_id}")
async def comparar_candidatos(
    candidato_a_id: int,
    candidato_b_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Puntajes y resúmenes en JSON."""
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

    id_min = min(candidato_a_id, candidato_b_id)
    id_max = max(candidato_a_id, candidato_b_id)
    clave = f"{id_min}:{id_max}"

    cached = await get_cache(db, "comparacion", clave)
    if cached:
        print(f"CACHE HIT: comparacion:{clave}")
        return json.loads(cached)

    plan_a = extraer_plan_gobierno(candidato_a.nombre)
    plan_b = extraer_plan_gobierno(candidato_b.nombre)
    plan_a = plan_a[:2000] if plan_a else "No disponible"
    plan_b = plan_b[:2000] if plan_b else "No disponible"

    nombre_a = candidato_a.nombre
    nombre_b = candidato_b.nombre
    apellido_a = get_apellido(nombre_a)
    apellido_b = get_apellido(nombre_b)
    partido_a = candidato_a.partido.nombre
    partido_b = candidato_b.partido.nombre

    prompt = (
        f"Eres un analista político peruano independiente y riguroso.\n"
        f"Compara estos dos candidatos para las elecciones 2026.\n\n"
        f"CANDIDATO A: {nombre_a} ({partido_a})\n"
        f"PLAN A:\n{plan_a}\n\n"
        f"CANDIDATO B: {nombre_b} ({partido_b})\n"
        f"PLAN B:\n{plan_b}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA:\n"
        f'1. "{nombre_a} propuestas plan gobierno 2026"\n'
        f'2. "{nombre_b} propuestas plan gobierno 2026"\n\n'
        f"REGLAS CRÍTICAS:\n"
        f'- NUNCA uses "Plan A", "Plan B", "Candidato A/B"\n'
        f'- USA nombres reales: "{nombre_a}" y "{nombre_b}"\n'
        f'- Apellidos cortos: "{apellido_a}" y "{apellido_b}"\n\n'
        f"IMPORTANTE: Responde ÚNICAMENTE con JSON válido.\n"
        f"Oraciones completas y naturales, no telegráficas.\n\n"
        f'{{\n'
        f'  "temas": {{\n'
        f'    "Economía": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 6, "ganador": "A",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Seguridad": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 6, "ganador": "A",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Educación": {{\n'
        f'      "puntaje_a": 6, "puntaje_b": 8, "ganador": "B",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Salud": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 7, "ganador": "empate",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Transporte": {{\n'
        f'      "puntaje_a": 5, "puntaje_b": 8, "ganador": "B",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Medio Ambiente": {{\n'
        f'      "puntaje_a": 8, "puntaje_b": 5, "ganador": "A",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }},\n'
        f'    "Corrupción": {{\n'
        f'      "puntaje_a": 4, "puntaje_b": 7, "ganador": "B",\n'
        f'      "resumen_a": "oración sobre {apellido_a}",\n'
        f'      "resumen_b": "oración sobre {apellido_b}"\n'
        f'    }}\n'
        f'  }},\n'
        f'  "ganador_general": "A",\n'
        f'  "puntaje_total_a": 51,\n'
        f'  "puntaje_total_b": 53,\n'
        f'  "resumen_ganador": "oración explicando el ganador",\n'
        f'  "nota_neutralidad": "Este análisis es informativo '
        f'y no constituye recomendación de voto"\n'
        f'}}\n\n'
        f"Reglas puntajes:\n"
        f"- Del 1 al 10 según concreción, viabilidad y coherencia\n"
        f"- Sin propuesta clara: máximo 4 puntos\n"
        f"- Ganador general: mayor suma de puntajes\n"
        f"- Diferencia menor a 3 puntos: empate"
    )

    def run_comparacion():
        ac = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        response = ac.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{"role": "user", "content": prompt}]
        )
        texto = ""
        for block in response.content:
            if hasattr(block, "text"):
                texto += block.text
        return texto

    try:
        texto = await asyncio.to_thread(run_comparacion)
        texto_limpio = texto.strip()
        if texto_limpio.startswith("```"):
            texto_limpio = texto_limpio.split("```")[1]
            if texto_limpio.startswith("json"):
                texto_limpio = texto_limpio[4:]
        resultado = json.loads(texto_limpio)
        await set_cache(db, "comparacion", clave, texto_limpio)
        return resultado
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {type(e).__name__}: {str(e)}")


@router.post("/analisis-tecnico/{candidato_a_id}/{candidato_b_id}")
async def analisis_tecnico_comparacion(
    candidato_a_id: int,
    candidato_b_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Análisis técnico completo — retorna JSON."""
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

    id_min = min(candidato_a_id, candidato_b_id)
    id_max = max(candidato_a_id, candidato_b_id)
    clave = f"{id_min}:{id_max}"

    cached = await get_cache(db, "analisis_tecnico", clave)
    if cached:
        print(f"CACHE HIT: analisis_tecnico:{clave}")
        return {"texto": cached}

    plan_a = extraer_plan_gobierno(candidato_a.nombre)
    plan_b = extraer_plan_gobierno(candidato_b.nombre)
    plan_a = plan_a[:3000] if plan_a else "No disponible"
    plan_b = plan_b[:3000] if plan_b else "No disponible"

    nombre_a = candidato_a.nombre
    nombre_b = candidato_b.nombre
    apellido_a = get_apellido(nombre_a)
    apellido_b = get_apellido(nombre_b)
    partido_a = candidato_a.partido.nombre
    partido_b = candidato_b.partido.nombre

    prompt = (
        f"IMPORTANTE: Responde DIRECTAMENTE con el análisis.\n"
        f"No escribas frases introductorias. Empieza con ## 💰\n\n"
        f"Eres un analista político peruano con experiencia en\n"
        f"ciencia política, economía pública y políticas sociales.\n"
        f"Compara a {nombre_a} ({partido_a}) y "
        f"{nombre_b} ({partido_b}).\n\n"
        f"PLAN DE {nombre_a}:\n{plan_a}\n\n"
        f"PLAN DE {nombre_b}:\n{plan_b}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA:\n"
        f'1. "Peru indicadores economicos 2024 2025 INEI MEF"\n'
        f'2. "Peru seguridad homicidios extorsion 2024"\n'
        f'3. "Peru educacion PISA ENLA 2024"\n'
        f'4. "Peru salud anemia ENDES 2024"\n'
        f'5. "{nombre_a} antecedentes judiciales"\n'
        f'6. "{nombre_b} antecedentes judiciales"\n\n'
        f"Escribe con prosa fluida y natural, como informe académico.\n"
        f"Usa datos reales: INEI, MEF, ENDES, MINEDU, BM, FMI.\n\n"
        f"## 💰 ECONOMÍA\n"
        f"Compara propuestas económicas. PBI, inflación, informalidad,\n"
        f"viabilidad fiscal, comparación internacional.\n\n"
        f"## 🔒 SEGURIDAD\n"
        f"Compara propuestas de seguridad. Datos homicidios/extorsión,\n"
        f"efectividad de enfoques similares en la región.\n\n"
        f"## 📚 EDUCACIÓN\n"
        f"Compara propuestas educativas. PISA/ENLA, gasto % PBI,\n"
        f"reformas exitosas en la región.\n\n"
        f"## 🏥 SALUD\n"
        f"Compara propuestas de salud. Anemia (ENDES), cobertura,\n"
        f"gasto per cápita.\n\n"
        f"## 🚆 TRANSPORTE\n"
        f"Compara infraestructura y transporte. Brecha vial (AFIN),\n"
        f"costo logístico % PBI.\n\n"
        f"## 🌿 MEDIO AMBIENTE\n"
        f"Compara propuestas ambientales. Deforestación (MINAM),\n"
        f"NDC Perú, comparación regional.\n\n"
        f"## ⚖️ CORRUPCIÓN E INTEGRIDAD\n"
        f"Compara anticorrupción y antecedentes. IPC 2024\n"
        f"(Transparencia Internacional), antecedentes verificados.\n\n"
        f"## 📊 CONCLUSIÓN TÉCNICA\n"
        f"Síntesis comparativa. Solidez técnica de cada plan.\n"
        f"Sin recomendar por quién votar.\n\n"
        f"- Nombres reales: {apellido_a} y {apellido_b}\n"
        f"- Directo y riguroso, sin eufemismos\n"
        f"- No omitas antecedentes negativos"
    )

    texto = await asyncio.to_thread(
        collect_claude, prompt, "claude-sonnet-4-20250514"
    )
    texto = limpiar_intro(texto)
    await set_cache(db, "analisis_tecnico", clave, texto)
    return {"texto": texto}
