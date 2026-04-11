"""
insert_tecnico_1.py — Inserta análisis técnico Fujimori (166) vs López Aliaga (168)
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert as pg_insert
from dotenv import load_dotenv

load_dotenv(".env.prod")
DATABASE_URL = os.getenv("DATABASE_URL")

# IDs en producción: Fujimori=166, López Aliaga=168
# Clave siempre ordenada: menor:mayor
CLAVE = "166:168"

TEXTO = """## 💰 ECONOMÍA

Ambos candidatos defienden el modelo de libre mercado y la Constitución de 1993, pero con énfasis distintos. Fujimori prioriza la disciplina fiscal con meta de reducir el déficit al 1% del PBI, eliminar 500 trámites administrativos y digitalizar el 80% de procedimientos empresariales mediante una Ventanilla Única con IA, buscando atraer entre USD 5,000 y 7,000 millones adicionales de inversión privada anual. López Aliaga apuesta por una reforma tributaria más agresiva: unificar todos los regímenes tributarios en uno solo amigable para emprendedores, reducir el IGV, crear el Banco Pyme y generar 2 millones de empleos mediante industrialización y zonas francas. Ambos defienden la minería y la inversión privada como motores del crecimiento, aunque López Aliaga propone metas más ambiciosas de crecimiento (7% del PBI anual) sin especificar su fuente de financiamiento. Técnicamente, el plan de Fujimori es más conservador pero más realista en el contexto fiscal peruano actual, donde el déficit fiscal bordea el 4.3% del PBI según el MEF.

## 🔒 SEGURIDAD

Es el tema donde más coinciden en el enfoque — ambos proponen mano dura — pero difieren en los instrumentos. Fujimori plantea un Consejo Presidencial de Prevención del Delito, modernización policial con videovigilancia, drones y reconocimiento facial, mega penales con trabajo productivo penitenciario, y la meta de reducir la tasa de homicidios en 20% hacia 2031. Propone además el retiro de la Corte Interamericana de Derechos Humanos para reinstaurar los jueces sin rostro. López Aliaga va más lejos institucionalmente: propone la Central de Lucha contra la Corrupción con poderes plenos de infiltración, penales de alta montaña sin cobertura móvil en la Cordillera de la Viuda, el Comando Unificado 'Las Palmas' integrando inteligencia militar y policial, y un convenio con Estados Unidos para tecnología y extradición de cabecillas. Ambos enfoques son cuestionados por expertos en seguridad por su sesgo punitivo y escasa atención a la prevención social, aunque López Aliaga presenta propuestas más detalladas e innovadoras institucionalmente.

## 📚 EDUCACIÓN

Fujimori propone infraestructura educativa masiva — construcción y remodelación de colegios —, implementación de clases de inglés obligatorias con certificación básica al terminar secundaria, educación cívica y valores patrióticos, y duplicar la cobertura de becas y créditos educativos. López Aliaga plantea incluir Libertad Financiera, Emprendimiento y Chino Mandarín en secundaria, invertir en internet satelital y tablets para todas las escuelas, y crear parques tecnológicos que atraigan empresas globales. Ambos priorizan la conectividad digital, aunque Fujimori tiene un enfoque más convencional centrado en infraestructura física, mientras López Aliaga apuesta por una transformación curricular más disruptiva. Ninguno propone reformas de fondo al sistema de evaluación docente ni aborda el problema del bajo rendimiento en PISA (Perú ocupa el puesto 64 de 81 países en la última edición).

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20% con cobertura universal de vacunación y chequeos preventivos, cerrar el déficit de camas hospitalarias e invertir en infraestructura médica. Su plan reconoce que el Perú es uno de los países con menor inversión en salud pública de la región. López Aliaga plantea transformar EsSalud en una entidad técnica autónoma con gestión meritocrática sin injerencia política, medicamentos genéricos obligatorios en farmacias y dotación de personal médico en postas rurales. Ambos carecen de propuestas de financiamiento claras para universalizar la salud. La anemia infantil afecta al 43.1% de niños menores de 3 años según ENDES 2024, y ninguno presenta un plan integral que combine nutrición, agua potable y atención primaria de manera articulada.

## 🚆 TRANSPORTE

López Aliaga presenta las propuestas más ambiciosas en este eje: trenes de alta velocidad Lima-Ica y Lima-Trujillo, un túnel trasandino, zonas francas para turismo e industria, y desarrollo de la industria del litio en Puno. Fujimori propone poner operativos cuatro metros en Lima, metros regionales en Arequipa, Trujillo y Piura, modernizar 17 aeropuertos concesionados, política de Cielos Abiertos y pavimentar el 100% de caminos rurales críticos. La brecha de infraestructura del Perú supera los USD 100,000 millones según AFIN 2024. Las propuestas de López Aliaga son más innovadoras pero su viabilidad fiscal es cuestionable. Las de Fujimori son más convencionales pero más alineadas con proyectos ya en cartera.

## 🌿 MEDIO AMBIENTE

Este es el eje más débil de ambos candidatos. Fujimori propone modernizar la Ley General de Minería con respeto ambiental y promover la convivencia entre minería y agricultura, sin metas de reducción de emisiones ni compromisos climáticos específicos. López Aliaga prioriza el desarrollo de la industria del litio en Puno y la creación de zonas francas industriales, con menciones secundarias a la sostenibilidad. Ninguno aborda la deforestación amazónica — que alcanza las 200,000 hectáreas anuales según MINAM — ni presenta una estrategia clara de transición energética. El Perú tiene compromisos NDC que requieren reducir emisiones en 30% al 2030, objetivo que ninguno de los dos planes hace suyo explícitamente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Este es el eje donde ambos candidatos enfrentan mayores cuestionamientos personales. Fujimori propone un 'Shock Anticorrupción Digital' con blockchain e IA para el 100% de contrataciones y obras del Estado. Sin embargo, enfrenta tres procesos penales previos por lavado de activos vinculados al caso Odebrecht, lo que genera una contradicción fundamental entre su propuesta y su historial. López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, trazabilidad blockchain para obras públicas, eliminación del financiamiento estatal a partidos y prohibición del transfuguismo. Su credibilidad anticorrupción es mayor en términos de historial personal, aunque Renovación Popular recibió aportes de constructoras brasileñas según reportes periodísticos, y enfrenta cuestionamientos por presunta deuda tributaria con la SUNAT.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y López Aliaga representan las dos expresiones más consolidadas de la derecha peruana en 2026, con visiones similares sobre el modelo económico pero diferencias importantes en estilo y profundidad. Fujimori presenta un plan más ordenado técnicamente con metas verificables y enfoque institucionalista, pero su historial judicial es su mayor lastre. López Aliaga ofrece propuestas más disruptivas e innovadoras — especialmente en transporte, seguridad y tributación — con mayor credibilidad anticorrupción personal, pero algunas metas fiscales son cuestionablemente ambiciosas. Ambos coinciden en mano dura contra el crimen, defensa del libre mercado y rechazo a la izquierda. La diferencia principal radica en que Fujimori apuesta por la continuidad institucional mejorada, mientras López Aliaga propone una ruptura más radical con el statu quo. Ninguno presenta una estrategia ambiental seria ni un plan integral de salud universal financiado."""


async def insertar():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as db:
        stmt = pg_insert(CacheAnalisis).values(
            tipo="analisis_tecnico",
            clave=CLAVE,
            contenido=TEXTO
        ).on_conflict_do_update(
            index_elements=["tipo", "clave"],
            set_={"contenido": TEXTO}
        )
        await db.execute(stmt)
        await db.commit()
        print(f"✅ Análisis técnico {CLAVE} insertado: Fujimori vs López Aliaga")

    await engine.dispose()


asyncio.run(insertar())
