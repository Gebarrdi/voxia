"""
insert_tecnicos_3_10.py — Inserta análisis técnicos #3 al #10
=============================================================
Comparaciones:
  #3  164:166  Fujimori vs López Chau
  #4  166:173  Fujimori vs Sánchez
  #5  168:169  López Aliaga vs Belmont
  #6  164:168  López Aliaga vs López Chau
  #7  164:169  Belmont vs López Chau
  #8  166:167  Fujimori vs Nieto
  #9  168:173  López Aliaga vs Sánchez
  #10 163:166  Fujimori vs Acuña
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

# ── #3: Fujimori (166) vs López Chau (164) ────────────────────────────────
"164:166": """## 💰 ECONOMÍA

Fujimori y López Chau representan dos visiones distintas del liberalismo económico. Fujimori defiende el modelo de libre mercado con disciplina fiscal estricta, buscando reducir el déficit al 1% del PBI, eliminar 500 trámites y atraer USD 5,000–7,000 millones de inversión privada adicional anual mediante digitalización y shock desregulatorio. López Chau apuesta por la descentralización productiva como motor de crecimiento — su lema "Todo el poder a las regiones" implica transformar las regiones en polos exportadores con industria, innovación y ciencia. Propone crecimiento promedio del 6%, déficit bajo el 1% y deuda pública menor al 30% del PBI. Ambos favorecen la inversión privada y la formalización, pero Fujimori tiene un enfoque más limeño-centralista mientras López Chau articula una estrategia territorial más sofisticada. La analista Alejandra Costa del El Comercio destacó a López Chau como uno de los candidatos que sí identificó los problemas económicos del país y propuso soluciones, a diferencia de varios competidores.

## 🔒 SEGURIDAD

Aquí existe una diferencia ideológica importante. Fujimori propone mano dura con participación de las FFAA junto a la PNP, mega penales con trabajo productivo y la controversial medida de retirarse de la Corte Interamericana de Derechos Humanos para reinstaurar jueces sin rostro. López Chau plantea derogar las leyes procrimen, purgar la Policía Nacional con criterio meritocrático, modernizar comisarías con tecnología de inteligencia y crear un sistema de información criminal integrado. Su propuesta también apunta a "cortar las venas financieras" del crimen organizado. López Chau tiene un enfoque más institucionalista y menos punitivo que Fujimori, aunque ambos reconocen la urgencia del problema: el 27% de peruanos han sido víctimas de delitos según el diagnóstico de Fuerza Popular.

## 📚 EDUCACIÓN

Fujimori propone infraestructura educativa masiva, inglés obligatorio con certificación al terminar secundaria, duplicar becas y fortalecer educación cívica. López Chau es más ambicioso: convertir las universidades en plataformas científicas y tecnológicas, garantizar cobertura universal de educación inicial (3–5 años), desplegar mil agrónomos jóvenes con universidades públicas en cada región, y promover la ciudadanía digital desde primaria. López Chau, ex rector de la UNI, tiene mayor credibilidad técnica en este eje dado su historial universitario. Ninguno aborda la crisis docente de fondo ni propone reformas al sistema de evaluación. El rendimiento de Perú en PISA sigue entre los más bajos de la región.

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20%, universalizar vacunación y cerrar el déficit de camas hospitalarias. Su plan reconoce que el Perú invierte menos en salud per cápita que la mayoría de países latinoamericanos. López Chau plantea integrar Minsa, EsSalud, gobiernos regionales y privados en un sistema de cobertura universal efectiva, con énfasis en acceso a agua potable y saneamiento como determinantes primarios de salud. Propone también plataformas digitales de gestión hospitalaria y fortalecimiento del primer nivel de atención. El enfoque de López Chau es más sistémico e integrador; el de Fujimori más focalizado en metas concretas. Ambos carecen de un modelo de financiamiento detallado para la universalización.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros operativos en Lima, metros regionales en Arequipa, Trujillo y Piura, modernización de 17 aeropuertos y pavimentación del 100% de caminos rurales críticos. López Chau propone una entidad autónoma y meritocrática para la ejecución de obras públicas regionales, aceleración de proyectos estratégicos como Chavimochic, Chinecas y Majes Siguas 2, y conectividad física y digital prioritaria para cerrar brechas territoriales. Fujimori tiene propuestas de mayor escala y mayor presencia mediática; López Chau tiene un enfoque más descentralizado y técnicamente más orientado a eliminar la corrupción en la ejecución de obras.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley General de Minería con respeto ambiental y convivencia entre minería y agricultura, sin compromisos climáticos ambiciosos. López Chau incluye una dimensión ambiental con énfasis en gestión de agua mediante cochas, reservorios y siembra-cosecha de agua en microcuencas — una propuesta con alta pertinencia para la adaptación climática en la sierra peruana. Ninguno presenta una estrategia de transición energética seria ni aborda la deforestación amazónica que supera las 200,000 hectáreas anuales. López Chau tiene una propuesta ambiental más concreta y territorialmente pertinente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori propone Shock Anticorrupción Digital con blockchain e IA, criptomoneda estatal para transacciones públicas y plataformas de monitoreo ciudadano. Sin embargo, sus tres procesos penales por lavado de activos vinculados al caso Odebrecht siguen siendo su mayor contradicción. López Chau plantea meritocracia como eje central anticorrupción — "si el presidente es corrupto, todo lo será" —, plataforma digital de seguimiento de obras, impedir el acceso de investigados a cargos públicos, y seguir el modelo de Singapur para eliminar coimas en 48 horas. Su perfil personal es más limpio, aunque su partido Ahora Nación es de reciente fundación y sin historial de gestión.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y López Chau comparten la defensa del libre mercado pero difieren en la profundidad y coherencia de sus propuestas. Fujimori presenta el plan más detallado y ordenado técnicamente, con metas verificables y financiamiento relativamente articulado, pero su historial judicial representa un riesgo institucional serio. López Chau ofrece la propuesta más coherente entre candidatos de centro-derecha: mayor énfasis en descentralización productiva, educación científica, anticorrupción meritocrática y gestión ambiental del agua. Su debilidad es la menor experiencia en gestión ejecutiva y el menor reconocimiento electoral inicial. Técnicamente, el plan de López Chau es superior en coherencia territorial y anticorrupción; el de Fujimori es superior en especificidad macroeconómica y metas cuantificadas.""",

# ── #4: Fujimori (166) vs Sánchez (173) ───────────────────────────────────
"166:173": """## 💰 ECONOMÍA

Esta es la comparación más ideológicamente polarizada del campo electoral peruano 2026. Fujimori defiende el modelo de libre mercado, la Constitución de 1993 y la inversión privada como motores del crecimiento. Su plan busca reducir el déficit fiscal al 1%, atraer USD 5,000–7,000 millones adicionales de inversión privada y digitalizar el 80% de trámites empresariales. Sánchez, por el contrario, propone superar el modelo neoliberal con una economía mixta: el Estado recupera soberanía sobre recursos estratégicos, se aplica un impuesto a las sobreganancias mineras, se establece una presión tributaria del 25% del PBI y se impulsa la industrialización nacional con sustitución de importaciones. Su propuesta incluye reforma constitucional y la posible renegociación de TLCs. El FMI y el BM advierten que modelos de alta intervención estatal sin marcos institucionales sólidos tienden a generar fuga de capitales e inflación en América Latina — casos como Venezuela y Argentina son referentes negativos que Sánchez deberá rebatir. Fujimori tiene el plan más afín al consenso técnico internacional.

## 🔒 SEGURIDAD

Fujimori propone mano dura con tecnología de vigilancia avanzada, participación de FFAA, mega penales y retiro de la CIDH para restablecer jueces sin rostro. Sánchez plantea un enfoque diferente: reestructurar la Policía para eliminar la corrupción institucionalizada, crear un Sistema Nacional Integrado de Información Criminal, y atacar las economías ilegales que financian el crimen organizado. Sánchez ve la inseguridad como síntoma de un Estado capturado por intereses económicos ilegales y propone una reforma estructural del sistema judicial. Fujimori propone más fuerza; Sánchez más inteligencia y reforma institucional. Ninguno de los dos presenta evidencia sobre la efectividad de sus enfoques en contextos similares, aunque el modelo de inteligencia criminal ha mostrado mejores resultados sostenidos en Colombia y Ecuador.

## 📚 EDUCACIÓN

Ambos coinciden en aumentar la inversión educativa y en universalizar el acceso, pero difieren en el modelo. Fujimori propone educación cívica con valores patrióticos, inglés obligatorio, becas y digitalización de colegios. Sánchez propone declarar la educación como derecho fundamental en una nueva Constitución, aumentar el gasto al 6% del PBI, crear el Ministerio de Ciencia y Tecnología, garantizar ingreso libre a la educación superior, salario mínimo de una UIT para docentes y educación intercultural con pertinencia andina y amazónica. El enfoque de Sánchez es más redistributivo e inclusivo; el de Fujimori más orientado a competencias del mercado laboral. Ambos tienen metas ambiciosas cuya viabilidad fiscal debe analizarse.

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20%, invertir en infraestructura hospitalaria y vacunación universal. Sánchez propone implementar Redes Integradas de Salud en todo el territorio, crear un Fondo Financiero Intangible para suministros médicos estratégicos, fortalecer CENARES para distribución hasta postas rurales y reducir el tiempo de espera diagnóstico a 72 horas máximo. El enfoque de Sánchez es más sistémico con metas operativas específicas; el de Fujimori más centrado en indicadores de resultado. Ambos reconocen el fracaso del sistema actual — el 50.5% de la población rural sin acceso a salud según el MINSA — pero proponen caminos muy distintos para resolverlo.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros en Lima, metros regionales, modernización de 17 aeropuertos y pavimentación rural. Sánchez propone intervenir 10,000 km de caminos rurales para reducir costos logísticos en 25%, infraestructura productiva que garantice derechos básicos y protección ante riesgos climáticos. Fujimori tiene propuestas de mayor escala y visibilidad; Sánchez tiene un enfoque más territorial y rural. Ninguno de los dos presenta un plan integral de financiamiento de infraestructura que resuelva la brecha de más de USD 100,000 millones identificada por AFIN.

## 🌿 MEDIO AMBIENTE

Sánchez presenta la propuesta ambiental más ambiciosa del campo electoral: transición ecológica justa con empleo verde, economía circular, valor agregado nacional en recursos naturales y compromisos con los derechos de comunidades indígenas. Propone además la prohibición gradual de exportar minerales sin procesamiento. Fujimori propone modernizar la Ley General de Minería con respeto ambiental, sin compromisos climáticos específicos. El Perú pierde 200,000 hectáreas de bosques anuales y tiene NDC que requieren reducir emisiones en 30% al 2030 — la propuesta de Sánchez es más consistente con estos compromisos, aunque su viabilidad económica enfrenta tensiones con la dependencia fiscal del sector extractivo.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori propone blockchain, IA y criptomoneda estatal para transparentar el Estado, pero sus tres procesos penales vinculados al caso Odebrecht signan su credibilidad. Sánchez propone una nueva Constitución con veedurías ciudadanas, control social y reforma del sistema judicial para eliminar la captura del Estado por poderes fácticos. Su asociación con el gobierno de Pedro Castillo — como ministro de Comercio Exterior 2021-2022 — y su promesa de indultarlo generan dudas sobre su independencia y criterio institucional. Ambos candidatos tienen pasivos anticorrupción significativos, aunque de naturaleza distinta.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y Sánchez representan los polos de la polarización peruana: libre mercado versus economía mixta, orden versus justicia social, continuidad institucional versus reforma constitucional. Fujimori tiene el plan más articulado técnicamente en macroeconomía y el más alineado con el consenso del FMI y BM, pero su historial judicial es su mayor lastre. Sánchez tiene el plan más coherente en salud, educación pública y medio ambiente, con mayor sensibilidad territorial e intercultural, pero su propuesta económica genera incertidumbre sobre la inversión privada y la estabilidad macroeconómica. La elección entre ambos implica un trade-off entre estabilidad económica con riesgo institucional (Fujimori) y transformación social con riesgo económico (Sánchez). Ninguno resuelve de manera convincente la crisis de seguridad ni presenta un plan ambiental con financiamiento realista.""",

# ── #5: López Aliaga (168) vs Belmont (169) ───────────────────────────────
"168:169": """## 💰 ECONOMÍA

López Aliaga y Belmont comparten el rechazo a los monopolios y la defensa de la economía de mercado, pero desde posiciones distintas. López Aliaga propone una reforma tributaria agresiva: unificar todos los regímenes en uno amigable para emprendedores, reducir el IGV, crear el Banco Pyme, alcanzar el 7% de crecimiento del PBI y generar 2 millones de empleos mediante industrialización y zonas francas. Belmont propone una economía social de mercado con "rostro humano", rechazando monopolios y oligopolios, y centrado en el Plan Choque de Reactivación: completar 1,500 obras paralizadas, formalizar el 100% de trabajadores en obras estatales y crear 100 plantas de procesamiento regional. También plantea renegociar contratos de empresas estratégicas y cuestionar el modelo de concesiones de peajes. López Aliaga tiene una propuesta macroeconómica más sofisticada; Belmont tiene una propuesta de ejecución más concreta y pragmática.

## 🔒 SEGURIDAD

López Aliaga presenta las propuestas más disruptivas: Central de Lucha contra la Corrupción con poderes plenos de infiltración, penales de alta montaña sin señal móvil, Comando Unificado 'Las Palmas' integrando inteligencia militar y policial, y convenio con Estados Unidos para extradición de cabecillas. Belmont propone reestructurar integralmente PNP, MP, INPE y Poder Judicial con énfasis en percepción ciudadana y eficiencia judicial — meta de resolver el 50% de denuncias. Belmont vincula la seguridad directamente con la ética pública de las autoridades. El enfoque de López Aliaga es más punitivo e innovador; el de Belmont más institucionalista y sistémico. Ninguno presenta evidencia comparada robusta de efectividad.

## 📚 EDUCACIÓN

López Aliaga plantea incluir Libertad Financiera, Emprendimiento y Chino Mandarín en secundaria, internet satelital y tablets para todas las escuelas, y crear parques tecnológicos que atraigan empresas globales. Belmont propone educación pública gratuita y obligatoria con énfasis en deporte, valores y folklore, y reducir la deserción escolar rural al 5% en cinco años. Su lema "Obras sí, palabras no" se refleja en priorizar infraestructura educativa concreta antes que reformas curriculares. López Aliaga tiene una visión más orientada al mercado laboral global; Belmont tiene una visión más culturalista y comunitaria. Ninguno propone reformas de fondo al sistema docente ni aborda los resultados PISA.

## 🏥 SALUD

López Aliaga propone transformar EsSalud en entidad técnica autónoma con gestión meritocrática, medicamentos genéricos obligatorios en farmacias y dotación de personal en postas rurales. Belmont propone elevar la cobertura de salud al 85% en cinco años, rehabilitar la mitad de los puestos de salud rurales, construir 50 nuevos establecimientos y reducir la desnutrición infantil al 10%. Belmont tiene metas más específicas y territorialmente focalizadas en zonas vulnerables; López Aliaga tiene un enfoque más institucional y de gestión. Ambos reconocen la crisis del sistema de salud peruano pero proponen caminos distintos para resolverla.

## 🚆 TRANSPORTE

López Aliaga presenta las propuestas más innovadoras: trenes de alta velocidad Lima-Ica y Lima-Trujillo, túnel trasandino, y zonas francas para turismo e industria. También propone el desarrollo de la industria del litio en Puno. Belmont propone intervenir 10,000 km de caminos rurales, invertir en puertos, aeropuertos e hidroeléctricas bajo supervisión estricta, y cuestiona el modelo de concesiones de peajes que encarece los alimentos. López Aliaga tiene propuestas de mayor escala y ambición; Belmont tiene propuestas más ejecutables en el corto plazo y con mayor sensibilidad hacia las zonas rurales.

## 🌿 MEDIO AMBIENTE

López Aliaga menciona el desarrollo de la industria del litio en Puno y las zonas francas industriales, sin una agenda ambiental definida. Belmont incluye una dimensión territorial-ambiental con énfasis en ordenamiento del territorio y desarrollo sostenible, y se niega a vender más empresas estratégicas del Estado. Ninguno de los dos tiene una propuesta ambiental sólida. López Aliaga prioriza el crecimiento industrial; Belmont prioriza la soberanía sobre recursos. Ninguno aborda la deforestación ni presenta compromisos climáticos específicos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, trazabilidad blockchain para el 100% de contrataciones, eliminación del financiamiento estatal a partidos y prohibición del transfuguismo. Su credibilidad anticorrupción personal es mayor que la de Fujimori, aunque Renovación Popular recibió aportes de constructoras brasileñas y López Aliaga enfrenta cuestionamientos por presunta deuda tributaria con la SUNAT. Belmont propone la imprescriptibilidad de delitos de corrupción, plataforma digital de obras con rendición de cuentas trimestral y revocatoria como mecanismo de control. Su historial personal es más limpio, aunque su gestión como alcalde de Lima tuvo cuestionamientos sobre ejecución presupuestal.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga y Belmont son los dos outsiders más conocidos del campo electoral 2026 — ambos empresarios mediáticos con experiencia en Lima. López Aliaga tiene las propuestas más ambiciosas e innovadoras, especialmente en transporte, tributación y anticorrupción, con mayor sofisticación técnica y mayor credibilidad en seguridad. Belmont tiene las propuestas más pragmáticas y ejecutables en el corto plazo, con mayor sensibilidad hacia la salud rural y la desnutrición infantil, y un historial personal anticorrupción más limpio. La diferencia fundamental es que López Aliaga apuesta por transformaciones estructurales profundas con alto riesgo de implementación, mientras Belmont apuesta por obras concretas y mejoras graduales con menor riesgo institucional. Ninguno de los dos tiene un plan ambiental serio.""",

# ── #6: López Aliaga (168) vs López Chau (164) ────────────────────────────
"164:168": """## 💰 ECONOMÍA

López Aliaga y López Chau comparten el apellido pero representan visiones económicas distintas dentro del espectro liberal. López Aliaga propone una reforma tributaria agresiva — unificar regímenes, reducir el IGV, crear el Banco Pyme — con la meta de alcanzar el 7% de crecimiento del PBI y 2 millones de empleos mediante industrialización y zonas francas. López Chau apuesta por la descentralización productiva como motor principal: "Todo el poder a las regiones" implica transformar las regiones en polos exportadores con cadenas de valor, innovación y ciencia. Propone crecimiento promedio del 6% y déficit bajo el 1%. Ambos defienden la inversión privada, pero López Aliaga tiene un enfoque más centralizado en reformas tributarias nacionales mientras López Chau tiene un modelo territorial más sofisticado. La analista económica Alejandra Costa del El Comercio destacó a López Chau como uno de los pocos candidatos con propuestas económicas serias, junto a Fujimori y Pérez Tello.

## 🔒 SEGURIDAD

López Aliaga presenta las propuestas más disruptivas: Central de Lucha contra la Corrupción con poderes plenos, penales de alta montaña sin cobertura móvil, Comando Unificado 'Las Palmas' y convenio con Estados Unidos para extradición. López Chau plantea derogar leyes procrimen, purgar la Policía con criterio meritocrático, modernizar comisarías con inteligencia y atacar las economías ilegales que financian el crimen. López Aliaga tiene propuestas más dramáticas e innovadoras; López Chau tiene un enfoque más institucionalista y menos punitivo. Ambos reconocen que el 84% de peruanos se siente inseguro, pero difieren en los instrumentos de respuesta.

## 📚 EDUCACIÓN

López Aliaga plantea incluir Libertad Financiera, Emprendimiento y Chino Mandarín en secundaria, internet satelital y parques tecnológicos. López Chau es más ambicioso: convertir universidades en plataformas científicas, garantizar cobertura universal de inicial, desplegar mil agrónomos jóvenes con universidades públicas en cada región, y promover ciudadanía digital desde primaria. López Chau, ex rector de la UNI, tiene mayor credibilidad técnica y un plan educativo más coherente y sistémico. López Aliaga tiene una visión más orientada al emprendimiento y al mercado global.

## 🏥 SALUD

López Aliaga propone transformar EsSalud en entidad técnica autónoma con gestión meritocrática, medicamentos genéricos obligatorios y dotación de personal en postas. López Chau plantea integrar Minsa, EsSalud y gobiernos regionales en un sistema de cobertura universal efectiva, con énfasis en agua potable y saneamiento como determinantes primarios de salud. El enfoque de López Chau es más sistémico e integrador; el de López Aliaga más centrado en la eficiencia de las instituciones existentes. Ambos carecen de un modelo de financiamiento universal detallado.

## 🚆 TRANSPORTE

López Aliaga presenta las propuestas más disruptivas: trenes de alta velocidad Lima-Ica y Lima-Trujillo, túnel trasandino y desarrollo del litio en Puno. López Chau propone una entidad autónoma meritocrática para obras regionales y aceleración de proyectos estratégicos como Chavimochic, Chinecas y Majes Siguas 2. López Aliaga tiene propuestas de mayor visibilidad y escala; López Chau tiene un enfoque más descentralizado y menos susceptible a la corrupción en la ejecución de obras.

## 🌿 MEDIO AMBIENTE

López Aliaga prioriza el desarrollo del litio y las zonas francas industriales, con una agenda ambiental secundaria. López Chau incluye una dimensión ambiental más concreta: gestión de agua mediante cochas y reservorios, siembra y cosecha de agua en microcuencas, y énfasis en la adaptación climática de la sierra. La propuesta de López Chau es más pertinente para la realidad hídrica peruana, especialmente considerando que el 43% de la población rural carece de agua potable según el INEI.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, trazabilidad blockchain para contrataciones y eliminación del financiamiento estatal a partidos. Sus cuestionamientos por presunta deuda tributaria con la SUNAT y los aportes de constructoras brasileñas a Renovación Popular son sus principales pasivos. López Chau plantea meritocracia como eje central anticorrupción, plataforma digital de seguimiento de obras y el modelo de Singapur para eliminar coimas en 48 horas. Su perfil personal es más limpio y su propuesta anticorrupción más estructural.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga y López Chau son los dos candidatos más técnicamente solventes del espectro de centro-derecha, aunque con estilos muy distintos. López Aliaga ofrece las propuestas más disruptivas e innovadoras — especialmente en seguridad, transporte y tributación — con mayor presencia mediática y mayor capacidad de movilización electoral. López Chau ofrece el plan más coherente técnicamente en educación, economía descentralizada, anticorrupción y gestión ambiental del agua, con mayor credibilidad personal e institucional. La diferencia principal: López Aliaga apuesta por reformas radicales de alto impacto y alto riesgo; López Chau apuesta por reformas sistémicas graduales con mayor sostenibilidad institucional.""",

# ── #7: Belmont (169) vs López Chau (164) ─────────────────────────────────
"164:169": """## 💰 ECONOMÍA

Belmont y López Chau representan dos versiones del pragmatismo económico peruano. Belmont propone una economía social de mercado con "rostro humano", rechazando monopolios y oligopolios, con el Plan Choque de Reactivación como medida estrella: completar 1,500 obras paralizadas, formalizar el 100% de trabajadores en obras estatales y crear 100 plantas de procesamiento regional. También propone renegociar contratos de empresas estratégicas. López Chau apuesta por "Todo el poder a las regiones" como eje transformador: descentralización productiva, industrialización regional, masificación del gas con tarifa única nacional y conversión de universidades en plataformas de innovación. Propone crecimiento promedio del 6% con déficit bajo el 1%. López Chau tiene un modelo económico más elaborado y con mayor coherencia territorial; Belmont tiene propuestas más ejecutables en el corto plazo.

## 🔒 SEGURIDAD

Belmont propone reestructurar PNP, MP, INPE y Poder Judicial, resolver el 50% de denuncias y elevar en 15 puntos la percepción de seguridad. Su enfoque vincula la inseguridad con la ética pública. López Chau plantea derogar leyes procrimen, purgar la Policía con meritocracia, modernizar comisarías con tecnología de inteligencia y atacar las economías ilegales. Ambos tienen enfoques institucionalistas, aunque López Chau es más específico en los instrumentos. Ninguno propone la militarización de la seguridad pública ni medidas de mano dura extrema, lo que los diferencia de Fujimori y López Aliaga.

## 📚 EDUCACIÓN

Belmont propone educación pública gratuita y obligatoria, reducción de la deserción escolar rural al 5% y reincorporación del deporte, valores y folklore al currículo. López Chau propone cobertura universal de educación inicial, convertir universidades en plataformas científicas, desplegar mil agrónomos jóvenes y promover ciudadanía digital. López Chau, ex rector de la UNI, tiene mayor credibilidad y profundidad en el eje educativo. Belmont tiene un enfoque más culturalista y comunitario, con énfasis en valores y pertinencia local.

## 🏥 SALUD

Belmont propone elevar cobertura de salud al 85% en cinco años, rehabilitar puestos rurales, construir 50 nuevos establecimientos y reducir la desnutrición infantil al 10%. Sus metas son específicas y territorialmente focalizadas. López Chau propone integrar Minsa, EsSalud y gobiernos regionales en un sistema de cobertura universal, con énfasis en agua potable y saneamiento. El enfoque de Belmont es más operativo con metas claras; el de López Chau es más sistémico e integrador. Ambos reconocen la crisis del sistema de salud pero tienen diferentes horizontes de implementación.

## 🚆 TRANSPORTE

Belmont propone intervenir 10,000 km de caminos rurales, invertir en puertos y aeropuertos bajo supervisión estricta, y cuestionar el modelo de concesiones de peajes. López Chau propone una entidad autónoma meritocrática para obras regionales y acelerar proyectos estratégicos como Chavimochic y Majes Siguas 2. Ambos tienen un enfoque más descentralizado que Fujimori o López Aliaga. Belmont tiene mayor credibilidad en obras urbanas por su experiencia como alcalde de Lima; López Chau tiene una visión regional más integral.

## 🌿 MEDIO AMBIENTE

Belmont incluye una dimensión territorial-ambiental con énfasis en ordenamiento del territorio y desarrollo sostenible, y se opone a la privatización de recursos estratégicos. López Chau tiene la propuesta hídrica más concreta: cochas, reservorios y siembra-cosecha de agua en microcuencas. Ninguno presenta compromisos climáticos específicos ni estrategia de transición energética. La propuesta de López Chau es más pertinente para la realidad hídrica peruana.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Belmont propone la imprescriptibilidad de delitos de corrupción, plataforma digital de obras con rendición de cuentas trimestral y revocatoria como mecanismo de control. Su historial personal es relativamente limpio. López Chau plantea meritocracia como eje anticorrupción, plataforma digital de seguimiento de obras, impedir el acceso de investigados a cargos públicos y el modelo de Singapur. Ambos tienen mayor credibilidad anticorrupción que Fujimori, y ninguno arrastra investigaciones penales relevantes.

## 📊 CONCLUSIÓN TÉCNICA

Belmont y López Chau son los candidatos más centrados y menos polarizantes del campo electoral 2026. Belmont ofrece el plan más concreto y ejecutable en obras, salud rural y reducción de desnutrición, con mayor credibilidad en gestión urbana y local. López Chau ofrece el plan más coherente técnicamente en educación científica, economía descentralizada y anticorrupción, con mayor sofisticación programática y pertinencia territorial. La diferencia fundamental es que Belmont apuesta por resultados tangibles y rápidos en los primeros años de gobierno, mientras López Chau apuesta por transformaciones estructurales de mayor alcance y horizonte temporal más largo.""",

# ── #8: Fujimori (166) vs Nieto (167) ─────────────────────────────────────
"166:167": """## 💰 ECONOMÍA

Fujimori defiende el libre mercado con disciplina fiscal estricta — reducir el déficit al 1% del PBI, digitalizar el 80% de trámites y atraer USD 5,000–7,000 millones de inversión privada adicional. Nieto propone la creación de un Fondo Soberano de Riqueza, crecimiento anual del 5%, presión tributaria del 18% y reducción de la informalidad laboral al 50% mediante diversificación productiva y transición ecológica. Ambos defienden la inversión privada, pero Nieto tiene una visión más keynesiana con énfasis en la diversificación productiva y la economía circular, mientras Fujimori es más ortodoxa en su defensa del libre mercado y la disciplina fiscal. El Fondo Soberano de Riqueza de Nieto es una propuesta innovadora que países como Chile y Noruega han implementado con éxito para gestionar la renta de recursos naturales.

## 🔒 SEGURIDAD

Fujimori propone mano dura con participación de FFAA, videovigilancia avanzada, mega penales y el retiro de la CIDH para reinstaurar jueces sin rostro. Nieto plantea la derogación inmediata de las leyes procrimen — lo que Nieto señaló directamente en el debate, acusando a Fujimori de haberlas aprobado desde el Congreso — junto con una reforma institucional integral del sistema de seguridad y justicia. Nieto tiene mayor credibilidad técnica en reforma institucional dado su experiencia como ministro del gobierno PPK. En el debate, Nieto fue uno de los candidatos más directos en cuestionar a Fujimori por estas leyes, generando uno de los momentos más tensos de la campaña.

## 📚 EDUCACIÓN

Fujimori propone inglés obligatorio con certificación, becas, infraestructura educativa y educación cívica con valores patrióticos. Nieto propone universalizar la conectividad digital educativa, fortalecer la innovación, reformar el currículo con competencias del siglo XXI e invertir en formación docente continua. Nieto tiene una visión más tecnocrática y orientada a la reforma educativa sistémica; Fujimori tiene una visión más enfocada en infraestructura y competencias específicas. Ninguno propone una reforma de fondo al sistema de evaluación docente.

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20%, universalizar vacunación e invertir en infraestructura hospitalaria. Nieto propone universalizar la salud integrando los sistemas existentes, con atención especial a la reducción de la anemia y la mortalidad materna, y una estrategia de salud preventiva más articulada. Nieto tiene un plan de salud más sistémico e integrador que Fujimori, aunque ambos reconocen que el Perú es uno de los países con menor gasto per cápita en salud de la región. La credibilidad técnica de Nieto en este eje es respaldada por su experiencia gubernamental.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros en Lima, metros regionales, modernización de 17 aeropuertos y pavimentación rural. Nieto propone fortalecer la inversión pública en infraestructura vial y logística con énfasis en descentralización y cierre de brechas territoriales. Fujimori tiene propuestas de mayor escala y especificidad; Nieto tiene un enfoque más orientado a la equidad territorial y la reducción de costos logísticos rurales.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley General de Minería con respeto ambiental, sin compromisos climáticos ambiciosos. Nieto incluye transición ecológica, economía circular y desarrollo industrial regional sostenible como ejes transversales de su plan, siendo uno de los candidatos con mayor coherencia entre crecimiento económico y sostenibilidad ambiental. La propuesta de Nieto es más consistente con los compromisos NDC del Perú para 2030.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori propone Shock Anticorrupción Digital con blockchain e IA, pero sus tres procesos penales por Odebrecht signan su credibilidad. Nieto propone reformas institucionales profundas con mecanismos de control ciudadano, respaldado por una trayectoria ministerial sin investigaciones penales relevantes. Su credibilidad anticorrupción es sustancialmente mayor que la de Fujimori. En el debate, Nieto cuestionó directamente a Fujimori por haber "gobernado desde el Congreso", en referencia al control que Fuerza Popular ejerció sobre el Legislativo 2016-2020.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y Nieto representan dos versiones de la centroderecha técnica peruana. Fujimori tiene el plan más detallado en términos macroeconómicos, con metas verificables y mayor presencia electoral, pero su historial judicial es su mayor lastre. Nieto ofrece el plan más coherente entre crecimiento y sostenibilidad, con mayor credibilidad anticorrupción y mayor profundidad en reforma institucional, respaldado por su experiencia como ministro PPK. Su debilidad es el menor reconocimiento electoral y la ausencia de una maquinaria partidaria consolidada. Técnicamente, el plan de Nieto es superior en coherencia programática, sostenibilidad ambiental y credibilidad anticorrupción; el de Fujimori es superior en especificidad macroeconómica y presencia electoral.""",

# ── #9: López Aliaga (168) vs Sánchez (173) ───────────────────────────────
"168:173": """## 💰 ECONOMÍA

Esta es la confrontación ideológica más radical del campo electoral en términos económicos. López Aliaga propone la más agresiva reforma pro-mercado: unificar regímenes tributarios, reducir el IGV, crear el Banco Pyme, alcanzar el 7% de crecimiento del PBI con 2 millones de empleos y desarrollar zonas francas e industria del litio. Sánchez propone exactamente lo contrario: superar el modelo neoliberal, recuperar soberanía sobre recursos estratégicos, aplicar impuesto a sobreganancias mineras, elevar la presión tributaria al 25% del PBI y promover la economía mixta con industrialización nacional. El debate López Aliaga-Sánchez representa el eje más polarizado de la elección 2026, comparable a la polarización Fujimori-Humala de 2011. Economistas del BM y el FMI respaldan en mayor medida el enfoque de López Aliaga; economistas heterodoxos como Epifanio Baca del CIES señalan que el modelo extractivo sin industrialización perpetúa la dependencia.

## 🔒 SEGURIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, penales de alta montaña, Comando Unificado 'Las Palmas' y convenio con EEUU para extradición de cabecillas criminales. Sánchez plantea reestructurar la Policía para eliminar la corrupción institucionalizada, crear un Sistema Nacional Integrado de Información Criminal y atacar las economías ilegales que financian el crimen organizado. López Aliaga tiene el enfoque más punitivo e innovador; Sánchez tiene el enfoque más estructural y enfocado en las causas económicas del crimen. Ambos reconocen que la inseguridad es el principal problema del Perú, pero proponen caminos radicalmente distintos.

## 📚 EDUCACIÓN

López Aliaga propone Chino Mandarín, Libertad Financiera e internet satelital para escuelas. Sánchez propone declarar la educación como derecho fundamental en la nueva Constitución, aumentar el gasto al 6% del PBI, salario mínimo de 1 UIT para docentes, ingreso libre a la educación superior y educación intercultural con pertinencia andina y amazónica. Sánchez tiene el plan educativo más redistributivo e inclusivo; López Aliaga tiene el plan más orientado al mercado laboral global. La diferencia de modelo es profunda: López Aliaga forma emprendedores para el mercado; Sánchez forma ciudadanos para la democracia.

## 🏥 SALUD

López Aliaga propone transformar EsSalud en entidad técnica autónoma con meritocracia y medicamentos genéricos obligatorios. Sánchez propone Redes Integradas de Salud en todo el territorio, Fondo Financiero Intangible para suministros médicos, tiempo máximo de espera de 72 horas para diagnósticos y reducción de la anemia infantil a menos del 20%. Sánchez tiene el plan de salud más sistémico y con mayor cobertura territorial; López Aliaga tiene un plan más enfocado en eficiencia de las instituciones existentes.

## 🚆 TRANSPORTE

López Aliaga propone trenes de alta velocidad Lima-Ica y Lima-Trujillo, túnel trasandino y zonas francas industriales. Sánchez propone intervenir 10,000 km de caminos rurales para reducir costos logísticos en 25%, infraestructura productiva que proteja ante riesgos climáticos y conectividad para comunidades rurales. López Aliaga tiene propuestas de mayor escala y visibilidad; Sánchez tiene un enfoque más rural y equitativo territorialmente.

## 🌿 MEDIO AMBIENTE

Sánchez presenta la propuesta ambiental más ambiciosa: transición ecológica justa, economía circular, prohibición gradual de exportar minerales sin procesamiento, compromisos con derechos de comunidades indígenas y empleo verde. López Aliaga menciona el desarrollo del litio en Puno y las zonas francas industriales, con una agenda ambiental secundaria. La propuesta de Sánchez es más consistente con los NDC del Perú para 2030, pero genera incertidumbre sobre la inversión privada en el sector extractivo que financia el 60% del presupuesto público.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, blockchain para contrataciones y eliminación del financiamiento estatal a partidos. Sus cuestionamientos por presunta deuda tributaria con la SUNAT y aportes de constructoras a Renovación Popular son sus principales pasivos. Sánchez propone una nueva Constitución con veedurías ciudadanas, control social y reforma judicial. Su asociación con el gobierno de Pedro Castillo y su promesa de indultarlo generan dudas sobre su criterio institucional y su independencia de los poderes fácticos de izquierda.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga y Sánchez representan los extremos ideológicos más definidos del campo electoral 2026. López Aliaga ofrece el plan pro-mercado más ambicioso con propuestas innovadoras en seguridad, transporte y tributación, pero con menor sensibilidad social y ambiental. Sánchez ofrece el plan más redistributivo e inclusivo con mayor coherencia ambiental y social, pero con mayor riesgo macroeconómico y menor certidumbre para la inversión privada. La elección entre ambos implica un trade-off radical: estabilidad económica pro-mercado versus justicia social con reforma constitucional. Ninguno de los dos tiene el perfil de gobernabilidad amplia que el Perú necesita para salir de su crisis institucional.""",

# ── #10: Fujimori (166) vs Acuña (163) ────────────────────────────────────
"163:166": """## 💰 ECONOMÍA

Fujimori y Acuña comparten la defensa del libre mercado y la inversión privada, pero proponen rutas distintas. Fujimori prioriza la disciplina fiscal con la meta de reducir el déficit al 1% del PBI, eliminar 500 trámites administrativos y atraer USD 5,000–7,000 millones de inversión privada adicional mediante digitalización avanzada. Acuña apuesta por la inversión masiva en infraestructura — un portafolio de 72 proyectos con S/143 mil millones de inversión — y el fortalecimiento del sector minero y petrolero con miras a duplicar el PBI de hidrocarburos. También propone formalizar las MYPES y crear el Ministerio de Infraestructura. Ambos tienen metas económicas ambiciosas, pero Fujimori tiene un plan más equilibrado entre inversión y disciplina fiscal; Acuña tiene un plan más centrado en infraestructura física como motor del crecimiento.

## 🔒 SEGURIDAD

Fujimori propone mano dura con FFAA y PNP, modernización tecnológica, mega penales y retiro de la CIDH para reinstaurar jueces sin rostro. Acuña plantea crear el Comando Nacional contra la Extorsión y el Sicariato e incorporar 5,000 nuevos efectivos policiales especializados en inteligencia, además de fortalecer fiscalías y juzgados. Ambos tienen enfoques similares en lo punitivo, aunque Fujimori presenta un plan más detallado tecnológicamente. Ninguno propone una estrategia integral de prevención social del delito que aborde las causas estructurales de la violencia.

## 📚 EDUCACIÓN

Fujimori propone inglés obligatorio con certificación, duplicar becas y cerrar brechas de infraestructura educativa. Acuña propone reestructurar el MINEDU, incluir inglés e IA en el currículo, construir un COAR por región e implementar el programa ILA — internet, luz y agua — para escuelas públicas. Acuña, como fundador y presidente de la Universidad César Vallejo, tiene mayor experiencia en educación superior, aunque su institución ha sido cuestionada por su calidad académica. Ambos priorizan la conectividad digital, pero ninguno aborda la reforma docente de fondo.

## 🏥 SALUD

Fujimori propone reducir la anemia infantil al 20%, universalizar vacunación e invertir en infraestructura hospitalaria. Acuña propone telemedicina con IA, infraestructura hospitalaria vía APP y cobertura de aseguramiento casi universal con 95% de abastecimiento de medicamentos. Ambos tienen propuestas similares en alcance, aunque Acuña tiene mayor énfasis en tecnología médica y Fujimori en la reducción de indicadores específicos. Ninguno presenta un modelo de financiamiento integral para universalizar la salud.

## 🚆 TRANSPORTE

Fujimori propone cuatro metros en Lima, metros regionales en Arequipa, Trujillo y Piura, modernización de 17 aeropuertos y pavimentación del 100% de caminos rurales críticos. Acuña propone un portafolio de 72 proyectos de infraestructura con inversión de S/143 mil millones y entrega de maquinaria a las 196 provincias del país. Acuña tiene las propuestas de infraestructura más ambiciosas en términos de escala; Fujimori tiene las propuestas más específicas y técnicamente articuladas. Ambos reconocen que la brecha de infraestructura supera los USD 100,000 millones según AFIN.

## 🌿 MEDIO AMBIENTE

Fujimori propone modernizar la Ley General de Minería con respeto ambiental y convivencia entre minería y agricultura. Acuña prioriza la expansión minera y petrolera — duplicar el PBI de hidrocarburos — lo que genera tensiones directas con la agenda ambiental. Ninguno de los dos tiene un plan ambiental sólido. Acuña tiene la propuesta más pro-extractivista del campo electoral, mientras Fujimori al menos menciona la compatibilidad minería-agricultura.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Fujimori propone Shock Anticorrupción Digital con blockchain e IA, pero enfrenta tres procesos penales por Odebrecht. Acuña propone IA y programas de integridad obligatorios, pero enfrenta 132 investigaciones fiscales activas, incluyendo acusación formal presentada el 31 de marzo de 2025, y el caso Odebrecht donde un colaborador señaló que recibió USD 50,000 de la red corrupta. Ambos candidatos tienen graves antecedentes que contradicen sus propuestas anticorrupción. La credibilidad de Acuña en este eje es aún menor que la de Fujimori dado el mayor número y gravedad de sus investigaciones.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori y Acuña son los dos candidatos con mayor experiencia electoral del campo 2026, ambos con bases regionales consolidadas y capacidad de movilización. Fujimori presenta el plan más detallado y técnicamente articulado en macroeconomía, seguridad y anticorrupción digital, con metas verificables. Acuña presenta el plan más ambicioso en infraestructura y mayor experiencia en gestión municipal y regional, pero con el perfil anticorrupción más cuestionado del campo electoral. Ambos defienden el libre mercado y la inversión privada, con diferencias en énfasis: Fujimori en digitalización y disciplina fiscal; Acuña en infraestructura física y expansión extractiva. El mayor diferenciador no es programático sino biográfico: Acuña arrastra más investigaciones activas que cualquier otro candidato del campo."""

}

# ── Insertar en DB ─────────────────────────────────────────────────────────

async def insertar_todo():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    print(f"Insertando {len(ANALISIS)} análisis técnicos...")

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
    print(f"\n🎉 ¡Listo! {len(ANALISIS)} análisis técnicos insertados en producción.")


asyncio.run(insertar_todo())
