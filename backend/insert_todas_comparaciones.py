"""
insert_todas_comparaciones.py — Inserta las 55 comparaciones en DB de producción.
Ejecutar desde D:\\VoxIA\\backend

Candidatos:
  163 - César Acuña (APP)
  164 - Pablo Lopez Chau (Ahora Nación)
  165 - Luis Olivera (Frente Esperanza)
  166 - Keiko Fujimori (Fuerza Popular)
  167 - Jorge Nieto (Buen Gobierno)
  168 - Lopez Aliaga (Renovación Popular)
  169 - Ricardo Belmont (Obras)
  170 - José Luna Galvez (Podemos Perú)
  171 - Carlos Alvarez (País para Todos)
  172 - María Perez Tello (Primero la Gente)
  173 - Roberto Sanchez (Juntos por el Perú)
"""
import asyncio
import json
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert as pg_insert
from dotenv import load_dotenv

load_dotenv(".env.prod")
DATABASE_URL = os.getenv("DATABASE_URL")

# ── Perfiles base de cada candidato por tema (del 1 al 10) ───────────────────
# Basado en análisis de planes de gobierno oficiales JNE 2026

PERFILES = {
    163: {  # César Acuña - APP
        "nombre": "Acuña", "partido": "APP",
        "Economía": 7, "Seguridad": 7, "Educación": 7,
        "Salud": 6, "Transporte": 8, "Medio Ambiente": 5, "Corrupción": 4
    },
    164: {  # Pablo Lopez Chau - Ahora Nación
        "nombre": "López Chau", "partido": "Ahora Nación",
        "Economía": 8, "Seguridad": 7, "Educación": 8,
        "Salud": 7, "Transporte": 7, "Medio Ambiente": 6, "Corrupción": 7
    },
    165: {  # Luis Olivera - Frente Esperanza
        "nombre": "Olivera", "partido": "Frente Esperanza",
        "Economía": 6, "Seguridad": 6, "Educación": 6,
        "Salud": 6, "Transporte": 5, "Medio Ambiente": 5, "Corrupción": 7
    },
    166: {  # Keiko Fujimori - Fuerza Popular
        "nombre": "Fujimori", "partido": "Fuerza Popular",
        "Economía": 7, "Seguridad": 8, "Educación": 7,
        "Salud": 7, "Transporte": 8, "Medio Ambiente": 5, "Corrupción": 4
    },
    167: {  # Jorge Nieto - Buen Gobierno
        "nombre": "Nieto", "partido": "Buen Gobierno",
        "Economía": 7, "Seguridad": 6, "Educación": 7,
        "Salud": 7, "Transporte": 6, "Medio Ambiente": 7, "Corrupción": 7
    },
    168: {  # Lopez Aliaga - Renovación Popular
        "nombre": "López Aliaga", "partido": "Renovación Popular",
        "Economía": 7, "Seguridad": 8, "Educación": 6,
        "Salud": 6, "Transporte": 8, "Medio Ambiente": 5, "Corrupción": 7
    },
    169: {  # Ricardo Belmont - Obras
        "nombre": "Belmont", "partido": "Obras",
        "Economía": 5, "Seguridad": 6, "Educación": 6,
        "Salud": 6, "Transporte": 7, "Medio Ambiente": 5, "Corrupción": 6
    },
    170: {  # José Luna Galvez - Podemos Perú
        "nombre": "Luna Gálvez", "partido": "Podemos Perú",
        "Economía": 5, "Seguridad": 5, "Educación": 6,
        "Salud": 6, "Transporte": 5, "Medio Ambiente": 5, "Corrupción": 3
    },
    171: {  # Carlos Alvarez - País para Todos
        "nombre": "Álvarez", "partido": "País para Todos",
        "Economía": 5, "Seguridad": 5, "Educación": 5,
        "Salud": 5, "Transporte": 5, "Medio Ambiente": 5, "Corrupción": 5
    },
    172: {  # María Perez Tello - Primero la Gente
        "nombre": "Pérez Tello", "partido": "Primero la Gente",
        "Economía": 6, "Seguridad": 7, "Educación": 7,
        "Salud": 7, "Transporte": 6, "Medio Ambiente": 7, "Corrupción": 7
    },
    173: {  # Roberto Sanchez - Juntos por el Perú
        "nombre": "Sánchez", "partido": "Juntos por el Perú",
        "Economía": 6, "Seguridad": 6, "Educación": 7,
        "Salud": 7, "Transporte": 6, "Medio Ambiente": 8, "Corrupción": 6
    }
}

# ── Resúmenes por tema para cada candidato ────────────────────────────────────

RESUMENES = {
    163: {
        "Economía": "Acuña propone inversión minera de USD 6,000 millones, formalización de MYPES y un Ministerio de Infraestructura con portafolio de 72 proyectos por S/143 mil millones.",
        "Seguridad": "Acuña plantea crear el Comando Nacional contra la Extorsión y el Sicariato e incorporar 5,000 efectivos policiales con especialización en inteligencia.",
        "Educación": "Acuña propone reestructurar el MINEDU, incluir inglés e IA en el currículo, construir un COAR por región y el programa ILA de internet, luz y agua para escuelas públicas.",
        "Salud": "Acuña propone telemedicina con IA, infraestructura hospitalaria vía APP y cobertura de aseguramiento casi universal con 95% de abastecimiento de medicamentos.",
        "Transporte": "Acuña propone un portafolio de 72 proyectos de infraestructura con inversión de S/143 mil millones y entrega de maquinaria a las 196 provincias del país.",
        "Medio Ambiente": "Acuña menciona sostenibilidad pero prioriza la expansión minera y petrolera, lo que genera tensiones con la agenda ambiental.",
        "Corrupción": "Acuña propone IA y programas de integridad obligatorios, pero su historial de 132 investigaciones fiscales activas debilita su credibilidad anticorrupción."
    },
    164: {
        "Economía": "López Chau apuesta por la descentralización productiva con el lema 'Todo el poder a las regiones', impulsando exportaciones regionales y masificación del gas con tarifa única nacional.",
        "Seguridad": "López Chau propone derogar las leyes procrimen, purgar la Policía Nacional y modernizar comisarías con tecnología de inteligencia para desarticular bandas criminales.",
        "Educación": "López Chau plantea convertir las universidades en plataformas científicas, garantizar cobertura universal de inicial y desplegar mil agrónomos jóvenes con universidades públicas.",
        "Salud": "López Chau plantea integrar Minsa, EsSalud y gobiernos regionales en un sistema de cobertura universal efectiva con énfasis en acceso a agua potable y saneamiento.",
        "Transporte": "López Chau prioriza conectividad física y digital mediante una entidad autónoma meritocrática para obras públicas regionales y aceleración de proyectos Chavimochic, Chinecas y Majes Siguas 2.",
        "Medio Ambiente": "López Chau incluye una dimensión ambiental con énfasis en gestión de agua mediante cochas y reservorios, aunque sin compromisos climáticos específicos.",
        "Corrupción": "López Chau plantea plataforma digital de seguimiento de obras, impedir el acceso de investigados por corrupción a cargos públicos y fiscalización ciudadana activa."
    },
    165: {
        "Economía": "Olivera propone formalizar la economía con un millón de empleos formales al año, reducir el IGV progresivamente al 10% hacia 2031 e impulsar el turismo con nuevos aeropuertos regionales.",
        "Seguridad": "Olivera, cuyo símbolo es la escoba anticorrupción, propone reformas institucionales para eliminar la inmunidad de autoridades y mecanismos de transparencia en tiempo real.",
        "Educación": "Olivera propone eliminar la desnutrición crónica infantil en menores de 5 años como base para mejorar el rendimiento educativo, con enfoque en zonas rurales.",
        "Salud": "Olivera prioriza la eliminación de la desnutrición crónica infantil y el acceso a servicios básicos mediante programas sociales focalizados.",
        "Transporte": "Olivera plantea la construcción de nuevos aeropuertos internacionales en distintas regiones para impulsar el turismo y la conectividad territorial.",
        "Medio Ambiente": "Olivera incluye propuestas de sostenibilidad ambiental pero sin metas específicas verificables en su plan de gobierno.",
        "Corrupción": "Olivera tiene la lucha anticorrupción como bandera central de su candidatura, proponiendo eliminar la inmunidad de altas autoridades y referéndum para reformas institucionales."
    },
    166: {
        "Economía": "Fujimori defiende el modelo de libre mercado y la Constitución de 1993, busca reducir la informalidad laboral al 30% mediante reforma tributaria para Mypes y promueve el 'capitalismo popular'.",
        "Seguridad": "Fujimori propone mano dura con participación activa de las FFAA junto a la PNP, reforma del sistema de justicia y reducir la tasa de homicidios en 20% hacia 2031.",
        "Educación": "Fujimori propone cerrar brechas de infraestructura escolar, conectividad y servicios básicos en todos los colegios priorizados, duplicar becas y certificación de inglés al terminar secundaria.",
        "Salud": "Fujimori propone reducir la anemia infantil al 20% con cobertura universal de vacunación y reducir el déficit de camas hospitalarias con inversión en infraestructura.",
        "Transporte": "Fujimori propone poner operativos 4 metros en Lima, metros regionales en Arequipa, Trujillo y Piura, modernizar 17 aeropuertos y pavimentar el 100% de caminos rurales críticos.",
        "Medio Ambiente": "Fujimori propone modernizar la Ley General de Minería con respeto ambiental y convivencia armoniosa entre minería y agricultura, sin compromisos climáticos ambiciosos.",
        "Corrupción": "Fujimori propone un 'Shock Anticorrupción Digital' con blockchain e IA para contrataciones, pero sus tres procesos penales previos y caso Odebrecht generan dudas sobre su credibilidad."
    },
    167: {
        "Economía": "Nieto promueve la creación de un Fondo Soberano de Riqueza, crecimiento anual del 5%, presión tributaria del 18% y reducción de informalidad laboral al 50% con diversificación productiva.",
        "Seguridad": "Nieto plantea una política de seguridad ciudadana integral con enfoque en reforma institucional, coordinación entre fuerzas del orden y inversión en equipamiento policial.",
        "Educación": "Nieto propone universalizar la conectividad digital educativa, fortalecer la innovación, y reformar el currículo con énfasis en competencias para el siglo XXI.",
        "Salud": "Nieto propone universalizar la salud integrando los sistemas existentes, con especial atención a la reducción de la anemia y la mortalidad materna.",
        "Transporte": "Nieto propone fortalecer la inversión pública en infraestructura vial y logística, con énfasis en la descentralización y el cierre de brechas territoriales.",
        "Medio Ambiente": "Nieto incluye transición ecológica, economía circular y desarrollo industrial regional sostenible como ejes transversales de su plan.",
        "Corrupción": "Nieto propone reformas institucionales profundas y mecanismos de control ciudadano, con credibilidad respaldada por su trayectoria como ministro del gobierno Kuczynski."
    },
    168: {
        "Economía": "López Aliaga propone simplificar los regímenes tributarios a uno solo amigable para emprendedores, reducir el IGV, crear el Banco Pyme, y alcanzar un crecimiento del 7% del PBI con 2 millones de nuevos empleos.",
        "Seguridad": "López Aliaga propone la Central de Lucha contra la Corrupción con plenos poderes, penales de altura en zonas remotas sin señal, y el Comando Unificado 'Las Palmas' integrando inteligencia militar y policial.",
        "Educación": "López Aliaga propone incluir Libertad Financiera, Emprendimiento y Chino Mandarín en la educación secundaria, con enfoque en valores y trazabilidad blockchain en contrataciones educativas.",
        "Salud": "López Aliaga propone transformar EsSalud en entidad técnica autónoma con gestión meritocrática, medicamentos genéricos obligatorios en farmacias y dotar de personal a postas médicas.",
        "Transporte": "López Aliaga propone trenes de alta velocidad Lima-Ica y Lima-Trujillo, un túnel trasandino, y zonas francas para turismo e industria como palancas de conectividad nacional.",
        "Medio Ambiente": "López Aliaga propone el desarrollo de la industria del litio en Puno y zonas francas industriales, con mención secundaria a la sostenibilidad ambiental.",
        "Corrupción": "López Aliaga propone la Central de Lucha contra la Corrupción con poderes de infiltración, trazabilidad blockchain para obras públicas y eliminación del financiamiento estatal a partidos."
    },
    169: {
        "Economía": "Belmont propone disciplina fiscal, formalización laboral y empresarial, inversión en infraestructura, apoyo a MYPE e innovación, sin propuestas de alto impacto diferencial.",
        "Seguridad": "Belmont plantea reformas institucionales en seguridad con énfasis en obras de infraestructura urbana como elemento disuasivo de la delincuencia.",
        "Educación": "Belmont propone mejorar la infraestructura educativa y digitalizar el sistema, aprovechando su experiencia mediática para promover la educación ciudadana.",
        "Salud": "Belmont propone universalizar el acceso a la salud con énfasis en la atención primaria y reducción de brechas en zonas periurbanas.",
        "Transporte": "Belmont, ex alcalde de Lima, propone obras de infraestructura urbana y vial con experiencia en gestión municipal, aunque sin proyectos nacionales específicos.",
        "Medio Ambiente": "Belmont incluye sostenibilidad ambiental y transición energética en su plan, sin metas específicas verificables.",
        "Corrupción": "Belmont propone digitalización estatal y simplificación de trámites como mecanismos anticorrupción, con credibilidad media dado su historial político."
    },
    170: {
        "Economía": "Luna Gálvez propone reactivación económica mediante inversión pública y privada, con énfasis en el sector turístico y la formalización, aunque su plan carece de metas específicas.",
        "Seguridad": "Luna Gálvez presenta propuestas genéricas de seguridad sin diferenciación clara respecto a otros candidatos, debilitadas por sus antecedentes judiciales.",
        "Educación": "Luna Gálvez propone mejorar la calidad educativa y la conectividad digital, sin propuestas innovadoras que lo distingan del resto del campo.",
        "Salud": "Luna Gálvez propone ampliar la cobertura de salud y reducir la anemia, sin mecanismos de financiamiento claros ni metas verificables.",
        "Transporte": "Luna Gálvez propone inversión en infraestructura vial sin especificidades técnicas ni fuentes de financiamiento definidas.",
        "Medio Ambiente": "Luna Gálvez incluye propuestas ambientales genéricas sin compromisos medibles ni marcos de acción concretos.",
        "Corrupción": "Luna Gálvez enfrenta graves cuestionamientos por su vinculación a investigaciones fiscales por manipulación de organismos autónomos como la ONPE y el CNM, lo que debilita profundamente su propuesta anticorrupción."
    },
    171: {
        "Economía": "Álvarez propone reactivación económica y formalización sin propuestas económicas técnicas sólidas, compensadas parcialmente por su cercanía con sectores populares.",
        "Seguridad": "Álvarez propone medidas de seguridad ciudadana sin diferenciación técnica clara, apoyándose en su popularidad mediática para comunicar el mensaje.",
        "Educación": "Álvarez propone acceso universal a la educación con énfasis en los más vulnerables, sin reformas estructurales al sistema.",
        "Salud": "Álvarez propone ampliar coberturas de salud y reducir la anemia con programas sociales, sin reformas sistémicas al sector.",
        "Transporte": "Álvarez propone obras de infraestructura básica sin proyectos de gran escala diferenciados de los demás candidatos.",
        "Medio Ambiente": "Álvarez incluye propuestas de sostenibilidad ambiental en su plan, con énfasis en acceso a agua potable para zonas rurales.",
        "Corrupción": "Álvarez propone transparencia en la gestión pública y rendición de cuentas, aunque su plan carece de mecanismos institucionales robustos contra la corrupción."
    },
    172: {
        "Economía": "Pérez Tello propone digitalización radical del Estado, simplificación de trámites, formalización empresarial y promoción de la inversión privada con énfasis en sostenibilidad.",
        "Seguridad": "Pérez Tello propone derogar leyes procrimen, modernización policial con tecnología predictiva y recuperación del control territorial con enfoque preventivo.",
        "Educación": "Pérez Tello propone universalizar la educación inicial, mejorar la calidad docente, digitalizar escuelas y promover la educación intercultural en zonas rurales.",
        "Salud": "Pérez Tello propone integrar los sistemas de salud con énfasis en la atención primaria, reducción de la anemia y acceso universal a medicamentos esenciales.",
        "Transporte": "Pérez Tello propone infraestructura de conectividad con enfoque territorial para cerrar brechas regionales, priorizando comunidades rurales y periurbanas.",
        "Medio Ambiente": "Pérez Tello incluye una dimensión ambiental sólida con énfasis en economía verde, gestión de recursos hídricos y reducción de emisiones como parte de su visión de desarrollo.",
        "Corrupción": "Pérez Tello propone digitalización estatal para transparencia, control ciudadano activo y reforma del sistema de justicia, con credibilidad respaldada por su trayectoria ministerial."
    },
    173: {
        "Economía": "Sánchez propone reformar el sistema tributario, incrementar la presión fiscal, invertir en sectores estratégicos y promover la economía social de mercado con énfasis en reducir la desigualdad.",
        "Seguridad": "Sánchez propone reformas estructurales en seguridad con énfasis en prevención, reinserción social y ataque a las economías ilegales que financian el crimen organizado.",
        "Educación": "Sánchez propone universalizar la educación pública de calidad, aumentar el gasto educativo al 6% del PBI y fortalecer las universidades públicas como motores de innovación regional.",
        "Salud": "Sánchez propone universalizar el sistema de salud con un modelo integrado, aumentar el gasto en salud e invertir en prevención y atención primaria.",
        "Transporte": "Sánchez propone completar proyectos de infraestructura vial y logística priorizando la conectividad de zonas rurales y la integración de mercados regionales.",
        "Medio Ambiente": "Sánchez tiene el plan ambiental más ambicioso del grupo, con propuestas de transición energética, economía circular, reducción de la deforestación y compromisos climáticos concretos.",
        "Corrupción": "Sánchez propone reformas anticorrupción institucionales con énfasis en transparencia y rendición de cuentas, aunque su asociación con el gobierno Castillo genera cuestionamientos sobre su credibilidad."
    }
}

# ── Generar comparación entre dos candidatos ──────────────────────────────────

def generar_comparacion(id_a: int, id_b: int) -> dict:
    perfil_a = PERFILES[id_a]
    perfil_b = PERFILES[id_b]
    resumenes_a = RESUMENES[id_a]
    resumenes_b = RESUMENES[id_b]

    temas = ["Economía", "Seguridad", "Educación", "Salud", "Transporte", "Medio Ambiente", "Corrupción"]

    resultado_temas = {}
    total_a = 0
    total_b = 0

    for tema in temas:
        pa = perfil_a[tema]
        pb = perfil_b[tema]
        total_a += pa
        total_b += pb

        diff = pa - pb
        if diff > 1:
            ganador = "A"
        elif diff < -1:
            ganador = "B"
        else:
            ganador = "empate"

        resultado_temas[tema] = {
            "puntaje_a": pa,
            "puntaje_b": pb,
            "ganador": ganador,
            "resumen_a": resumenes_a[tema],
            "resumen_b": resumenes_b[tema]
        }

    diff_total = total_a - total_b
    if diff_total > 2:
        ganador_general = "A"
        ganador_nombre = perfil_a["nombre"]
    elif diff_total < -2:
        ganador_general = "B"
        ganador_nombre = perfil_b["nombre"]
    else:
        ganador_general = "empate"
        ganador_nombre = None

    if ganador_general == "A":
        resumen = f"{perfil_a['nombre']} obtiene ventaja con {total_a} puntos frente a {total_b} de {perfil_b['nombre']}, destacando en {', '.join([t for t in temas if resultado_temas[t]['ganador'] == 'A'][:2])}."
    elif ganador_general == "B":
        resumen = f"{perfil_b['nombre']} obtiene ventaja con {total_b} puntos frente a {total_a} de {perfil_a['nombre']}, destacando en {', '.join([t for t in temas if resultado_temas[t]['ganador'] == 'B'][:2])}."
    else:
        resumen = f"Los planes de {perfil_a['nombre']} ({total_a} pts) y {perfil_b['nombre']} ({total_b} pts) presentan propuestas similares en la mayoría de los temas evaluados."

    return {
        "temas": resultado_temas,
        "ganador_general": ganador_general,
        "puntaje_total_a": total_a,
        "puntaje_total_b": total_b,
        "resumen_ganador": resumen,
        "nota_neutralidad": "Este análisis es informativo y no constituye recomendación de voto"
    }


# ── Insertar en DB ─────────────────────────────────────────────────────────────

async def insertar_todo():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    ids = sorted(PERFILES.keys())
    comparaciones = []

    # Generar todas las combinaciones únicas
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            id_a = ids[i]
            id_b = ids[j]
            comparaciones.append((id_a, id_b))

    print(f"Total comparaciones a insertar: {len(comparaciones)}")

    insertadas = 0
    errores = 0

    async with async_session() as db:
        for id_a, id_b in comparaciones:
            clave = f"{id_a}:{id_b}"
            try:
                comparacion = generar_comparacion(id_a, id_b)
                contenido = json.dumps(comparacion, ensure_ascii=False)

                stmt = pg_insert(CacheAnalisis).values(
                    tipo="comparacion",
                    clave=clave,
                    contenido=contenido
                ).on_conflict_do_update(
                    index_elements=["tipo", "clave"],
                    set_={"contenido": contenido}
                )
                await db.execute(stmt)
                nombre_a = PERFILES[id_a]["nombre"]
                nombre_b = PERFILES[id_b]["nombre"]
                print(f"  ✅ {clave}: {nombre_a} vs {nombre_b}")
                insertadas += 1
            except Exception as e:
                print(f"  ❌ {clave}: ERROR — {e}")
                errores += 1

        await db.commit()

    await engine.dispose()
    print(f"\n✅ Insertadas: {insertadas}")
    print(f"❌ Errores:    {errores}")
    print("🎉 ¡Listo! Todas las comparaciones en producción.")


asyncio.run(insertar_todo())
