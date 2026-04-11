"""
insert_tecnico_2.py — Inserta análisis técnico Fujimori (166) vs Belmont (169)
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert as pg_insert
from dotenv import load_dotenv

load_dotenv(".env.prod")
DATABASE_URL = os.getenv("DATABASE_URL")

CLAVE = "166:169"

TEXTO = """## 💰 ECONOMÍA

Fujimori y Belmont parten de diagnósticos similares sobre la informalidad y la necesidad de reactivar la economía, pero proponen instrumentos muy distintos. Fujimori defiende el modelo de libre mercado con disciplina fiscal, busca reducir el déficit al 1% del PBI, eliminar 500 trámites administrativos y atraer entre USD 5,000 y 7,000 millones de inversión privada adicional anual mediante una Ventanilla Única Digital con IA. Su apuesta sectorial se concentra en minería, agroexportación y servicios. Belmont propone una economía social de mercado con "rostro humano", rechazando explícitamente los monopolios y oligopolios. Su medida más concreta es el Plan Choque de Reactivación: culminar 1,500 obras sociales paralizadas, formalizar el 100% de trabajadores en obras estatales y crear 100 plantas de procesamiento regional. Belmont también plantea renegociar contratos de empresas estratégicas y cuestiona las concesiones de peajes. Técnicamente, el plan de Fujimori es más sofisticado en términos macroeconómicos, mientras que el de Belmont es más pragmático y focalizado en la ejecución de obras concretas, aunque carece de una estrategia fiscal integral.

## 🔒 SEGURIDAD

Fujimori apuesta por la mano dura tecnológica: videovigilancia, drones, reconocimiento facial, mega penales con trabajo productivo, un Consejo Presidencial de Prevención del Delito y la meta de reducir homicidios en 20% al 2031. Propone además el retiro de la Corte Interamericana de Derechos Humanos para reinstaurar jueces sin rostro, una medida muy cuestionada por organismos de derechos humanos. Belmont propone reestructurar integralmente el sistema de seguridad y justicia — PNP, Ministerio Público, INPE y Poder Judicial — con un enfoque en percepción ciudadana y eficiencia judicial: elevar en 15 puntos la percepción de seguridad vecinal y lograr que el 50% de denuncias sean resueltas. Su plan vincula la seguridad directamente con la ética pública, sosteniendo que el ejemplo de las autoridades es fundamental para erradicar la delincuencia. La propuesta de Belmont es menos tecnológica pero más sistémica en su enfoque institucional. Ninguno de los dos presenta evidencia comparada sobre la efectividad de sus enfoques en contextos similares al Perú.

## 📚 EDUCACIÓN

Fujimori propone cerrar brechas de infraestructura escolar, duplicar becas y créditos educativos, implementar inglés obligatorio con certificación básica al terminar secundaria y fortalecer la educación cívica. Su plan reconoce que el déficit de infraestructura educativa supera los S/158,800 millones. Belmont propone educación pública gratuita, de calidad y obligatoria, con la meta de reducir la deserción escolar en zonas rurales y marginales al 5% en cinco años, e incluir deporte, valores y folklore en el currículo. Su lema "Obras sí, palabras no" se refleja en su énfasis en infraestructura concreta: completar escuelas paralizadas antes de construir nuevas. Ambos coinciden en la necesidad de digitalizar el sistema educativo, aunque ninguno aborda la crisis de calidad docente ni propone reformas al sistema de evaluación. Según PISA 2025, Perú mantiene uno de los rendimientos más bajos de la región en comprensión lectora y matemáticas.

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20%, universalizar la vacunación, cerrar el déficit de camas hospitalarias e invertir en infraestructura médica con énfasis en tecnología. Belmont es más específico: elevar la cobertura de salud al 85% en cinco años, rehabilitar la mitad de los puestos de salud en zonas vulnerables, construir 50 nuevos establecimientos rurales y reducir la desnutrición infantil al 10%. Su experiencia como exalcalde de Lima le da mayor credibilidad en la gestión de servicios locales de salud. Ambos reconocen que el 50.5% de la población rural carece de acceso a servicios de salud según datos del MINSA. La diferencia es que Belmont presenta metas más específicas y territorialmente focalizadas, mientras Fujimori apuesta más por la tecnología y la infraestructura hospitalaria de mayor escala. Ninguno propone un modelo de financiamiento universal claro.

## 🚆 TRANSPORTE

Fujimori presenta el plan de transporte más ambicioso entre ambos: cuatro metros operativos en Lima, metros regionales en Arequipa, Trujillo y Piura, modernización de 17 aeropuertos concesionados, política de Cielos Abiertos y pavimentación del 100% de caminos rurales críticos. Belmont propone intervenir 10,000 kilómetros de caminos rurales, invertir en puertos, aeropuertos e hidroeléctricas bajo supervisión estricta, y cuestionar el modelo de concesiones de peajes que según él encarece los alimentos. Su enfoque es más crítico con el modelo concesionario actual. La brecha de infraestructura del Perú supera los USD 100,000 millones según AFIN 2024. Fujimori tiene propuestas de mayor escala pero requieren financiamiento significativo; las de Belmont son más modestas pero más ejecutables en el corto plazo.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley General de Minería con respeto ambiental y promover la convivencia entre minería y agricultura, sin compromisos climáticos específicos más allá de los NDC ya existentes. Belmont incluye una dimensión territorial-ambiental en su plan con énfasis en ordenamiento del territorio y desarrollo sostenible, y propone no vender más empresas estratégicas del Estado ni financiar armamento a costa de necesidades sociales básicas. Ninguno de los dos presenta una estrategia de transición energética ni aborda la deforestación amazónica de manera concreta. El Perú pierde aproximadamente 200,000 hectáreas de bosques al año según MINAM, una realidad que ninguno de los dos candidatos convierte en prioridad programática.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori propone un Shock Anticorrupción Digital con blockchain e IA para el 100% de contrataciones y obras. Sin embargo, sus tres procesos penales previos por lavado de activos vinculados al caso Odebrecht representan la mayor contradicción entre discurso y trayectoria. Belmont propone la imprescriptibilidad de los delitos de corrupción, una Plataforma Digital Única de Obras Públicas de acceso ciudadano con rendición de cuentas trimestral, y la revocatoria como mecanismo de control. Su historial personal es más limpio en términos de antecedentes legales, aunque su gestión como alcalde de Lima en los noventa tuvo cuestionamientos sobre la ejecución presupuestal. La credibilidad anticorrupción de Belmont es mayor que la de Fujimori en términos biográficos.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y Belmont representan dos versiones distintas del pragmatismo peruano: Fujimori desde la derecha institucionalizada con experiencia parlamentaria y electoral, Belmont desde el outsiderismo mediático con experiencia municipal. Fujimori tiene el plan más detallado técnicamente con metas macroeconómicas verificables y mayor cobertura de temas, pero su historial judicial es su principal lastre. Belmont tiene un plan más simple pero más enfocado en lo concreto — obras, servicios básicos, instituciones — con mayor credibilidad personal anticorrupción y un discurso más cercano a los sectores populares. La principal debilidad de Belmont es la ausencia de una estrategia económica integral y un equipo técnico de respaldo reconocido; la de Fujimori es la contradicción entre su propuesta anticorrupción y su historial. Ninguno de los dos tiene un plan ambiental serio ni una estrategia de salud universal financiada de manera realista."""


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
        print(f"✅ Análisis técnico {CLAVE} insertado: Fujimori vs Belmont")

    await engine.dispose()


asyncio.run(insertar())
