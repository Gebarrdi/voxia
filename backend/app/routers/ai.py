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


def get_apellido(nombre: str) -> str:
    """Retorna primer nombre + primer apellido."""
    partes = nombre.split()
    if len(partes) >= 3:
        return f"{partes[0]} {partes[2]}"
    elif len(partes) == 2:
        return f"{partes[0]} {partes[1]}"
    return partes[0]


async def stream_claude(
    prompt: str,
    model: str = "claude-haiku-4-5-20251001"
):
    ac = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    with ac.messages.stream(
        model=model,
        max_tokens=6000,
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
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )

    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = (
        f"IMPORTANTE: Responde DIRECTAMENTE con el análisis.\n"
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
        f'4. "{candidato.nombre} antecedentes judiciales penales fiscalía"\n'
        f'5. "{candidato.nombre} investigación corrupción sentencias"\n'
        f'6. "{candidato.nombre} logros obras resultados cargo público"\n'
        f'7. "{candidato.nombre} IDL OjoPúblico Hildebrandt Caretas"\n\n'
        f"FORMATO DE RESPUESTA — usa exactamente esta estructura:\n\n"
        f"## 👤 PERFIL ACADÉMICO Y PROFESIONAL\n"
        f"- Estudios universitarios y postgrados (con institución y año)\n"
        f"- Trayectoria laboral (empresas, cargos, fechas)\n"
        f"- Si fue/es congresista: desde cuándo, proyectos presentados\n"
        f"  y aprobados, asistencia, comisiones\n"
        f"- Cargos públicos previos y resultados de su gestión\n\n"
        f"## 📋 PROPUESTAS CLAVE DEL PLAN DE GOBIERNO\n"
        f"Lista las 6-7 propuestas más importantes extraídas\n"
        f"directamente del plan oficial. SOLO LISTARLAS, no evaluarlas.\n"
        f"Usa el formato:\n"
        f"- [Eje temático]: descripción concreta de la propuesta\n\n"
        f"## ✅ ASPECTOS POSITIVOS DEL CANDIDATO\n"
        f"3-4 aspectos positivos de la PERSONA (no del plan):\n"
        f"experiencia, logros verificables, trayectoria, reconocimientos.\n"
        f"Cada punto debe citar fuente o dato concreto.\n\n"
        f"## ⚠️ ASPECTOS NEGATIVOS Y RIESGOS DEL CANDIDATO\n"
        f"3-4 aspectos negativos de la PERSONA:\n"
        f"antecedentes judiciales, cuestionamientos éticos, fracasos\n"
        f"de gestión, inconsistencias. Cita fuente específica.\n"
        f"No omitas información negativa relevante.\n\n"
        f"## 🔍 INVESTIGACIONES PERIODÍSTICAS\n"
        f"Investigaciones verificadas de IDL-Reporteros, OjoPúblico,\n"
        f"Caretas, La República, El Comercio, Hildebrandt, Beto a Saber.\n"
        f"Incluye medio, año y hallazgo específico.\n\n"
        f"## 📊 CONCLUSIÓN NEUTRAL\n"
        f"Párrafo balanceado sobre el candidato como persona y político.\n"
        f"Sin evaluar el plan. Sin recomendar por quién votar.\n\n"
        f"IMPORTANTE:\n"
        f"- Analiza al CANDIDATO, no al plan de gobierno\n"
        f"- Las propuestas solo se listan, no se evalúan aquí\n"
        f"- Sé directo y sin eufemismos\n"
        f"- Cita fuentes específicas\n"
        f"- No omitas antecedentes negativos relevantes\n"
        f"- No recomiendas por quién votar"
    )

    return StreamingResponse(
        stream_claude(prompt, model="claude-haiku-4-5-20251001"),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
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
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )

    plan_gobierno = extraer_plan_gobierno(candidato.nombre)

    prompt = (
        f"IMPORTANTE: Responde DIRECTAMENTE con el análisis.\n"
        f"No escribas frases como 'Necesito buscar', 'Permíteme',\n"
        f"'Ahora procederé', 'Entendido' o similares.\n"
        f"Empieza directo con ## 1. [NOMBRE DE LA PROPUESTA]\n\n"
        f"Eres un economista y analista de políticas públicas peruano,\n"
        f"Eres un economista y analista de políticas públicas peruano,\n"
        f"especializado en finanzas públicas y evaluación de programas.\n"
        f"Analiza la VIABILIDAD ESPECÍFICA de cada propuesta del plan\n"
        f"de gobierno de {candidato.nombre} "
        f"({candidato.partido.nombre}).\n\n"
        f"PLAN DE GOBIERNO OFICIAL (fuente: JNE):\n"
        f"{plan_gobierno}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA — ejecuta estas búsquedas:\n"
        f'1. "Peru presupuesto fiscal 2026 MEF déficit"\n'
        f'2. "Peru PBI crecimiento inflación informalidad 2025 2026"\n'
        f"3. Para cada propuesta identificada, busca experiencias\n"
        f"   internacionales específicas y su costo estimado\n\n"
        f"TAREA: Identifica las 5-7 propuestas más importantes del\n"
        f"plan y analiza CADA UNA con este formato exacto:\n\n"
        f"## [NÚMERO]. [NOMBRE DE LA PROPUESTA]\n\n"
        f"**Qué propone:** descripción clara en 2-3 líneas de\n"
        f"exactamente qué plantea el candidato.\n\n"
        f"**Costo estimado:** cuánto costaría implementarlo,\n"
        f"con referencia a presupuesto actual del Perú.\n\n"
        f"**Precedentes internacionales:** 1-2 países que\n"
        f"implementaron algo similar, con resultados reales\n"
        f"y concretos (no genéricos).\n\n"
        f"**Restricciones:** obstáculos específicos en el contexto\n"
        f"peruano — fiscal, institucional, técnico o político.\n\n"
        f"**Veredicto:** Alta / Media / Baja viabilidad — con\n"
        f"justificación en 1-2 líneas directas y sin rodeos.\n\n"
        f"---\n\n"
        f"Al final, después de analizar todas las propuestas:\n\n"
        f"## 📊 VEREDICTO GLOBAL DEL PLAN\n"
        f"Coherencia fiscal general del plan. ¿Las propuestas\n"
        f"son consistentes entre sí? ¿Hay contradicciones?\n"
        f"¿El financiamiento es realista dado el contexto del\n"
        f"Perú (déficit fiscal, regla fiscal, presupuesto 2026)?\n\n"
        f"REGLAS:\n"
        f"- Sé directo y sin eufemismos\n"
        f"- Usa datos reales y actualizados del Perú\n"
        f"- Cita fuentes: MEF, INEI, BM, FMI, CEPAL\n"
        f"- No repitas lo que ya está en el plan, analiza\n"
        f"- Si una propuesta es inviable, dilo claramente"
    )

    return StreamingResponse(
        stream_claude(prompt, model="claude-sonnet-4-20250514"),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )


@router.post("/comparar/{candidato_a_id}/{candidato_b_id}")
async def comparar_candidatos(
    candidato_a_id: int,
    candidato_b_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Llamada 1: Solo puntajes y resúmenes breves en JSON."""
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
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )

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

    ac = anthropic.Anthropic(api_key=settings.anthropic_api_key)

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
        f"Los resúmenes deben ser oraciones completas y naturales,\n"
        f"no telegráficas. Usa artículos y conectores correctamente.\n\n"
        f'{{\n'
        f'  "temas": {{\n'
        f'    "Economía": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 6, "ganador": "A",\n'
        f'      "resumen_a": "oración completa sobre propuesta '
        f'económica de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre propuesta '
        f'económica de {apellido_b}"\n'
        f'    }},\n'
        f'    "Seguridad": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 6, "ganador": "A",\n'
        f'      "resumen_a": "oración completa sobre seguridad '
        f'de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre seguridad '
        f'de {apellido_b}"\n'
        f'    }},\n'
        f'    "Educación": {{\n'
        f'      "puntaje_a": 6, "puntaje_b": 8, "ganador": "B",\n'
        f'      "resumen_a": "oración completa sobre educación '
        f'de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre educación '
        f'de {apellido_b}"\n'
        f'    }},\n'
        f'    "Salud": {{\n'
        f'      "puntaje_a": 7, "puntaje_b": 7, "ganador": "empate",\n'
        f'      "resumen_a": "oración completa sobre salud '
        f'de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre salud '
        f'de {apellido_b}"\n'
        f'    }},\n'
        f'    "Transporte": {{\n'
        f'      "puntaje_a": 5, "puntaje_b": 8, "ganador": "B",\n'
        f'      "resumen_a": "oración completa sobre transporte '
        f'de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre transporte '
        f'de {apellido_b}"\n'
        f'    }},\n'
        f'    "Medio Ambiente": {{\n'
        f'      "puntaje_a": 8, "puntaje_b": 5, "ganador": "A",\n'
        f'      "resumen_a": "oración completa sobre medio ambiente '
        f'de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre medio ambiente '
        f'de {apellido_b}"\n'
        f'    }},\n'
        f'    "Corrupción": {{\n'
        f'      "puntaje_a": 4, "puntaje_b": 7, "ganador": "B",\n'
        f'      "resumen_a": "oración completa sobre antecedentes '
        f'y postura de {apellido_a}",\n'
        f'      "resumen_b": "oración completa sobre antecedentes '
        f'y postura de {apellido_b}"\n'
        f'    }}\n'
        f'  }},\n'
        f'  "ganador_general": "A",\n'
        f'  "puntaje_total_a": 51,\n'
        f'  "puntaje_total_b": 53,\n'
        f'  "resumen_ganador": "oración explicando por qué gana '
        f'el candidato con mayor puntaje",\n'
        f'  "nota_neutralidad": "Este análisis es informativo '
        f'y no constituye recomendación de voto"\n'
        f'}}\n\n'
        f"Reglas puntajes:\n"
        f"- Del 1 al 10 según concreción, viabilidad y coherencia\n"
        f"- Sin propuesta clara: máximo 4 puntos\n"
        f"- Ganador general: mayor suma de puntajes\n"
        f"- Diferencia menor a 3 puntos: empate"
    )

    try:
        response = ac.messages.create(
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

        texto_limpio = texto.strip()
        if texto_limpio.startswith("```"):
            texto_limpio = texto_limpio.split("```")[1]
            if texto_limpio.startswith("json"):
                texto_limpio = texto_limpio[4:]
        resultado = json.loads(texto_limpio)
        return resultado

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error: {type(e).__name__}: {str(e)}"
        )


@router.post("/analisis-tecnico/{candidato_a_id}/{candidato_b_id}")
async def analisis_tecnico_comparacion(
    candidato_a_id: int,
    candidato_b_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Llamada 2: Análisis técnico completo en streaming."""
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
        raise HTTPException(
            status_code=404,
            detail="Candidato no encontrado"
        )

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
        f"No escribas frases como 'Entendido', 'Voy a realizar',\n"
        f"'Permíteme buscar' o similares.\n"
        f"Empieza directo con ## 👤 PERFIL ACADÉMICO Y PROFESIONAL\n\n"
        f"Eres un analista político peruano independiente y riguroso.\n"
        f"Eres un analista político peruano con experiencia en ciencia "
        f"política, economía pública y políticas sociales comparadas.\n"
        f"Redacta un análisis técnico riguroso comparando a "
        f"{nombre_a} ({partido_a}) y {nombre_b} ({partido_b}) "
        f"para las elecciones peruanas del 12 de abril de 2026.\n\n"
        f"PLAN DE GOBIERNO DE {nombre_a}:\n{plan_a}\n\n"
        f"PLAN DE GOBIERNO DE {nombre_b}:\n{plan_b}\n\n"
        f"INSTRUCCIONES DE BÚSQUEDA:\n"
        f'1. "Peru indicadores economicos 2024 2025 INEI MEF"\n'
        f'2. "Peru seguridad ciudadana homicidios 2024 INEI"\n'
        f'3. "Peru educacion PISA ENLA resultados 2024"\n'
        f'4. "Peru salud anemia infantil ENDES 2024"\n'
        f'5. "{nombre_a} antecedentes judiciales corrupción"\n'
        f'6. "{nombre_b} antecedentes judiciales corrupción"\n\n'
        f"Escribe el análisis con prosa fluida y natural, "
        f"como lo haría un politólogo o economista en un informe "
        f"académico. Usa artículos, conectores y oraciones completas.\n"
        f"Incluye datos estadísticos reales del Perú cuando sea "
        f"posible (INEI, MEF, ENDES, MINEDU, Transparencia "
        f"Internacional, BM, FMI, CEPAL).\n\n"
        f"ESTRUCTURA DEL ANÁLISIS:\n\n"
        f"## 💰 ECONOMÍA\n"
        f"Analiza y compara las propuestas económicas de ambos "
        f"candidatos. Incluye contexto macroeconómico del Perú "
        f"(PBI, inflación, informalidad), viabilidad fiscal de "
        f"las propuestas y comparación con experiencias "
        f"internacionales similares.\n\n"
        f"## 🔒 SEGURIDAD\n"
        f"Analiza y compara las propuestas de seguridad ciudadana. "
        f"Incluye datos de homicidios, extorsión y crimen organizado "
        f"en el Perú, y evalúa la efectividad de enfoques similares "
        f"en otros países de la región.\n\n"
        f"## 📚 EDUCACIÓN\n"
        f"Analiza y compara las propuestas educativas. Incluye "
        f"resultados PISA/ENLA del Perú, gasto educativo como "
        f"porcentaje del PBI y reformas exitosas en la región.\n\n"
        f"## 🏥 SALUD\n"
        f"Analiza y compara las propuestas de salud. Incluye "
        f"datos de anemia infantil (ENDES), cobertura del sistema "
        f"de salud y gasto per cápita en salud.\n\n"
        f"## 🚆 TRANSPORTE\n"
        f"Analiza y compara las propuestas de infraestructura "
        f"y transporte. Incluye la brecha de infraestructura "
        f"vial del Perú (AFIN) y costo logístico como % del PBI.\n\n"
        f"## 🌿 MEDIO AMBIENTE\n"
        f"Analiza y compara las propuestas ambientales. Incluye "
        f"datos de deforestación en la Amazonía peruana (MINAM), "
        f"compromisos NDC del Perú y comparación con políticas "
        f"ambientales exitosas en la región.\n\n"
        f"## ⚖️ CORRUPCIÓN E INTEGRIDAD\n"
        f"Analiza y compara las propuestas anticorrupción y los "
        f"antecedentes de cada candidato. Incluye el Índice de "
        f"Percepción de Corrupción del Perú (Transparencia "
        f"Internacional 2024) y antecedentes judiciales verificados.\n\n"
        f"## 📊 CONCLUSIÓN TÉCNICA\n"
        f"Síntesis comparativa final para un lector especializado. "
        f"Evalúa la solidez técnica de cada plan, la experiencia "
        f"de los candidatos y el contexto político-institucional "
        f"del Perú. No recomiendas por quién votar.\n\n"
        f"IMPORTANTE:\n"
        f"- Usa siempre los nombres reales: {apellido_a} y {apellido_b}\n"
        f"- Sé directo, riguroso y sin eufemismos\n"
        f"- No omitas antecedentes negativos relevantes\n"
        f"- No recomiendas por quién votar"
    )

    return StreamingResponse(
        stream_claude(prompt, model="claude-sonnet-4-20250514"),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )
