"""
insert_tecnicos_26_55.py — Análisis técnicos grupo 3 y 4 (30 comparaciones)
============================================================================
  #26  165:169  Olivera vs Belmont
  #27  165:170  Olivera vs Luna Gálvez
  #28  165:171  Olivera vs Álvarez
  #29  165:172  Olivera vs Pérez Tello
  #30  165:173  Olivera vs Sánchez
  #31  166:170  Fujimori vs Luna Gálvez
  #32  166:171  Fujimori vs Álvarez
  #33  166:172  Fujimori vs Pérez Tello
  #34  167:168  Nieto vs López Aliaga
  #35  167:169  Nieto vs Belmont
  #36  167:170  Nieto vs Luna Gálvez
  #37  167:171  Nieto vs Álvarez
  #38  167:172  Nieto vs Pérez Tello
  #39  167:173  Nieto vs Sánchez
  #40  168:170  López Aliaga vs Luna Gálvez
  #41  168:171  López Aliaga vs Álvarez
  #42  168:172  López Aliaga vs Pérez Tello
  #43  169:170  Belmont vs Luna Gálvez
  #44  169:171  Belmont vs Álvarez
  #45  169:172  Belmont vs Pérez Tello
  #46  169:173  Belmont vs Sánchez
  #47  170:171  Luna Gálvez vs Álvarez
  #48  170:172  Luna Gálvez vs Pérez Tello
  #49  170:173  Luna Gálvez vs Sánchez
  #50  171:172  Álvarez vs Pérez Tello
  #51  171:173  Álvarez vs Sánchez
  #52  172:173  Pérez Tello vs Sánchez
  #53  163:164  Acuña vs López Chau  (ya insertada antes, se actualiza)
  #54  163:165  Acuña vs Olivera
  #55  164:165  López Chau vs Olivera
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert as pg_insert
from dotenv import load_dotenv

load_dotenv(".env.prod")
DATABASE_URL = os.getenv("DATABASE_URL")

ANALISIS = {

"165:169": """## 💰 ECONOMÍA

Olivera propone formalizar la economía con reducción progresiva del IGV al 10% hacia 2031 y nuevos aeropuertos regionales para el turismo. Belmont propone economía social de mercado, Plan Choque de 1,500 obras paralizadas y renegociación de contratos estratégicos. Ambos tienen propuestas más modestas que los candidatos principales, pero con enfoques distintos: Olivera prioriza la reducción tributaria como motor de formalización, Belmont prioriza la reactivación de obras concretas.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales para eliminar la inmunidad de autoridades. Belmont propone reestructurar PNP, MP, INPE y PJ con énfasis en percepción ciudadana y resolver el 50% de denuncias. Belmont tiene el plan más específico y operativo; Olivera tiene un enfoque más orientado a la reforma política.

## 📚 EDUCACIÓN

Olivera prioriza la alimentación y desnutrición como base del rendimiento educativo. Belmont propone educación gratuita y obligatoria con deporte, folklore y valores, y deserción rural al 5%. Belmont tiene el plan más específico con metas concretas; Olivera tiene el enfoque más preventivo y social.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura como determinantes de salud. Belmont propone cobertura al 85%, rehabilitar puestos rurales y construir 50 nuevos establecimientos. Belmont tiene metas más específicas y operativas.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales para el turismo. Belmont propone 10,000 km de caminos rurales y cuestiona el modelo de concesiones de peajes. Belmont tiene el plan más territorial y orientado a las necesidades rurales básicas.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas ambientales sin metas verificables. Belmont tiene dimensión territorial-ambiental con énfasis en ordenamiento y desarrollo sostenible. Belmont tiene una propuesta ambiental más coherente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica central. Belmont propone imprescriptibilidad de delitos de corrupción y plataforma digital de obras. Ambos tienen buena credibilidad anticorrupción personal.

## 📊 CONCLUSIÓN TÉCNICA

Belmont tiene el plan más operativo y con metas más específicas en salud rural, desnutrición e infraestructura básica. Olivera tiene mayor historia anticorrupción y un enfoque más político-institucional orientado a la reforma del Estado. Ambos son candidatos con credibilidad personal razonable pero sin la sofisticación técnica de López Chau, Nieto o Pérez Tello.""",

"165:170": """## 💰 ECONOMÍA

Olivera propone reducción progresiva del IGV al 10% y nuevos aeropuertos regionales. Luna Gálvez propone reactivación económica genérica sin metas específicas. Olivera tiene el plan más articulado de los dos en reducción tributaria para la formalización.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales anticorrupción. Luna Gálvez tiene propuestas genéricas de seguridad debilitadas por sus investigaciones por manipulación de ONPE y CNM. Olivera tiene mayor credibilidad en este eje.

## 📚 EDUCACIÓN

Olivera prioriza la nutrición como base del rendimiento educativo. Luna Gálvez propone mejorar calidad y conectividad sin propuestas diferenciadas. Ninguno tiene un plan educativo sofisticado.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura. Luna Gálvez propone ampliar cobertura sin financiamiento claro. Olivera tiene el enfoque más coherente con las causas estructurales de la desnutrición.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales. Luna Gálvez propone infraestructura vial genérica. Planes igualmente modestos.

## 🌿 MEDIO AMBIENTE

Ninguno tiene una propuesta ambiental seria. Planes igualmente débiles en este eje.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica con propuestas concretas de reforma institucional. Luna Gálvez enfrenta investigaciones por manipulación de organismos autónomos del Estado — amenaza directa a la democracia. La diferencia en credibilidad es abismal.

## 📊 CONCLUSIÓN TÉCNICA

Olivera supera a Luna Gálvez en credibilidad anticorrupción y coherencia programática. Las investigaciones de Luna Gálvez por captura institucional del Estado hacen que esta comparación sea una de las más claras del campo electoral.""",

"165:171": """## 💰 ECONOMÍA

Olivera propone reducción del IGV al 10% y formalización con un millón de empleos anuales. Álvarez propone disciplina fiscal, convergencia del déficit al 1% del PBI y digitalización total del Estado. Planes modestos en ambos casos, con distintos énfasis: Olivera en reducción tributaria, Álvarez en gestión fiscal eficiente.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales anticorrupción. Álvarez propone Plataforma Nacional de Análisis Criminal y meta de reducir homicidios de 8.6 a 6 por 100 mil. El plan de seguridad de Álvarez es más detallado y técnico que el de Olivera.

## 📚 EDUCACIÓN

Olivera prioriza la nutrición como base educativa. Álvarez propone acceso universal sin reformas estructurales. Olivera tiene el enfoque más coherente en la relación nutrición-aprendizaje; Álvarez tiene un enfoque más convencional.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura. Álvarez propone ampliar coberturas con programas sociales. Olivera tiene el enfoque más preventivo; Álvarez tiene el más asistencial.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales para el turismo. Álvarez propone obras básicas de infraestructura. Planes igualmente modestos.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas sin metas verificables. Álvarez incluye sostenibilidad con énfasis en agua rural. Planes igualmente débiles.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica. Álvarez propone transparencia con digitalización. Ambos tienen buena credibilidad anticorrupción personal.

## 📊 CONCLUSIÓN TÉCNICA

Álvarez tiene el plan de seguridad más detallado de los dos y mayor potencial electoral según encuestas. Olivera tiene mayor historia anticorrupción y un enfoque más coherente en nutrición-educación. Ambos tienen perfiles programáticos modestos comparados con López Chau, Nieto o Pérez Tello.""",

"165:172": """## 💰 ECONOMÍA

Olivera propone reducción del IGV al 10% y nuevos aeropuertos. Pérez Tello propone digitalización radical del Estado, economía digital, bioindustria y diversificación sectorial con meta de inversión privada del 22% del PBI. Pérez Tello tiene el plan económico sustancialmente más sofisticado y diversificado.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales anticorrupción. Pérez Tello propone derogar leyes procrimen, modernización policial con tecnología predictiva y enfoque preventivo-comunitario. Pérez Tello tiene el plan más completo y equilibrado.

## 📚 EDUCACIÓN

Olivera prioriza la nutrición como base del aprendizaje. Pérez Tello propone universalizar inicial, mejorar calidad docente y educación intercultural. Pérez Tello tiene el plan más sistémico y completo.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura. Pérez Tello propone integrar sistemas con énfasis en atención primaria y medicamentos esenciales. Pérez Tello tiene el plan más integral.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Pérez Tello tiene el plan más equitativo territorialmente.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas sin metas verificables. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica central. Pérez Tello propone digitalización estatal, control ciudadano y reforma judicial, con credibilidad ministerial. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello supera a Olivera en casi todas las dimensiones programáticas: economía más sofisticada, seguridad más equilibrada, salud más integral y medio ambiente más consistente. Olivera tiene una historia anticorrupción más larga y el enfoque más coherente en nutrición infantil. La superioridad programática de Pérez Tello es clara.""",

"165:173": """## 💰 ECONOMÍA

Olivera propone reducción del IGV al 10% y formalización con un millón de empleos anuales, dentro del marco del libre mercado. Sánchez propone superar el modelo neoliberal con economía mixta, soberanía sobre recursos y presión tributaria del 25%. Son posiciones ideológicamente distintas: Olivera es más liberal en lo tributario; Sánchez es más intervencionista.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales anticorrupción. Sánchez propone depuración policial, inteligencia financiera y ataque a economías ilegales. Sánchez tiene el plan de seguridad más específico.

## 📚 EDUCACIÓN

Olivera prioriza la nutrición como base educativa. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo e inclusivo.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura. Sánchez propone Redes Integradas de Salud con tiempo máximo de 72 horas para diagnósticos. Sánchez tiene el plan más sistémico y con mayor cobertura territorial.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales. Sánchez propone 10,000 km de caminos rurales. Sánchez tiene el plan más orientado a la conectividad rural básica.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas ambientales sin metas verificables. Sánchez propone transición ecológica justa y compromisos con comunidades indígenas. Sánchez tiene la propuesta ambiental más ambiciosa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con Castillo genera dudas. Olivera tiene mayor credibilidad anticorrupción institucional.

## 📊 CONCLUSIÓN TÉCNICA

Sánchez supera a Olivera en salud, educación, transporte rural y medio ambiente. Olivera supera a Sánchez en credibilidad anticorrupción institucional y coherencia con el marco económico actual. Ambos tienen propuestas modestas comparadas con los candidatos líderes, pero con enfoques sociales relativamente coherentes.""",

"166:170": """## 💰 ECONOMÍA

Fujimori defiende el libre mercado con disciplina fiscal, shock desregulatorio y atracción de inversión privada. Luna Gálvez propone reactivación económica genérica sin metas específicas ni financiamiento claro. Fujimori tiene el plan económico sustancialmente más sofisticado y articulado.

## 🔒 SEGURIDAD

Fujimori propone mano dura con FFAA, videovigilancia avanzada y mega penales. Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de ONPE y CNM. Fujimori tiene el plan más específico y operativo.

## 📚 EDUCACIÓN

Fujimori propone inglés obligatorio, becas e infraestructura educativa masiva. Luna Gálvez propone mejorar calidad y conectividad sin innovaciones. Fujimori tiene el plan más moderno y específico.

## 🏥 SALUD

Fujimori propone reducir anemia al 20%, universalizar vacunación e invertir en infraestructura hospitalaria. Luna Gálvez propone ampliar cobertura sin mecanismos claros. Fujimori supera claramente en este eje.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros en Lima, metros regionales y pavimentación rural. Luna Gálvez propone inversión vial genérica. Fujimori tiene propuestas de mayor escala y especificidad.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley General de Minería con respeto ambiental. Luna Gálvez tiene propuestas ambientales genéricas. Ninguno tiene una propuesta ambiental sólida.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori enfrenta tres procesos penales por Odebrecht. Luna Gálvez enfrenta investigaciones por manipulación de ONPE y CNM. Ambos tienen perfiles anticorrupción comprometidos, aunque de naturaleza diferente: Fujimori por presunta corrupción económica, Luna Gálvez por presunta captura institucional.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori supera a Luna Gálvez en todas las dimensiones programáticas. Ambos tienen graves cuestionamientos anticorrupción que los debilitan institucionalmente, aunque los antecedentes de Luna Gálvez por manipulación de organismos electorales representan una amenaza más directa a la democracia.""",

"166:171": """## 💰 ECONOMÍA

Fujimori defiende el libre mercado con disciplina fiscal y shock desregulatorio. Álvarez propone disciplina fiscal similar — convergencia del déficit al 1% del PBI — con digitalización total del Estado. Ambos son afines macroeconómicamente, aunque Fujimori tiene un plan más detallado con metas específicas de inversión.

## 🔒 SEGURIDAD

Fujimori propone mano dura con FFAA y videovigilancia avanzada. Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. El plan de Álvarez es sorprendentemente más técnico en su especificidad de metas; Fujimori tiene mayor escala operativa.

## 📚 EDUCACIÓN

Fujimori propone inglés, becas e infraestructura. Álvarez propone acceso universal sin reformas estructurales. Fujimori tiene el plan más moderno y específico.

## 🏥 SALUD

Fujimori propone reducir anemia al 20% y universalizar vacunación. Álvarez propone ampliar coberturas con programas sociales. Fujimori tiene el plan más específico.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros, metros regionales y pavimentación. Álvarez propone obras básicas con digitalización estatal. Fujimori tiene propuestas de mayor escala.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley de Minería con respeto ambiental. Álvarez incluye sostenibilidad con énfasis en agua rural. Planes igualmente modestos en compromisos climáticos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori enfrenta tres procesos penales por Odebrecht. Álvarez tiene mayor credibilidad anticorrupción personal y propone digitalización total del Estado. Álvarez tiene el perfil anticorrupción más limpio de los dos.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori tiene el plan más detallado técnicamente en macroeconomía, infraestructura y seguridad operativa. Álvarez tiene mayor credibilidad anticorrupción y un plan de seguridad con metas sorprendentemente específicas. El principal diferenciador es el historial judicial de Fujimori frente al perfil más limpio de Álvarez.""",

"166:172": """## 💰 ECONOMÍA

Fujimori defiende el libre mercado con disciplina fiscal y shock desregulatorio. Pérez Tello propone digitalización radical del Estado, economía digital, bioindustria y diversificación sectorial. Ambos planes son de alta calidad técnica — Fujimori más ortodoxo en libre mercado; Pérez Tello más innovador en diversificación sectorial. La analista Costa del El Comercio destacó a ambas entre los candidatos con propuestas económicas más serias.

## 🔒 SEGURIDAD

Fujimori propone mano dura con FFAA, videovigilancia avanzada y mega penales. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Fujimori tiene mayor escala operativa; Pérez Tello tiene mayor equilibrio entre represión y prevención.

## 📚 EDUCACIÓN

Fujimori propone inglés, becas e infraestructura. Pérez Tello propone universalizar inicial, mejorar calidad docente y educación intercultural. Planes complementarios — Fujimori más en infraestructura y competencias; Pérez Tello más en inclusión y calidad.

## 🏥 SALUD

Fujimori propone reducir anemia al 20% y universalizar vacunación. Pérez Tello propone integrar sistemas con atención primaria y medicamentos esenciales. Pérez Tello tiene el plan más integral y sistémico.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros, metros regionales y pavimentación. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Fujimori tiene mayor escala; Pérez Tello tiene mayor equidad territorial.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley de Minería con respeto ambiental, sin compromisos climáticos. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori enfrenta tres procesos penales por Odebrecht. Pérez Tello propone digitalización estatal y control ciudadano, con trayectoria ministerial sin investigaciones relevantes. Pérez Tello tiene sustancialmente mayor credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori tiene el plan más detallado en macroeconomía y mayor presencia electoral. Pérez Tello tiene mayor coherencia programática global — mejor en salud, medio ambiente, anticorrupción y educación inclusiva. La diferencia clave es que Fujimori tiene el mayor lastre judicial del campo, mientras Pérez Tello tiene el perfil más limpio y el plan más diversificado.""",

"167:168": """## 💰 ECONOMÍA

Nieto propone Fondo Soberano de Riqueza, crecimiento del 5%, presión tributaria del 18% y diversificación productiva con economía circular. López Aliaga propone reforma tributaria agresiva — unificar regímenes, reducir IGV, Banco Pyme — con meta de 7% de crecimiento y 2 millones de empleos. Ambos tienen planes económicos de alta calidad técnica. Nieto es más macroeconómicamente cauteloso y orientado a la sostenibilidad; López Aliaga es más agresivo en reformas tributarias con mayor riesgo fiscal.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional integral. López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, penales de alta montaña y Comando 'Las Palmas'. López Aliaga tiene las propuestas más disruptivas e innovadoras; Nieto tiene el enfoque más institucionalista y menos punitivo.

## 📚 EDUCACIÓN

Nieto propone reforma curricular, conectividad digital universal y mejora docente. López Aliaga propone Chino Mandarín, Libertad Financiera e internet satelital. Nieto tiene el plan más sistémico y orientado a la calidad; López Aliaga tiene el plan más orientado al mercado global.

## 🏥 SALUD

Nieto propone integrar sistemas de salud con estrategia preventiva y atención a anemia y mortalidad materna. López Aliaga propone transformar EsSalud en entidad técnica autónoma y medicamentos genéricos. Nieto tiene el plan más integral; López Aliaga tiene el plan más específico en reforma institucional.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con énfasis en equidad territorial. López Aliaga propone trenes de alta velocidad, túnel trasandino y zonas francas. López Aliaga tiene las propuestas más innovadoras y ambiciosas.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica, economía circular y sostenibilidad como ejes transversales. López Aliaga prioriza el litio y las zonas francas con agenda ambiental secundaria. Nieto tiene la propuesta ambiental más coherente de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral, con trayectoria ministerial impecable. López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, aunque enfrenta cuestionamientos por presunta deuda con la SUNAT y aportes de constructoras brasileñas a su partido.

## 📊 CONCLUSIÓN TÉCNICA

Nieto y López Aliaga son dos de los candidatos con mayor calidad programática del campo electoral. Nieto tiene el plan más equilibrado, coherente ambientalmente y el perfil anticorrupción más limpio. López Aliaga tiene las propuestas más disruptivas e innovadoras en seguridad, transporte y tributación, con mayor presencia electoral. La diferencia es entre la reforma institucional sostenible (Nieto) y la transformación radical de alto impacto (López Aliaga).""",

"167:169": """## 💰 ECONOMÍA

Nieto propone Fondo Soberano de Riqueza, crecimiento del 5% y diversificación productiva. Belmont propone economía social de mercado y Plan Choque de 1,500 obras paralizadas. Nieto tiene el plan más sofisticado técnicamente; Belmont tiene el plan más pragmático y orientado a resultados concretos.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional integral. Belmont propone reestructurar PNP, MP, INPE y PJ con énfasis en percepción ciudadana. Enfoques similares — ambos institucionalistas — aunque Nieto es más específico en la dimensión legislativa y Belmont en la dimensión operativa.

## 📚 EDUCACIÓN

Nieto propone reforma curricular y mejora docente. Belmont propone educación gratuita con deporte y folklore, y deserción rural al 5%. Nieto tiene el plan más moderno; Belmont tiene el plan más culturalista y comunitario.

## 🏥 SALUD

Nieto propone integrar sistemas con estrategia preventiva. Belmont propone cobertura al 85% y rehabilitar puestos rurales. Belmont tiene metas más específicas; Nieto tiene el plan más sistémico.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con equidad territorial. Belmont propone 10,000 km de caminos rurales. Enfoques similares, ambos más modestos que Fujimori o López Aliaga pero más realistas.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica y economía circular. Belmont tiene dimensión territorial-ambiental con ordenamiento del territorio. Nieto tiene la propuesta ambiental más completa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral. Belmont propone imprescriptibilidad de delitos de corrupción con trayectoria personal relativamente limpia. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Nieto tiene el plan técnicamente más coherente y el perfil anticorrupción más sólido. Belmont tiene propuestas más operativas en salud rural y obras concretas. Ambos representan alternativas programáticamente serias de centro, con mayor calidad que varios candidatos con mayor presencia electoral.""",

"167:170": """## 💰 ECONOMÍA

Nieto propone Fondo Soberano de Riqueza, crecimiento del 5% y diversificación productiva. Luna Gálvez propone reactivación económica genérica sin metas específicas. Nieto supera claramente a Luna Gálvez en sofisticación económica.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional. Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de ONPE y CNM. Nieto gana claramente.

## 📚 EDUCACIÓN

Nieto propone reforma curricular y mejora docente. Luna Gálvez propone mejorar calidad sin innovaciones. Nieto tiene el plan más específico y moderno.

## 🏥 SALUD

Nieto propone integrar sistemas con estrategia preventiva. Luna Gálvez propone ampliar cobertura sin financiamiento claro. Nieto supera a Luna Gálvez.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con equidad territorial. Luna Gálvez propone inversión vial genérica. Nieto tiene el plan más articulado.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica y economía circular. Luna Gálvez tiene propuestas genéricas. Nieto gana claramente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral. Luna Gálvez enfrenta investigaciones por manipulación de organismos autónomos del Estado. La diferencia es abismal.

## 📊 CONCLUSIÓN TÉCNICA

Nieto supera a Luna Gálvez en todas las dimensiones programáticas. Las investigaciones de Luna Gálvez por captura institucional representan una amenaza directa a la democracia que hace que esta comparación sea una de las más claras del campo electoral.""",

"167:171": """## 💰 ECONOMÍA

Nieto propone Fondo Soberano de Riqueza y diversificación productiva. Álvarez propone disciplina fiscal con convergencia del déficit al 1% del PBI y digitalización total del Estado. Ambos planes son macroeconómicamente responsables; Nieto tiene el plan más innovador con el Fondo Soberano; Álvarez tiene el plan más convencional pero con mayor énfasis en digitalización.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional. Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. Álvarez tiene el plan de seguridad más técnico en metas específicas; Nieto tiene el más orientado a la reforma legislativa.

## 📚 EDUCACIÓN

Nieto propone reforma curricular y mejora docente. Álvarez propone acceso universal sin reformas estructurales. Nieto tiene el plan más sistémico.

## 🏥 SALUD

Nieto propone integrar sistemas con estrategia preventiva. Álvarez propone ampliar coberturas con programas sociales. Nieto tiene el plan más integral.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con equidad territorial. Álvarez propone obras básicas con digitalización. Planes similares en escala y modestia.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica y economía circular. Álvarez incluye sostenibilidad con énfasis en agua rural. Nieto tiene la propuesta ambiental más completa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral. Álvarez propone transparencia con digitalización y tiene buena credibilidad personal. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Nieto tiene el plan más coherente técnicamente. Álvarez tiene un plan de seguridad más técnico en metas y mayor potencial electoral según encuestas. Ambos representan alternativas programáticamente serias de centro.""",

"167:172": """## 💰 ECONOMÍA

Nieto y Pérez Tello tienen los planes económicos más sofisticados del centro del espectro político. Nieto propone Fondo Soberano de Riqueza, crecimiento del 5% y economía circular. Pérez Tello propone economía digital, bioindustria y diversificación sectorial con meta de inversión privada del 22% del PBI. Planes de alta calidad con distintos énfasis: Nieto más macroeconómico y fiscal; Pérez Tello más orientado a la diversificación sectorial y la economía del conocimiento.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional integral. Pérez Tello propone derogar leyes procrimen, modernización policial con tecnología predictiva y enfoque preventivo. Plans muy similares — ambos institucionalistas, tecnológicos y no punitivos.

## 📚 EDUCACIÓN

Nieto propone reforma curricular y mejora docente. Pérez Tello propone universalizar inicial y educación intercultural. Plans complementarios de alta calidad.

## 🏥 SALUD

Nieto propone integrar sistemas con estrategia preventiva. Pérez Tello propone integrar sistemas con énfasis en atención primaria y medicamentos esenciales. Planes muy similares en calidad y enfoque.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con equidad territorial. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Planes similares en escala y equidad.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica y economía circular. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Planes complementarios de alta calidad ambiental — los dos más consistentes del campo electoral junto con Sánchez.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral. Pérez Tello propone digitalización estatal y reforma judicial con credibilidad ministerial. Ambos tienen la mayor credibilidad anticorrupción del campo.

## 📊 CONCLUSIÓN TÉCNICA

Nieto y Pérez Tello son los dos candidatos de mayor calidad programática del centro del campo electoral 2026 según los analistas. Sus planes son complementarios más que competidores: Nieto es más sólido en macroeconomía y sostenibilidad ambiental; Pérez Tello es más innovador en economía del conocimiento y digitalización. Es la comparación programática más pareja y de mayor calidad del campo electoral.""",

"167:173": """## 💰 ECONOMÍA

Nieto defiende el modelo de mercado con diversificación productiva. Sánchez propone superar el modelo neoliberal con economía mixta y soberanía sobre recursos. Posiciones distintas ideológicamente: Nieto es más afín al consenso técnico internacional; Sánchez propone una transformación estructural con mayor incertidumbre para la inversión privada.

## 🔒 SEGURIDAD

Nieto propone derogar leyes procrimen y reforma institucional. Sánchez propone depuración policial y ataque a economías ilegales con veedurías ciudadanas. Enfoques similares en el énfasis institucional, con diferencias en la profundidad de la reforma.

## 📚 EDUCACIÓN

Nieto propone reforma curricular y mejora docente. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo; Nieto el más técnico en reforma sistémica.

## 🏥 SALUD

Nieto propone integrar sistemas con estrategia preventiva. Sánchez propone Redes Integradas con Fondo para suministros y tiempo máximo de 72 horas. Sánchez tiene el plan más sistémico con metas operativas más específicas.

## 🚆 TRANSPORTE

Nieto propone infraestructura vial con equidad territorial. Sánchez propone 10,000 km de caminos rurales. Planes similares en énfasis territorial.

## 🌿 MEDIO AMBIENTE

Nieto incluye transición ecológica y economía circular. Sánchez propone transición ecológica justa y compromisos con comunidades indígenas. Ambos tienen propuestas ambientales serias — las más consistentes del campo electoral junto con Pérez Tello.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Nieto tiene el perfil anticorrupción más limpio del campo electoral. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con Castillo genera dudas. Nieto tiene mayor credibilidad institucional anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Nieto tiene el plan más coherente técnicamente y el perfil anticorrupción más sólido. Sánchez tiene el plan más ambicioso en distribución social, salud territorial y medio ambiente. La diferencia es entre la reforma institucional dentro del modelo actual (Nieto) y la transformación constitucional del modelo económico (Sánchez).""",

"168:170": """## 💰 ECONOMÍA

López Aliaga propone reforma tributaria agresiva con meta de 7% de crecimiento y 2 millones de empleos. Luna Gálvez propone reactivación económica genérica sin metas específicas. López Aliaga supera ampliamente a Luna Gálvez en sofisticación y especificidad económica.

## 🔒 SEGURIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos y penales de alta montaña. Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de ONPE y CNM. López Aliaga gana claramente.

## 📚 EDUCACIÓN

López Aliaga propone Chino Mandarín, Libertad Financiera e internet satelital. Luna Gálvez propone mejorar calidad sin innovaciones. López Aliaga tiene el plan más diferenciado.

## 🏥 SALUD

López Aliaga propone transformar EsSalud en entidad técnica autónoma. Luna Gálvez propone ampliar cobertura sin mecanismos claros. López Aliaga tiene el plan más específico en reforma institucional.

## 🚆 TRANSPORTE

López Aliaga propone trenes de alta velocidad y túnel trasandino. Luna Gálvez propone inversión vial genérica. López Aliaga tiene propuestas de mayor escala e innovación.

## 🌿 MEDIO AMBIENTE

López Aliaga prioriza el litio y las zonas francas. Luna Gálvez tiene propuestas genéricas. Ninguno tiene propuesta ambiental seria.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos. Luna Gálvez enfrenta investigaciones por manipulación de organismos autónomos del Estado. La diferencia en credibilidad anticorrupción es abismal.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga supera a Luna Gálvez en todas las dimensiones programáticas. Las investigaciones de Luna Gálvez representan una amenaza directa a la democracia institucional que hace que esta comparación sea una de las más claras del campo electoral.""",

"168:171": """## 💰 ECONOMÍA

López Aliaga propone reforma tributaria agresiva con meta de 7% de crecimiento. Álvarez propone disciplina fiscal con convergencia del déficit al 1% y digitalización total del Estado. López Aliaga tiene el plan más agresivo en reformas; Álvarez tiene el más convencional. Ambos defienden el libre mercado.

## 🔒 SEGURIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos y penales de alta montaña. Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. López Aliaga tiene las propuestas más disruptivas; Álvarez tiene las más técnicas en metas específicas.

## 📚 EDUCACIÓN

López Aliaga propone Chino Mandarín y parques tecnológicos. Álvarez propone acceso universal sin reformas estructurales. López Aliaga tiene el plan más diferenciado.

## 🏥 SALUD

López Aliaga propone transformar EsSalud con meritocracia. Álvarez propone ampliar coberturas con programas sociales. López Aliaga tiene el plan más específico en reforma institucional.

## 🚆 TRANSPORTE

López Aliaga propone trenes de alta velocidad y túnel trasandino. Álvarez propone obras básicas con digitalización. López Aliaga tiene propuestas de mayor escala e innovación.

## 🌿 MEDIO AMBIENTE

López Aliaga prioriza el litio y zonas francas. Álvarez incluye sostenibilidad con agua rural. Planes igualmente modestos en compromisos climáticos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga tiene mayor credibilidad anticorrupción personal que Fujimori, aunque enfrenta cuestionamientos por deuda tributaria y aportes de constructoras. Álvarez tiene buena credibilidad personal y propone digitalización estatal. Ambos tienen credibilidad anticorrupción razonable.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga tiene el plan más ambicioso e innovador. Álvarez tiene un plan de seguridad más técnico en metas y mayor potencial electoral sorpresivo según encuestas. La comparación refleja la diferencia entre el candidato con las propuestas más disruptivas (López Aliaga) y el candidato con mayor potencial de sorpresa electoral (Álvarez).""",

"168:172": """## 💰 ECONOMÍA

López Aliaga propone reforma tributaria agresiva, 7% de crecimiento y zonas francas. Pérez Tello propone economía digital, bioindustria y diversificación sectorial. Ambos tienen planes de alta calidad técnica: López Aliaga más agresivo en reformas tributarias; Pérez Tello más innovador en diversificación sectorial.

## 🔒 SEGURIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos y penales de alta montaña. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. López Aliaga tiene las propuestas más disruptivas; Pérez Tello tiene el plan más equilibrado entre represión y prevención.

## 📚 EDUCACIÓN

López Aliaga propone Chino Mandarín y parques tecnológicos. Pérez Tello propone universalizar inicial, mejorar calidad docente y educación intercultural. Pérez Tello tiene el plan más sistémico e inclusivo.

## 🏥 SALUD

López Aliaga propone transformar EsSalud con meritocracia. Pérez Tello propone integrar sistemas con atención primaria y medicamentos esenciales. Pérez Tello tiene el plan más integral.

## 🚆 TRANSPORTE

López Aliaga propone trenes de alta velocidad y túnel trasandino. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. López Aliaga tiene mayor escala; Pérez Tello tiene mayor equidad territorial.

## 🌿 MEDIO AMBIENTE

López Aliaga prioriza el litio y zonas francas. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga tiene credibilidad anticorrupción razonable con cuestionamientos por deuda tributaria y aportes de constructoras. Pérez Tello tiene credibilidad ministerial sólida con trayectoria sin investigaciones relevantes. Pérez Tello tiene el perfil anticorrupción más limpio de los dos.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga y Pérez Tello son dos de los candidatos con mayor calidad programática del campo electoral. López Aliaga tiene las propuestas más disruptivas e innovadoras en seguridad, transporte y tributación. Pérez Tello tiene el plan más coherente en salud integral, educación inclusiva, medio ambiente y anticorrupción. La diferencia es entre la transformación radical de alto impacto (López Aliaga) y la reforma sistémica sostenible (Pérez Tello).""",

"169:170": """## 💰 ECONOMÍA

Belmont propone economía social de mercado con Plan Choque de obras paralizadas. Luna Gálvez propone reactivación económica genérica sin metas específicas. Belmont tiene el plan más articulado con metas concretas; Luna Gálvez tiene el plan más genérico.

## 🔒 SEGURIDAD

Belmont propone reestructurar PNP, MP, INPE y PJ con metas de percepción ciudadana. Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de ONPE y CNM. Belmont tiene mayor credibilidad y especificidad.

## 📚 EDUCACIÓN

Belmont propone educación gratuita con deporte y folklore, y deserción rural al 5%. Luna Gálvez propone mejorar calidad sin innovaciones. Belmont tiene el plan más específico.

## 🏥 SALUD

Belmont propone cobertura al 85% y rehabilitar puestos rurales. Luna Gálvez propone ampliar cobertura sin mecanismos claros. Belmont supera claramente con metas específicas.

## 🚆 TRANSPORTE

Belmont propone 10,000 km de caminos rurales. Luna Gálvez propone inversión vial genérica. Belmont tiene el plan más articulado.

## 🌿 MEDIO AMBIENTE

Belmont tiene dimensión territorial-ambiental con ordenamiento del territorio. Luna Gálvez tiene propuestas genéricas. Belmont tiene la propuesta más coherente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Belmont propone imprescriptibilidad de delitos de corrupción con historial personal relativamente limpio. Luna Gálvez enfrenta investigaciones por manipulación de organismos autónomos del Estado. La diferencia en credibilidad es abismal.

## 📊 CONCLUSIÓN TÉCNICA

Belmont supera a Luna Gálvez en todas las dimensiones programáticas y en credibilidad anticorrupción. Las investigaciones de Luna Gálvez por captura institucional hacen que esta comparación sea de las más claras del campo electoral.""",

"169:171": """## 💰 ECONOMÍA

Belmont propone economía social de mercado y Plan Choque de obras. Álvarez propone disciplina fiscal con digitalización del Estado. Ambos tienen planes modestos en sofisticación técnica — Belmont más centrado en obras concretas; Álvarez más en gestión fiscal eficiente.

## 🔒 SEGURIDAD

Belmont propone reestructurar el sistema judicial con énfasis en percepción ciudadana. Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. Álvarez tiene el plan de seguridad más técnico en metas específicas.

## 📚 EDUCACIÓN

Belmont propone educación gratuita con deporte y folklore. Álvarez propone acceso universal sin reformas estructurales. Belmont tiene el plan más culturalista; Álvarez el más convencional.

## 🏥 SALUD

Belmont propone cobertura al 85% y rehabilitar puestos rurales. Álvarez propone ampliar coberturas con programas sociales. Belmont tiene las metas más específicas y territorialmente focalizadas.

## 🚆 TRANSPORTE

Belmont propone 10,000 km de caminos rurales. Álvarez propone obras básicas con digitalización. Planes similares en escala y modestia.

## 🌿 MEDIO AMBIENTE

Belmont tiene dimensión territorial-ambiental con ordenamiento del territorio. Álvarez incluye sostenibilidad con agua rural. Planes similares en coherencia ambiental.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Belmont propone imprescriptibilidad de delitos de corrupción. Álvarez propone transparencia con digitalización. Ambos tienen buena credibilidad anticorrupción personal.

## 📊 CONCLUSIÓN TÉCNICA

Belmont tiene propuestas más específicas en salud rural y obras concretas. Álvarez tiene el plan de seguridad más técnico y mayor potencial electoral sorpresivo. Ambos representan alternativas de centro-derecha pragmáticas con credibilidad anticorrupción razonable.""",

"169:172": """## 💰 ECONOMÍA

Belmont propone economía social de mercado y Plan Choque de obras. Pérez Tello propone economía digital, bioindustria y diversificación sectorial. Pérez Tello tiene el plan económico sustancialmente más sofisticado y diversificado.

## 🔒 SEGURIDAD

Belmont propone reestructurar el sistema judicial. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Pérez Tello tiene el plan más completo y equilibrado.

## 📚 EDUCACIÓN

Belmont propone educación gratuita con deporte y folklore. Pérez Tello propone universalizar inicial y educación intercultural. Pérez Tello tiene el plan más sistémico; Belmont tiene el más culturalista y comunitario.

## 🏥 SALUD

Belmont propone cobertura al 85% con metas específicas. Pérez Tello propone integrar sistemas con atención primaria. Belmont tiene las metas más específicas territorialmente; Pérez Tello tiene el plan más integral.

## 🚆 TRANSPORTE

Belmont propone 10,000 km de caminos rurales. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Enfoques similares en escala y equidad territorial.

## 🌿 MEDIO AMBIENTE

Belmont tiene dimensión territorial-ambiental. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Belmont propone imprescriptibilidad de delitos de corrupción con historial personal relativamente limpio. Pérez Tello propone digitalización estatal y reforma judicial con credibilidad ministerial sólida. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello supera a Belmont en sofisticación económica, salud integral y medio ambiente. Belmont tiene propuestas más específicas en obras concretas y salud rural. Pérez Tello tiene la mayor calidad programática global de los dos.""",

"169:173": """## 💰 ECONOMÍA

Belmont propone economía social de mercado con Plan Choque de obras. Sánchez propone superar el modelo neoliberal con economía mixta y soberanía sobre recursos. Posiciones distintas: Belmont dentro del marco de mercado; Sánchez con mayor intervención estatal.

## 🔒 SEGURIDAD

Belmont propone reestructurar el sistema judicial con énfasis en percepción ciudadana. Sánchez propone depuración policial y ataque a economías ilegales. Enfoques similares en el énfasis institucional.

## 📚 EDUCACIÓN

Belmont propone educación gratuita con deporte y folklore. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo; Belmont el más comunitario.

## 🏥 SALUD

Belmont propone cobertura al 85% con metas específicas. Sánchez propone Redes Integradas con tiempo máximo de 72 horas para diagnósticos. Sánchez tiene el plan más sistémico; Belmont tiene las metas más específicas en zonas rurales.

## 🚆 TRANSPORTE

Belmont propone 10,000 km de caminos rurales. Sánchez propone 10,000 km de caminos rurales también. Los planes son prácticamente idénticos en este eje.

## 🌿 MEDIO AMBIENTE

Belmont tiene dimensión territorial-ambiental. Sánchez propone transición ecológica justa y compromisos con comunidades indígenas. Sánchez tiene la propuesta ambiental más ambiciosa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Belmont propone imprescriptibilidad de delitos de corrupción. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con Castillo genera dudas. Belmont tiene mayor credibilidad institucional anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Belmont y Sánchez son los candidatos con mayor orientación hacia las necesidades de los sectores populares, aunque con enfoques distintos. Sánchez tiene el plan más ambicioso en salud, educación y medio ambiente. Belmont tiene mayor credibilidad institucional y propuestas más pragmáticas en obras concretas.""",

"170:171": """## 💰 ECONOMÍA

Luna Gálvez propone reactivación económica genérica sin metas específicas. Álvarez propone disciplina fiscal con digitalización del Estado y convergencia del déficit al 1% del PBI. Álvarez tiene el plan más articulado y responsable fiscalmente.

## 🔒 SEGURIDAD

Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de ONPE y CNM. Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. Álvarez supera claramente en credibilidad y especificidad.

## 📚 EDUCACIÓN

Luna Gálvez propone mejorar calidad sin innovaciones. Álvarez propone acceso universal. Álvarez tiene el plan más convencional pero más orientado a la inclusión.

## 🏥 SALUD

Luna Gálvez propone ampliar cobertura sin financiamiento claro. Álvarez propone ampliar coberturas con programas sociales. Planes similares en ambición, con Álvarez más articulado.

## 🚆 TRANSPORTE

Luna Gálvez propone inversión vial genérica. Álvarez propone obras básicas con digitalización. Planes similares en modestia.

## 🌿 MEDIO AMBIENTE

Ambos tienen propuestas ambientales genéricas. Luna Gálvez incluye propuestas sin compromisos medibles. Planes igualmente débiles.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Luna Gálvez enfrenta investigaciones por manipulación de ONPE y CNM — amenaza directa a la democracia. Álvarez propone transparencia con digitalización y tiene buena credibilidad personal. La diferencia es abismal.

## 📊 CONCLUSIÓN TÉCNICA

Álvarez supera a Luna Gálvez en credibilidad anticorrupción y especificidad de propuestas. Las investigaciones de Luna Gálvez por captura institucional representan el mayor riesgo democrático del campo electoral, lo que hace que esta comparación sea una de las más claras a favor de Álvarez.""",

"170:172": """## 💰 ECONOMÍA

Luna Gálvez propone reactivación económica genérica. Pérez Tello propone economía digital, bioindustria y diversificación sectorial con meta de inversión privada del 22% del PBI. Pérez Tello supera ampliamente en sofisticación técnica.

## 🔒 SEGURIDAD

Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones por manipulación de organismos autónomos. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Pérez Tello supera claramente.

## 📚 EDUCACIÓN

Luna Gálvez propone mejorar calidad sin innovaciones. Pérez Tello propone universalizar inicial y educación intercultural. Pérez Tello tiene el plan más sistémico e inclusivo.

## 🏥 SALUD

Luna Gálvez propone ampliar cobertura sin mecanismos claros. Pérez Tello propone integrar sistemas con atención primaria y medicamentos esenciales. Pérez Tello supera ampliamente.

## 🚆 TRANSPORTE

Luna Gálvez propone inversión vial genérica. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Pérez Tello tiene el plan más articulado.

## 🌿 MEDIO AMBIENTE

Luna Gálvez tiene propuestas genéricas. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello supera claramente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Luna Gálvez enfrenta investigaciones por manipulación de ONPE y CNM. Pérez Tello tiene credibilidad ministerial sólida. La diferencia es abismal.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello supera a Luna Gálvez en todas las dimensiones programáticas y en credibilidad anticorrupción. Las investigaciones de Luna Gálvez por captura institucional hacen que esta comparación sea una de las más claras del campo electoral.""",

"170:173": """## 💰 ECONOMÍA

Luna Gálvez propone reactivación genérica sin metas específicas. Sánchez propone economía mixta, soberanía sobre recursos y presión tributaria del 25%. Sánchez tiene el plan más articulado ideológicamente, aunque con mayor incertidumbre para la inversión privada.

## 🔒 SEGURIDAD

Luna Gálvez tiene propuestas genéricas debilitadas por sus investigaciones. Sánchez propone depuración policial y ataque a economías ilegales. Sánchez tiene el plan más específico y creíble.

## 📚 EDUCACIÓN

Luna Gálvez propone mejorar calidad sin innovaciones. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo e inclusivo.

## 🏥 SALUD

Luna Gálvez propone ampliar cobertura sin mecanismos claros. Sánchez propone Redes Integradas con Fondo para suministros. Sánchez supera claramente.

## 🚆 TRANSPORTE

Luna Gálvez propone inversión vial genérica. Sánchez propone 10,000 km de caminos rurales. Sánchez tiene el plan más articulado.

## 🌿 MEDIO AMBIENTE

Luna Gálvez tiene propuestas genéricas. Sánchez propone transición ecológica justa. Sánchez tiene la propuesta ambiental más ambiciosa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Luna Gálvez enfrenta investigaciones por manipulación de ONPE y CNM. Sánchez propone nueva Constitución con veedurías ciudadanas, aunque su asociación con Castillo genera dudas. Luna Gálvez tiene el peor perfil institucional de los dos.

## 📊 CONCLUSIÓN TÉCNICA

Sánchez supera a Luna Gálvez en todas las dimensiones programáticas. Las investigaciones de Luna Gálvez por captura institucional representan el mayor riesgo democrático del campo, lo que hace que esta comparación sea una de las más claras del campo electoral.""",

"171:172": """## 💰 ECONOMÍA

Álvarez propone disciplina fiscal con digitalización del Estado y convergencia del déficit al 1% del PBI. Pérez Tello propone economía digital, bioindustria y diversificación sectorial con meta de inversión privada del 22% del PBI. Pérez Tello tiene el plan más innovador y diversificado; ambos son macroeconómicamente responsables.

## 🔒 SEGURIDAD

Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Álvarez tiene las metas más específicas; Pérez Tello tiene el enfoque más equilibrado entre represión y prevención.

## 📚 EDUCACIÓN

Álvarez propone acceso universal sin reformas estructurales. Pérez Tello propone universalizar inicial y educación intercultural. Pérez Tello tiene el plan más sistémico e inclusivo.

## 🏥 SALUD

Álvarez propone ampliar coberturas con programas sociales. Pérez Tello propone integrar sistemas con atención primaria y medicamentos esenciales. Pérez Tello tiene el plan más integral.

## 🚆 TRANSPORTE

Álvarez propone obras básicas con digitalización. Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Planes similares en escala y equidad.

## 🌿 MEDIO AMBIENTE

Álvarez incluye sostenibilidad con énfasis en agua rural. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Álvarez propone transparencia con digitalización y tiene buena credibilidad personal. Pérez Tello propone digitalización estatal y reforma judicial con credibilidad ministerial sólida. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello supera a Álvarez en sofisticación económica, salud integral y medio ambiente. Álvarez tiene un plan de seguridad más técnico en metas y mayor potencial electoral sorpresivo según encuestas. La superioridad programática de Pérez Tello contrasta con la mayor popularidad inesperada de Álvarez.""",

"171:173": """## 💰 ECONOMÍA

Álvarez propone disciplina fiscal con digitalización del Estado. Sánchez propone superar el modelo neoliberal con economía mixta y soberanía sobre recursos. Posiciones distintas: Álvarez dentro del marco de mercado con eficiencia fiscal; Sánchez con mayor intervención estatal y reformas estructurales.

## 🔒 SEGURIDAD

Álvarez propone Plataforma Nacional de Análisis Criminal con meta de reducir homicidios de 8.6 a 6 por 100 mil. Sánchez propone depuración policial y ataque a economías ilegales. Álvarez tiene las metas más específicas; Sánchez tiene el enfoque más estructural.

## 📚 EDUCACIÓN

Álvarez propone acceso universal. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo e inclusivo.

## 🏥 SALUD

Álvarez propone ampliar coberturas con programas sociales. Sánchez propone Redes Integradas con tiempo máximo de 72 horas para diagnósticos. Sánchez tiene el plan más sistémico y con mayor cobertura territorial.

## 🚆 TRANSPORTE

Álvarez propone obras básicas con digitalización. Sánchez propone 10,000 km de caminos rurales. Planes similares en escala y orientación rural.

## 🌿 MEDIO AMBIENTE

Álvarez incluye sostenibilidad con agua rural. Sánchez propone transición ecológica justa y compromisos con comunidades indígenas. Sánchez tiene la propuesta ambiental más ambiciosa.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Álvarez propone digitalización y transparencia con buena credibilidad personal. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con Castillo genera dudas. Álvarez tiene mayor credibilidad institucional anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Álvarez tiene mayor credibilidad institucional anticorrupción y un plan de seguridad más técnico. Sánchez tiene el plan más ambicioso en distribución social, salud territorial y medio ambiente. Ambos tienen sorpresiva presencia electoral — Álvarez por su popularidad mediática, Sánchez por su crecimiento en encuestas en las últimas semanas de campaña.""",

"172:173": """## 💰 ECONOMÍA

Pérez Tello y Sánchez representan dos modelos distintos del progresismo peruano. Pérez Tello propone economía digital, bioindustria y diversificación sectorial dentro del marco de mercado, con meta de inversión privada del 22% del PBI. Sánchez propone superar el modelo neoliberal con economía mixta, soberanía sobre recursos y presión tributaria del 25%. Pérez Tello es más afín al consenso técnico internacional; Sánchez propone una transformación estructural más radical.

## 🔒 SEGURIDAD

Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Sánchez propone depuración policial, inteligencia financiera y ataque a economías ilegales con veedurías ciudadanas. Son los dos planes de seguridad más institucionalistas y menos punitivos del campo — complementarios más que opuestos.

## 📚 EDUCACIÓN

Pérez Tello propone universalizar inicial, mejorar calidad docente y educación intercultural. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI, salario de 1 UIT para docentes e ingreso libre a la educación superior. Sánchez tiene el plan más redistributivo; Pérez Tello tiene el más orientado a la calidad sistémica.

## 🏥 SALUD

Pérez Tello propone integrar sistemas con atención primaria y medicamentos esenciales. Sánchez propone Redes Integradas con Fondo para suministros y tiempo máximo de 72 horas. Planes muy similares en calidad y enfoque — los más sistémicos del campo electoral.

## 🚆 TRANSPORTE

Pérez Tello propone conectividad territorial con prioridad en comunidades rurales. Sánchez propone 10,000 km de caminos rurales. Planes muy similares en escala y orientación rural.

## 🌿 MEDIO AMBIENTE

Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Sánchez propone transición ecológica justa, economía circular y compromisos con comunidades indígenas. Ambos tienen las propuestas ambientales más consistentes del campo electoral junto con Nieto. La diferencia es que Pérez Tello es más técnica; Sánchez es más política y redistributiva.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Pérez Tello propone digitalización estatal, control ciudadano y reforma judicial con credibilidad ministerial sólida. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con el gobierno de Castillo y su promesa de indultarlo generan dudas sobre su criterio institucional. Pérez Tello tiene mayor credibilidad institucional anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello y Sánchez son los dos candidatos del progresismo peruano con mayor calidad programática. Pérez Tello tiene el plan más coherente técnicamente, mayor credibilidad institucional anticorrupción y mayor consistencia con el marco económico actual. Sánchez tiene el plan más ambicioso en redistribución social, medio ambiente y reforma constitucional, con mayor arraigo en sectores populares y rurales. Es la comparación más pareja del espectro progresista — la elección entre ambos depende fundamentalmente de si el votante prioriza la viabilidad técnica institucional (Pérez Tello) o la transformación estructural redistributiva (Sánchez).""",

"163:164": """## 💰 ECONOMÍA

Acuña propone inversión masiva en infraestructura con S/143 mil millones en 72 proyectos, expansión minera y petrolera y formalización de MYPES. López Chau apuesta por "Todo el poder a las regiones": descentralización productiva, masificación del gas con tarifa única nacional y conversión de universidades en plataformas de innovación, con crecimiento promedio del 6%. López Chau tiene el plan económico más coherente técnicamente y más orientado a la diversificación productiva; Acuña tiene el plan más ambicioso en infraestructura física.

## 🔒 SEGURIDAD

Acuña plantea el Comando Nacional contra la Extorsión y el Sicariato e incorporar 5,000 efectivos especializados. López Chau propone derogar leyes procrimen, purga policial meritocrática y modernizar comisarías con inteligencia. López Chau tiene el enfoque más institucionalista y estructural; Acuña tiene el más operativo.

## 📚 EDUCACIÓN

Acuña propone COAR por región, programa ILA y reforma curricular con inglés e IA. López Chau propone convertir universidades en plataformas científicas, cobertura universal de inicial y desplegar mil agrónomos jóvenes. López Chau, ex rector de la UNI, tiene mayor credibilidad técnica y un plan más coherente en ciencia aplicada. Acuña tiene mayor énfasis en infraestructura educativa.

## 🏥 SALUD

Acuña propone telemedicina con IA e infraestructura hospitalaria vía APP. López Chau propone integrar Minsa, EsSalud y gobiernos regionales con énfasis en agua potable y saneamiento. López Chau tiene el enfoque más sistémico e integrador.

## 🚆 TRANSPORTE

Acuña propone el portafolio más ambicioso: 72 proyectos con S/143 mil millones. López Chau propone entidad meritocrática para obras regionales y proyectos estratégicos como Chavimochic y Majes Siguas 2. Acuña tiene mayor escala; López Chau tiene mayor anticorrupción en la ejecución.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. López Chau propone gestión de agua con cochas y reservorios — la propuesta hídrica más concreta del campo electoral. López Chau tiene la propuesta ambiental más pertinente territorialmente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales activas — el peor perfil anticorrupción del campo electoral. López Chau tiene alta credibilidad personal y propone meritocracia como eje central anticorrupción. La diferencia en credibilidad es muy significativa.

## 📊 CONCLUSIÓN TÉCNICA

López Chau supera a Acuña en coherencia programática, educación científica, economía descentralizada, gestión ambiental hídrica y anticorrupción. Acuña supera a López Chau en escala de infraestructura y mayor experiencia en gestión pública regional. El diferenciador principal es el historial judicial de Acuña, que contrasta directamente con la credibilidad personal de López Chau.""",

"163:165": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva con 72 proyectos y expansión extractiva. Olivera propone reducción progresiva del IGV al 10% hacia 2031 y nuevos aeropuertos regionales para el turismo. Acuña tiene el plan económico más ambicioso en escala; Olivera tiene propuestas más específicas en reducción tributaria para la formalización.

## 🔒 SEGURIDAD

Acuña plantea el Comando Nacional contra el Sicariato y 5,000 efectivos. Olivera propone reformas institucionales para eliminar la inmunidad de autoridades y mecanismos de transparencia en tiempo real. Acuña tiene el plan más operativo; Olivera tiene el enfoque más anticorrupción e institucional.

## 📚 EDUCACIÓN

Acuña propone COAR por región, ILA y reforma curricular. Olivera propone la alimentación y nutrición como base del rendimiento educativo en zonas rurales. Acuña tiene el plan más moderno y específico; Olivera tiene el enfoque más preventivo y social.

## 🏥 SALUD

Acuña propone telemedicina con IA e infraestructura hospitalaria. Olivera prioriza la nutrición y la agricultura como determinantes primarios de la salud. Acuña tiene el plan más tecnológico; Olivera tiene el enfoque más orientado a las causas estructurales.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Olivera propone nuevos aeropuertos regionales para el turismo. Acuña supera claramente en escala y especificidad.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Olivera tiene propuestas ambientales sin metas verificables. Ninguno tiene una propuesta ambiental seria.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. Olivera tiene la lucha anticorrupción como bandera histórica con propuesta de eliminar inmunidades y referéndum institucional. La diferencia en credibilidad anticorrupción es sustancial.

## 📊 CONCLUSIÓN TÉCNICA

Acuña tiene el plan más completo en infraestructura, educación y tecnología médica, con mayor presencia electoral. Olivera tiene mayor credibilidad anticorrupción y un enfoque más social basado en la nutrición como motor del desarrollo humano. El principal diferenciador es el historial judicial de Acuña frente al perfil moral más limpio de Olivera.""",

"164:165": """## 💰 ECONOMÍA

López Chau propone descentralización productiva, masificación del gas con tarifa única y plataformas científicas universitarias. Olivera propone reducción progresiva del IGV al 10% hacia 2031 y nuevos aeropuertos regionales. López Chau tiene el plan económico más sofisticado y territorialmen coherente; Olivera tiene propuestas más específicas en reducción tributaria.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen, purga policial meritocrática y modernización tecnológica. Olivera propone reformas institucionales para eliminar la inmunidad de autoridades. Enfoques complementarios — López Chau más específico en modernización policial; Olivera más orientado a la reforma política.

## 📚 EDUCACIÓN

López Chau propone universidades como plataformas científicas, cobertura universal de inicial y mil agrónomos jóvenes. Olivera propone la nutrición como base del aprendizaje. López Chau tiene el plan más moderno y específico; Olivera tiene el enfoque más preventivo y social.

## 🏥 SALUD

López Chau propone integrar sistemas de salud con énfasis en agua potable y saneamiento. Olivera prioriza la nutrición y la agricultura. López Chau tiene el plan más sistémico e integrador.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática para obras y proyectos estratégicos. Olivera propone nuevos aeropuertos regionales para el turismo. López Chau tiene el plan más articulado en infraestructura productiva.

## 🌿 MEDIO AMBIENTE

López Chau propone gestión de agua con cochas y reservorios — propuesta hídrica concreta. Olivera tiene propuestas sin metas verificables. López Chau tiene la propuesta ambiental más pertinente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Chau tiene alta credibilidad anticorrupción personal y propone meritocracia como eje central. Olivera tiene la lucha anticorrupción como bandera histórica con propuesta de eliminar inmunidades. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

López Chau tiene el plan más sofisticado técnicamente en todas las dimensiones. Olivera tiene mayor historia anticorrupción y un enfoque más social basado en la nutrición infantil. Ambos tienen buena credibilidad personal — la comparación refleja la diferencia entre el tecnócrata universitario con plan territorial (López Chau) y el político veterano con bandera moral (Olivera)."""

}

async def insertar_todo():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    print(f"Insertando {len(ANALISIS)} análisis técnicos (grupos 3 y 4 — las 30 restantes)...")

    async with async_session() as db:
        for clave, texto in ANALISIS.items():
            try:
                stmt = pg_insert(CacheAnalisis).values(
                    tipo="analisis_tecnico",
                    clave=clave,
                    contenido=texto
                ).on_conflict_do_update(
                    index_elements=["tipo", "clave"],
                    set_={"contenido": texto}
                )
                await db.execute(stmt)
                print(f"  ✅ {clave}")
            except Exception as e:
                print(f"  ❌ {clave}: {e}")

        await db.commit()

    await engine.dispose()
    print(f"\n🎉 ¡COMPLETADO! Las 55 análisis técnicos están listos en producción.")

asyncio.run(insertar_todo())
