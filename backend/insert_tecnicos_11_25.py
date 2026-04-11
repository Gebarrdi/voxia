"""
insert_tecnicos_11_25.py — Análisis técnicos grupo 2 (15 comparaciones)
========================================================================
  #11  163:167  Acuña vs Nieto
  #12  163:168  Acuña vs López Aliaga
  #13  163:169  Acuña vs Belmont
  #14  163:170  Acuña vs Luna Gálvez
  #15  163:171  Acuña vs Álvarez
  #16  163:172  Acuña vs Pérez Tello
  #17  163:173  Acuña vs Sánchez
  #18  164:167  López Chau vs Nieto
  #19  164:170  López Chau vs Luna Gálvez
  #20  164:171  López Chau vs Álvarez
  #21  164:172  López Chau vs Pérez Tello
  #22  164:173  López Chau vs Sánchez
  #23  165:166  Olivera vs Fujimori
  #24  165:167  Olivera vs Nieto
  #25  165:168  Olivera vs López Aliaga
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

"163:167": """## 💰 ECONOMÍA

Acuña propone inversión masiva en infraestructura con S/143 mil millones en 72 proyectos, expansión minera y petrolera para duplicar el PBI de hidrocarburos, y formalización de MYPES. Nieto propone un Fondo Soberano de Riqueza, crecimiento anual del 5%, presión tributaria del 18% y reducción de la informalidad al 50% mediante diversificación productiva, transición ecológica y economía circular. Nieto tiene el plan económico más sofisticado técnicamente de los dos, con mayor énfasis en diversificación y sostenibilidad; Acuña tiene un plan más centrado en infraestructura física y expansión extractiva. La analista Alejandra Costa del El Comercio señaló que Nieto es uno de los candidatos que sí identificó los problemas económicos del país y propuso soluciones concretas.

## 🔒 SEGURIDAD

Acuña plantea el Comando Nacional contra la Extorsión y el Sicariato, incorporar 5,000 efectivos policiales especializados y fortalecer fiscalías y juzgados. Nieto propone derogar las leyes procrimen — cuestionando directamente a Fujimori y al bloque parlamentario que las aprobó — reforma institucional integral y mejorar la coordinación entre fuerzas del orden. Nieto tiene mayor credibilidad técnica en reforma institucional dado su trayectoria ministerial PPK; Acuña tiene propuestas más operativas pero menos sistémicas.

## 📚 EDUCACIÓN

Acuña propone reestructurar el MINEDU, incluir inglés e IA en el currículo, construir un COAR por región e implementar el programa ILA. Nieto propone universalizar conectividad digital, reformar el currículo con competencias del siglo XXI y mejorar la formación docente continua. Nieto tiene un plan más sistémico y orientado a la calidad; Acuña tiene un plan más orientado a la infraestructura y equipamiento. Ninguno aborda la crisis docente de fondo ni propone reformas al sistema de evaluación.

## 🏥 SALUD

Acuña propone telemedicina con IA, infraestructura hospitalaria vía APP y 95% de abastecimiento de medicamentos. Nieto propone integrar los sistemas de salud existentes con especial atención a la anemia y mortalidad materna, con una estrategia preventiva más articulada. Ambos reconocen la crisis del sistema, pero Nieto tiene un enfoque más integral mientras Acuña apuesta más por la tecnología médica.

## 🚆 TRANSPORTE

Acuña propone el portafolio más ambicioso en infraestructura: 72 proyectos con S/143 mil millones y maquinaria para las 196 provincias. Nieto propone fortalecer la inversión pública en infraestructura vial y logística con énfasis en equidad territorial. Acuña tiene propuestas de mayor escala; Nieto tiene un enfoque más descentralizado y menos susceptible a obras faraónicas sin impacto real.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión minera y petrolera, generando tensiones directas con la agenda ambiental. Nieto incluye transición ecológica, economía circular y desarrollo industrial regional sostenible como ejes transversales, siendo uno de los candidatos con mayor coherencia ambiental. La propuesta de Nieto es más consistente con los compromisos NDC del Perú para 2030.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales activas y es señalado por Odebrecht. Nieto tiene el perfil anticorrupción más limpio del campo electoral, con propuestas de reforma institucional profunda y mecanismos de control ciudadano respaldados por su trayectoria ministerial. La diferencia en credibilidad anticorrupción entre ambos es sustancial.

## 📊 CONCLUSIÓN TÉCNICA

Nieto tiene el plan técnicamente superior en coherencia programática, sostenibilidad ambiental y credibilidad anticorrupción. Acuña tiene mayor capacidad de movilización electoral y propuestas de infraestructura más ambiciosas, pero arrastra el mayor número de investigaciones fiscales del campo electoral. Si la decisión fuera estrictamente programática, Nieto gana claramente; si la decisión incluye viabilidad electoral y maquinaria política, Acuña tiene ventaja.""",

"163:168": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva con 72 proyectos y expansión extractiva; López Aliaga propone reforma tributaria agresiva — unificar regímenes, reducir IGV, Banco Pyme — con meta de 7% de crecimiento y 2 millones de empleos. Ambos defienden el libre mercado y la inversión privada, pero López Aliaga tiene un plan macroeconómico más sofisticado con metas específicas; Acuña tiene un plan más centrado en infraestructura física.

## 🔒 SEGURIDAD

López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, penales de alta montaña, Comando 'Las Palmas' y convenio con EEUU para extradición. Acuña plantea el Comando Nacional contra el Sicariato y 5,000 nuevos efectivos especializados. López Aliaga tiene las propuestas más disruptivas e innovadoras del campo electoral en seguridad; Acuña tiene propuestas más convencionales.

## 📚 EDUCACIÓN

Acuña propone un COAR por región, ILA y reforma curricular con inglés e IA. López Aliaga plantea Chino Mandarín, Libertad Financiera, internet satelital y parques tecnológicos. Ambos priorizan la conectividad digital pero con enfoques distintos: Acuña más institucionalista, López Aliaga más orientado al mercado global.

## 🏥 SALUD

Acuña propone telemedicina con IA e infraestructura hospitalaria vía APP. López Aliaga propone transformar EsSalud en entidad técnica autónoma, medicamentos genéricos obligatorios y dotar de personal postas rurales. López Aliaga tiene el plan más específico en reforma institucional de salud; Acuña tiene el plan más tecnológico.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. López Aliaga propone trenes de alta velocidad Lima-Ica y Lima-Trujillo, túnel trasandino y zonas francas. Ambos tienen propuestas de gran escala; López Aliaga tiene las más innovadoras e internacionalmente comparables.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. López Aliaga prioriza la industria del litio y zonas francas, con agenda ambiental secundaria. Ninguno tiene un plan ambiental serio.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. López Aliaga tiene mayor credibilidad anticorrupción personal, aunque Renovación Popular recibió aportes de constructoras brasileñas y enfrenta cuestionamientos por presunta deuda con la SUNAT.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga tiene el plan más técnicamente sofisticado en macroeconomía, seguridad e infraestructura innovadora, con mayor credibilidad anticorrupción personal. Acuña tiene mayor experiencia en gestión pública regional y propuestas de infraestructura más convencionales pero ejecutables. El diferenciador principal es el historial judicial: Acuña arrastra más investigaciones que cualquier otro candidato del campo.""",

"163:169": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva con 72 proyectos y expansión extractiva. Belmont propone economía social de mercado, Plan Choque de 1,500 obras paralizadas y renegociación de contratos estratégicos. Acuña tiene propuestas de mayor escala; Belmont tiene propuestas más ejecutables en el corto plazo y más orientadas a la formalización laboral. La analista Costa del El Comercio señaló que el plan de Belmont "no se tomó el tiempo" para identificar los principales problemas económicos del país con la misma profundidad que otros candidatos.

## 🔒 SEGURIDAD

Ambos proponen reforzar las instituciones de seguridad, aunque con enfoques distintos. Acuña plantea el Comando Nacional contra el Sicariato y 5,000 nuevos efectivos. Belmont propone reestructurar PNP, MP, INPE y PJ con énfasis en percepción ciudadana y resolver el 50% de denuncias. Belmont tiene un enfoque más sistémico e institucional; Acuña tiene un enfoque más operativo.

## 📚 EDUCACIÓN

Acuña propone COAR por región, ILA y reforma curricular. Belmont propone educación gratuita y obligatoria con énfasis en deporte, folklore y valores, y reducción de la deserción rural al 5%. Acuña tiene un plan más moderno y tecnológico; Belmont tiene un plan más culturalista y comunitario.

## 🏥 SALUD

Acuña propone telemedicina con IA. Belmont propone elevar cobertura al 85%, rehabilitar puestos rurales y construir 50 nuevos establecimientos. Belmont tiene metas más específicas y territorialmente focalizadas en zonas vulnerables.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Belmont propone intervenir 10,000 km de caminos rurales y cuestiona el modelo de concesiones de peajes. Acuña tiene propuestas de mayor escala; Belmont tiene un enfoque más rural y crítico del modelo concesionario.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Belmont tiene una dimensión territorial-ambiental con énfasis en ordenamiento del territorio y se opone a privatizar recursos estratégicos. Belmont tiene una propuesta ambiental más coherente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales — el peor perfil anticorrupción del campo. Belmont propone imprescriptibilidad de delitos de corrupción y plataforma digital de obras con rendición de cuentas. Su historial personal es más limpio.

## 📊 CONCLUSIÓN TÉCNICA

Belmont tiene mayor credibilidad anticorrupción y propuestas más específicas en salud rural y desnutrición. Acuña tiene mayor presencia electoral y propuestas de infraestructura más ambiciosas. El diferenciador principal es el historial judicial de Acuña, que contrasta con el perfil más limpio de Belmont.""",

"163:170": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva y expansión extractiva con metas específicas. Luna Gálvez propone reactivación económica mediante inversión pública y privada con énfasis en turismo, sin metas específicas ni financiamiento claro. Acuña tiene un plan económico más desarrollado y con mayor especificidad; Luna Gálvez tiene un plan más genérico y menos técnico.

## 🔒 SEGURIDAD

Acuña plantea el Comando Nacional contra el Sicariato y 5,000 efectivos especializados. Luna Gálvez presenta propuestas genéricas de seguridad sin diferenciación clara, debilitadas por sus graves antecedentes judiciales vinculados a la manipulación de organismos autónomos como la ONPE y el CNM.

## 📚 EDUCACIÓN

Acuña propone COAR por región, programa ILA y reforma curricular con inglés e IA. Luna Gálvez propone mejorar la calidad educativa y la conectividad digital sin innovaciones que lo distingan. Acuña tiene un plan educativo más específico y diferenciado.

## 🏥 SALUD

Acuña propone telemedicina con IA e infraestructura hospitalaria. Luna Gálvez propone ampliar la cobertura de salud sin mecanismos de financiamiento claros. Acuña tiene propuestas más concretas.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Luna Gálvez propone inversión en infraestructura vial sin especificidades técnicas. Acuña gana claramente en este eje.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Luna Gálvez incluye propuestas ambientales genéricas sin compromisos medibles. Ninguno tiene una propuesta ambiental seria.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. Luna Gálvez enfrenta investigaciones por manipulación de organismos autónomos — ONPE y CNM — que representan una amenaza directa a la democracia institucional. Ambos tienen perfiles anticorrupción muy comprometidos, aunque de naturaleza diferente: Acuña por presunta corrupción económica, Luna Gálvez por presunta captura institucional del Estado.

## 📊 CONCLUSIÓN TÉCNICA

Esta es una de las comparaciones más difíciles del campo electoral, pues ambos candidatos tienen graves cuestionamientos anticorrupción. Acuña tiene el plan más desarrollado y mayor experiencia en gestión pública. Luna Gálvez tiene un perfil programático más débil y antecedentes que amenazan directamente la institucionalidad democrática. Técnicamente, Acuña supera a Luna Gálvez en todas las dimensiones programáticas, aunque ambos representan riesgos institucionales significativos.""",

"163:171": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva y expansión extractiva con metas específicas. Álvarez propone reactivación económica y formalización sin propuestas técnicas sólidas, compensadas por su cercanía con sectores populares. El plan económico de Acuña es más sofisticado; el de Álvarez es más genérico pero más comunicable al ciudadano común.

## 🔒 SEGURIDAD

Acuña propone el Comando Nacional contra el Sicariato. Álvarez propone un enfoque integral con mano firme, inteligencia y articulación estatal — con la meta concreta de reducir homicidios de 8.6 a 6 por 100 mil habitantes y extorsión en más del 50%. Sorprendentemente, el plan de seguridad de Álvarez es más detallado técnicamente que el de Acuña.

## 📚 EDUCACIÓN

Acuña propone COAR por región, ILA y reforma curricular. Álvarez propone acceso universal a la educación con énfasis en los más vulnerables, sin reformas estructurales. Acuña tiene un plan más específico e innovador.

## 🏥 SALUD

Acuña propone telemedicina con IA. Álvarez propone ampliar coberturas con programas sociales focalizados. Acuña tiene propuestas más tecnológicas; Álvarez tiene propuestas más orientadas a reducir brechas socioeconómicas.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Álvarez propone obras básicas sin proyectos de gran escala diferenciados. Acuña gana claramente en este eje.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Álvarez incluye sostenibilidad ambiental con énfasis en agua potable rural. Álvarez tiene una propuesta ambiental más consistente con las necesidades de las comunidades rurales.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. Álvarez propone transparencia en la gestión pública, aunque su plan carece de mecanismos institucionales robustos. Álvarez tiene mayor credibilidad personal anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Acuña tiene el plan más detallado en infraestructura, educación y tecnología médica. Álvarez tiene mayor credibilidad anticorrupción y un plan de seguridad sorprendentemente técnico. El resultado electoral final favoreció a Álvarez según las encuestas más recientes, donde subió significativamente en las preferencias. Programáticamente, el plan de Acuña es más completo; electoralmente, Álvarez tiene mayor potencial de sorpresa.""",

"163:172": """## 💰 ECONOMÍA

Acuña propone infraestructura masiva y expansión extractiva. Pérez Tello propone digitalización radical del Estado, simplificación de trámites, formalización empresarial y diversificación productiva con énfasis en economía digital, bioindustria, acuicultura y economía creativa. La analista económica Alejandra Costa del El Comercio destacó a Pérez Tello — junto a Fujimori, López Aliaga y López Chau — como uno de los candidatos con propuestas económicas más serias. El plan de Pérez Tello es más sofisticado y diversificado; el de Acuña más concentrado en infraestructura y extractivismo.

## 🔒 SEGURIDAD

Acuña propone el Comando Nacional contra el Sicariato. Pérez Tello propone derogar leyes procrimen, modernización policial con tecnología predictiva y recuperación del control territorial con enfoque preventivo. Pérez Tello tiene un plan de seguridad más equilibrado entre represión y prevención.

## 📚 EDUCACIÓN

Acuña propone COAR por región, ILA y reforma curricular. Pérez Tello propone universalizar educación inicial, mejorar la calidad docente, digitalizar escuelas y promover educación intercultural rural. Pérez Tello tiene un plan educativo más sistémico e inclusivo.

## 🏥 SALUD

Acuña propone telemedicina con IA. Pérez Tello propone integrar sistemas de salud con énfasis en atención primaria, reducción de anemia y acceso universal a medicamentos esenciales. Pérez Tello tiene un plan de salud más integral.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Pérez Tello propone infraestructura de conectividad territorial priorizando comunidades rurales y periurbanas. Acuña tiene propuestas de mayor escala; Pérez Tello tiene un enfoque más equitativo territorialmente.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Pérez Tello incluye una dimensión ambiental sólida con énfasis en economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más consistente de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. Pérez Tello propone digitalización estatal para transparencia, control ciudadano y reforma del sistema de justicia, con credibilidad respaldada por su trayectoria ministerial sin investigaciones relevantes. La diferencia en credibilidad anticorrupción es muy significativa.

## 📊 CONCLUSIÓN TÉCNICA

Pérez Tello supera a Acuña en casi todos los ejes programáticos: economía diversificada, seguridad equilibrada, salud integral, medio ambiente y anticorrupción. Acuña supera a Pérez Tello en escala de propuestas de infraestructura y en presencia electoral. Es una de las comparaciones donde la superioridad programática de un candidato contrasta más claramente con su menor presencia electoral.""",

"163:173": """## 💰 ECONOMÍA

Acuña defiende el libre mercado con expansión extractiva e infraestructura masiva. Sánchez propone superar el modelo neoliberal: economía mixta, soberanía sobre recursos, impuesto a sobreganancias mineras y presión tributaria del 25%. Son posiciones diametralmente opuestas. Acuña es más afín al consenso técnico internacional; Sánchez propone una transformación estructural que genera incertidumbre para la inversión privada.

## 🔒 SEGURIDAD

Acuña propone el Comando Nacional contra el Sicariato. Sánchez propone depuración policial, Sistema Nacional Integrado de Información Criminal y ataque a economías ilegales. Sánchez tiene el enfoque más estructural; Acuña tiene el más operativo.

## 📚 EDUCACIÓN

Acuña propone COAR por región e ILA. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI, salario de 1 UIT para docentes e ingreso libre a la educación superior. Sánchez tiene el plan más redistributivo e inclusivo; Acuña tiene propuestas más específicas de infraestructura.

## 🏥 SALUD

Acuña propone telemedicina con IA. Sánchez propone Redes Integradas de Salud, Fondo para suministros médicos y tiempo máximo de 72 horas para diagnósticos. Sánchez tiene el plan más sistémico y con mayor cobertura territorial.

## 🚆 TRANSPORTE

Acuña propone 72 proyectos con S/143 mil millones. Sánchez propone 10,000 km de caminos rurales para reducir costos logísticos. Acuña tiene propuestas de mayor escala; Sánchez tiene un enfoque más rural y equitativo.

## 🌿 MEDIO AMBIENTE

Acuña prioriza la expansión extractiva. Sánchez propone transición ecológica justa, economía circular y prohibición gradual de exportar minerales sin procesamiento. Sánchez tiene la propuesta ambiental más ambiciosa del campo electoral.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Acuña enfrenta 132 investigaciones fiscales. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con el gobierno Castillo genera dudas. Ninguno de los dos tiene un perfil anticorrupción sólido, aunque por razones distintas.

## 📊 CONCLUSIÓN TÉCNICA

Acuña y Sánchez representan opciones muy distintas ideológicamente. Acuña es el candidato del extractivismo y la infraestructura; Sánchez es el candidato de la redistribución y el cambio estructural. Programáticamente, Sánchez supera a Acuña en salud, educación y medio ambiente; Acuña supera a Sánchez en coherencia macroeconómica con el sistema internacional. El mayor lastre de Acuña es su historial judicial; el de Sánchez es su asociación con Castillo.""",

"164:167": """## 💰 ECONOMÍA

López Chau propone "Todo el poder a las regiones" como eje transformador — descentralización productiva, masificación del gas con tarifa única y conversión de universidades en plataformas de innovación. Nieto propone un Fondo Soberano de Riqueza, crecimiento del 5%, presión tributaria del 18% y diversificación productiva con transición ecológica. Ambos tienen los planes económicos más coherentes técnicamente del campo electoral según analistas. La analista Costa del El Comercio destacó a ambos, junto con Pérez Tello, como los candidatos con propuestas económicas más serias fuera del grupo Fujimori-López Aliaga. La diferencia es que López Chau tiene un modelo más territorial y descentralizador; Nieto tiene un modelo más macroeconómico con el Fondo Soberano como innovación principal.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen, purgar la Policía con meritocracia y modernizar comisarías con inteligencia. Nieto propone derogar las leyes procrimen y una reforma institucional integral del sistema de seguridad y justicia. Son enfoques muy similares — ambos institucionalistas y no punitivos — con la diferencia de que López Chau es más específico en la modernización tecnológica y Nieto es más enfocado en la reforma legislativa.

## 📚 EDUCACIÓN

López Chau propone convertir universidades en plataformas científicas, cobertura universal de inicial y desplegar mil agrónomos jóvenes. Nieto propone universalizar conectividad digital, reformar el currículo con competencias del siglo XXI y mejorar la formación docente. Ambos tienen planes educativos de alta calidad técnica — López Chau con mayor énfasis en ciencia aplicada al agro, Nieto con mayor énfasis en reforma curricular y docente.

## 🏥 SALUD

López Chau propone integrar Minsa, EsSalud y gobiernos regionales con énfasis en agua potable y saneamiento. Nieto propone universalizar la salud con estrategia preventiva y atención especial a anemia y mortalidad materna. Son enfoques complementarios — López Chau más territorial y Nieto más preventivo.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática para obras regionales y acelerar Chavimochic, Chinecas y Majes Siguas 2. Nieto propone fortalecer la inversión en infraestructura vial con énfasis en equidad territorial. Enfoques similares, ambos más modestos que Fujimori o López Aliaga pero más realistas en términos fiscales.

## 🌿 MEDIO AMBIENTE

López Chau propone gestión de agua con cochas y reservorios — la propuesta hídrica más concreta del campo electoral. Nieto incluye transición ecológica, economía circular y sostenibilidad como ejes transversales. Nieto tiene la propuesta ambiental más integral; López Chau tiene la propuesta hídrica más específica y pertinente para las regiones andinas.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Chau plantea meritocracia como eje central y el modelo de Singapur para eliminar coimas. Nieto tiene el perfil anticorrupción más limpio del campo electoral, con trayectoria ministerial sin investigaciones relevantes. Ambos tienen alta credibilidad anticorrupción personal.

## 📊 CONCLUSIÓN TÉCNICA

López Chau y Nieto son los dos candidatos con los planes más técnicamente coherentes del centro del espectro político. López Chau tiene mayor potencial de articulación territorial y una propuesta educativa más innovadora en ciencia aplicada. Nieto tiene el plan más equilibrado en todas las dimensiones y el perfil anticorrupción más sólido del campo. Es la comparación donde la calidad programática de ambos es más pareja — la diferencia es de énfasis más que de calidad.""",

"164:170": """## 💰 ECONOMÍA

López Chau propone descentralización productiva, masificación del gas y transformación universitaria. Luna Gálvez propone reactivación económica genérica sin metas específicas. El plan de López Chau es sustancialmente más sofisticado técnicamente.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen, purga policial meritocrática y modernización tecnológica. Luna Gálvez tiene propuestas genéricas de seguridad debilitadas por sus investigaciones por manipulación de organismos autónomos del Estado.

## 📚 EDUCACIÓN

López Chau propone universidades como plataformas científicas y cobertura universal de inicial. Luna Gálvez propone mejorar calidad y conectividad sin propuestas diferenciadas. López Chau gana claramente.

## 🏥 SALUD

López Chau propone integrar los sistemas de salud con énfasis en agua y saneamiento. Luna Gálvez propone ampliar cobertura sin financiamiento claro. López Chau tiene el plan más articulado.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática para obras y proyectos estratégicos. Luna Gálvez propone inversión vial genérica. López Chau es más específico y técnico.

## 🌿 MEDIO AMBIENTE

López Chau tiene la propuesta hídrica más concreta. Luna Gálvez tiene propuestas ambientales genéricas. López Chau gana claramente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Chau tiene alta credibilidad anticorrupción. Luna Gálvez enfrenta investigaciones por manipulación de ONPE y CNM — amenaza directa a la democracia institucional. La diferencia es abismal.

## 📊 CONCLUSIÓN TÉCNICA

López Chau supera a Luna Gálvez en todas las dimensiones programáticas. Las investigaciones de Luna Gálvez por captura institucional del Estado representan el mayor riesgo democrático del campo electoral, lo que hace que esta comparación sea una de las más claras en términos de preferencia técnica.""",

"164:171": """## 💰 ECONOMÍA

López Chau propone descentralización productiva, masificación del gas y plataformas científicas universitarias. Álvarez propone reactivación económica con enfoque en disciplina fiscal — convergencia del déficit al 1% del PBI — sin propuestas técnicas diferenciadoras. López Chau tiene el plan más sofisticado y territorial; Álvarez tiene el plan más convencional pero más comunicable al ciudadano promedio.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen y purga policial meritocrática. Álvarez propone enfoque integral con meta de reducir homicidios de 8.6 a 6 por 100 mil habitantes y extorsión en más del 50%, con Plataforma Nacional de Análisis Criminal. El plan de seguridad de Álvarez es sorprendentemente más detallado y técnico que el de López Chau.

## 📚 EDUCACIÓN

López Chau propone universidades como plataformas científicas y cobertura universal de inicial. Álvarez propone acceso universal a la educación sin reformas estructurales. López Chau tiene un plan educativo más específico e innovador.

## 🏥 SALUD

López Chau propone integrar sistemas de salud con énfasis en agua y saneamiento. Álvarez propone ampliar coberturas con programas sociales. López Chau tiene el plan más sistémico.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática y proyectos estratégicos. Álvarez propone obras básicas con digitalización total del Estado. Enfoques complementarios, ambos más modestos que Fujimori o López Aliaga.

## 🌿 MEDIO AMBIENTE

López Chau tiene la propuesta hídrica más concreta. Álvarez incluye sostenibilidad ambiental con énfasis en agua para comunidades rurales. Ambos tienen propuestas ambientales similares en pertinencia.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Chau tiene alta credibilidad anticorrupción personal. Álvarez propone transparencia con digitalización total del Estado. Ambos tienen buena credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

López Chau tiene el plan más coherente técnicamente en educación, economía descentralizada y gestión hídrica. Álvarez tiene un plan de seguridad más detallado y mayor potencial electoral según las encuestas más recientes. La superioridad programática de López Chau contrasta con la sorpresiva capacidad electoral de Álvarez.""",

"164:172": """## 💰 ECONOMÍA

López Chau y Pérez Tello son los dos candidatos con mayor coherencia técnica en sus propuestas económicas según los analistas del El Comercio. López Chau apuesta por "Todo el poder a las regiones" — descentralización productiva, masificación del gas y ciencia aplicada. Pérez Tello propone digitalización radical del Estado, economía digital, bioindustria, acuicultura y economía creativa, con meta de elevar la inversión privada al 22% del PBI. Ambos planes son de alta calidad técnica: López Chau tiene un modelo más territorial; Pérez Tello tiene un modelo más orientado a la diversificación sectorial y la economía del conocimiento.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen, purga policial y modernización tecnológica. Pérez Tello propone derogar leyes procrimen, tecnología predictiva y enfoque preventivo-comunitario. Los dos planes más similares del campo electoral en este eje — ambos institucionalistas, tecnológicos y no punitivos.

## 📚 EDUCACIÓN

López Chau propone universidades como plataformas científicas y mil agrónomos jóvenes. Pérez Tello propone universalizar educación inicial, mejorar calidad docente y educación intercultural. Planes complementarios de alta calidad — López Chau más enfocado en ciencia aplicada; Pérez Tello más enfocado en inclusión y calidad educativa.

## 🏥 SALUD

López Chau propone integrar sistemas con énfasis en agua y saneamiento. Pérez Tello propone integrar sistemas con énfasis en atención primaria y medicamentos esenciales. Enfoques muy similares, con diferencias de énfasis.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática y proyectos estratégicos. Pérez Tello propone infraestructura de conectividad territorial priorizando comunidades rurales. Enfoques similares en escala y pertinencia.

## 🌿 MEDIO AMBIENTE

López Chau tiene la propuesta hídrica más concreta. Pérez Tello incluye economía verde, gestión hídrica y reducción de emisiones. Pérez Tello tiene la propuesta ambiental más integral de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Ambos tienen alta credibilidad anticorrupción personal. López Chau plantea meritocracia y el modelo Singapur. Pérez Tello propone digitalización total del Estado, control ciudadano y reforma del sistema de justicia.

## 📊 CONCLUSIÓN TÉCNICA

Esta es la comparación de los dos candidatos con mayor calidad programática del centro del espectro político. López Chau tiene el plan más territorial y científico; Pérez Tello tiene el plan más diversificado sectorialmente y más consistente ambientalmente. En términos de credibilidad anticorrupción y calidad programática global, están muy parejos — la diferencia es de énfasis y estilo más que de calidad.""",

"164:173": """## 💰 ECONOMÍA

López Chau defiende el modelo de mercado con descentralización productiva. Sánchez propone superar el modelo neoliberal con economía mixta, soberanía sobre recursos y presión tributaria del 25%. Posiciones muy distintas. López Chau es más afín al consenso técnico internacional; Sánchez propone reformas más radicales con mayor incertidumbre para la inversión privada.

## 🔒 SEGURIDAD

López Chau propone derogar leyes procrimen y modernizar la Policía. Sánchez propone depuración policial y ataque a economías ilegales con veedurías ciudadanas. Enfoques similares en el énfasis institucional, con diferencias en la profundidad de la reforma.

## 📚 EDUCACIÓN

López Chau propone universidades como plataformas científicas. Sánchez propone educación como derecho fundamental, gasto del 6% del PBI y educación intercultural. Sánchez tiene el plan más redistributivo e inclusivo; López Chau el más orientado a la ciencia aplicada.

## 🏥 SALUD

López Chau propone integrar sistemas de salud. Sánchez propone Redes Integradas con Fondo para suministros y tiempo máximo de 72 horas para diagnósticos. Sánchez tiene el plan más sistémico y con mayor cobertura territorial.

## 🚆 TRANSPORTE

López Chau propone entidad meritocrática y proyectos estratégicos. Sánchez propone 10,000 km de caminos rurales. Enfoques distintos pero complementarios — López Chau más en grandes proyectos, Sánchez más en conectividad rural básica.

## 🌿 MEDIO AMBIENTE

López Chau tiene la propuesta hídrica más concreta. Sánchez propone transición ecológica justa, economía circular y compromisos con comunidades indígenas. Sánchez tiene la propuesta ambiental más ambiciosa y consistente.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

López Chau tiene alta credibilidad anticorrupción. Sánchez propone nueva Constitución con veedurías ciudadanas, pero su asociación con Castillo genera dudas. López Chau tiene mayor credibilidad institucional.

## 📊 CONCLUSIÓN TÉCNICA

López Chau tiene el plan más coherente con el modelo económico actual y mayor credibilidad institucional. Sánchez tiene el plan más ambicioso en distribución social, medio ambiente y salud territorial. La elección entre ambos implica un trade-off: estabilidad económica con innovación territorial (López Chau) versus transformación social con riesgo macroeconómico (Sánchez).""",

"165:166": """## 💰 ECONOMÍA

Olivera propone formalizar la economía con un millón de empleos formales anuales, reducir el IGV progresivamente al 10% hacia 2031 e impulsar el turismo con nuevos aeropuertos regionales. Fujimori defiende el libre mercado con disciplina fiscal, shock desregulatorio y atracción de USD 5,000–7,000 millones de inversión privada adicional. Fujimori tiene el plan más técnicamente articulado en macroeconomía; Olivera tiene propuestas más específicas en reducción tributaria para la formalización.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales para eliminar la inmunidad de autoridades y mecanismos de transparencia en tiempo real. Fujimori propone mano dura con FFAA, videovigilancia avanzada, mega penales y retiro de la CIDH. Fujimori tiene el plan más detallado operativamente; Olivera tiene un enfoque más institucionalista y anticorrupción.

## 📚 EDUCACIÓN

Olivera propone eliminar la desnutrición crónica infantil como base para mejorar el rendimiento educativo, con énfasis en zonas rurales. Fujimori propone inglés obligatorio, becas e infraestructura educativa masiva. Fujimori tiene el plan más específico y moderno; Olivera tiene un enfoque más social y territorial.

## 🏥 SALUD

Olivera prioriza la eliminación de la desnutrición crónica infantil mediante el fortalecimiento agrícola. Fujimori propone reducir anemia al 20%, universalizar vacunación e invertir en infraestructura hospitalaria. Fujimori tiene el plan más completo; Olivera tiene un enfoque preventivo basado en alimentación y agricultura.

## 🚆 TRANSPORTE

Olivera propone nuevos aeropuertos internacionales regionales para impulsar el turismo. Fujimori propone cuatro metros en Lima, metros regionales, modernización de 17 aeropuertos y pavimentación rural. Fujimori tiene propuestas de mayor escala y especificidad.

## 🌿 MEDIO AMBIENTE

Olivera propone reformas institucionales sin metas ambientales específicas verificables. Fujimori propone modernizar la Ley General de Minería con respeto ambiental. Ninguno tiene una propuesta ambiental sólida.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera central — propone eliminar la inmunidad de altas autoridades y un referéndum para reformas institucionales. Su credibilidad anticorrupción es mayor que la de Fujimori, quien enfrenta tres procesos penales por Odebrecht.

## 📊 CONCLUSIÓN TÉCNICA

Fujimori tiene el plan más detallado técnicamente en macroeconomía, seguridad e infraestructura. Olivera tiene mayor credibilidad anticorrupción y un enfoque más social basado en la alimentación y la transparencia institucional. La principal diferencia es que Fujimori opera desde la derecha institucionalizada con plan técnico completo, mientras Olivera opera desde la reforma moral del Estado con propuestas más simples pero más coherentes en anticorrupción.""",

"165:167": """## 💰 ECONOMÍA

Olivera propone formalización con reducción progresiva del IGV al 10% y nuevos aeropuertos regionales para el turismo. Nieto propone Fondo Soberano de Riqueza, crecimiento del 5%, presión tributaria del 18% y diversificación productiva con economía circular. Nieto tiene el plan económico más sofisticado técnicamente; Olivera tiene propuestas más específicas en reducción tributaria.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales para eliminar la inmunidad de autoridades. Nieto propone derogar leyes procrimen y reforma institucional integral del sistema de seguridad y justicia. Enfoques muy similares — ambos institucionalistas y reformistas — aunque Nieto tiene mayor especificidad.

## 📚 EDUCACIÓN

Olivera propone la alimentación y la desnutrición como base de la mejora educativa. Nieto propone reforma curricular, conectividad digital universal y mejora docente. Nieto tiene el plan educativo más moderno y sistémico.

## 🏥 SALUD

Olivera prioriza la nutrición y la agricultura como base de la salud. Nieto propone universalizar la salud integrando los sistemas con estrategia preventiva. Nieto tiene el plan más integral; Olivera tiene el enfoque más preventivo basado en alimentación.

## 🚆 TRANSPORTE

Olivera propone nuevos aeropuertos regionales para el turismo. Nieto propone infraestructura vial con énfasis en equidad territorial. Nieto tiene un plan más completo en infraestructura.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas ambientales sin metas verificables. Nieto incluye transición ecológica y economía circular. Nieto tiene la propuesta ambiental más consistente de los dos.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica, con propuesta de eliminar inmunidades y referéndum institucional. Nieto tiene el perfil anticorrupción más limpio del campo electoral con trayectoria ministerial impecable. Ambos tienen alta credibilidad anticorrupción.

## 📊 CONCLUSIÓN TÉCNICA

Nieto tiene el plan más técnicamente completo y coherente en todas las dimensiones. Olivera tiene mayor historia anticorrupción y un enfoque más social basado en la alimentación como motor del desarrollo humano. Ambos tienen alta credibilidad personal, con Nieto como el candidato con mayor profundidad programática de los dos.""",

"165:168": """## 💰 ECONOMÍA

Olivera propone formalización con reducción progresiva del IGV al 10% y nuevos aeropuertos para el turismo. López Aliaga propone reforma tributaria más agresiva: unificar regímenes, reducir IGV, Banco Pyme, 7% de crecimiento y 2 millones de empleos. López Aliaga tiene el plan macroeconómico más sofisticado e innovador; ambos coinciden en la reducción del IGV como herramienta de formalización, aunque con distintas intensidades.

## 🔒 SEGURIDAD

Olivera propone reformas institucionales anticorrupción. López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos, penales de alta montaña y Comando 'Las Palmas'. López Aliaga tiene las propuestas más disruptivas e innovadoras en seguridad del campo electoral.

## 📚 EDUCACIÓN

Olivera propone la alimentación y desnutrición como base educativa. López Aliaga propone Chino Mandarín, Libertad Financiera, internet satelital y parques tecnológicos. Planes muy distintos — Olivera más social, López Aliaga más orientado al mercado global.

## 🏥 SALUD

Olivera prioriza la nutrición y agricultura como base de la salud. López Aliaga propone transformar EsSalud en entidad técnica autónoma y medicamentos genéricos obligatorios. López Aliaga tiene el plan más específico en reforma institucional de salud.

## 🚆 TRANSPORTE

Olivera propone aeropuertos regionales. López Aliaga propone trenes de alta velocidad, túnel trasandino y zonas francas. López Aliaga tiene propuestas de mayor escala e innovación.

## 🌿 MEDIO AMBIENTE

Olivera tiene propuestas ambientales sin metas verificables. López Aliaga prioriza el litio y las zonas francas industriales. Ninguno tiene una propuesta ambiental seria.

## ⚖️ CORRUPCIÓN E INTEGRIDAD

Olivera tiene la lucha anticorrupción como bandera histórica — eliminar inmunidades y referéndum institucional. López Aliaga propone la Central de Lucha contra la Corrupción con poderes plenos y blockchain. Olivera tiene mayor historia anticorrupción; López Aliaga tiene propuestas institucionales más detalladas.

## 📊 CONCLUSIÓN TÉCNICA

López Aliaga supera a Olivera en escala y sofisticación de propuestas en casi todos los ejes. Olivera tiene una historia anticorrupción más larga y un enfoque más social basado en la alimentación. La comparación refleja la diferencia entre el outsider mediático con plan técnico sofisticado (López Aliaga) y el político veterano con bandera moral clara pero plan técnico más simple (Olivera)."""

}

async def insertar_todo():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    print(f"Insertando {len(ANALISIS)} análisis técnicos (grupo 2)...")

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
    print(f"\n🎉 Grupo 2 completado: {len(ANALISIS)} análisis técnicos insertados.")

asyncio.run(insertar_todo())
