"""
insert_viabilidades.py — Inserta análisis de viabilidad de los 10 candidatos sin caché
========================================================================================
IDs: 163, 164, 165, 166, 168, 169, 170, 171, 172, 173
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert as pg_insert
from dotenv import load_dotenv

load_dotenv(".env.prod")
DATABASE_URL = os.getenv("DATABASE_URL")

# Contexto fiscal común para todos los análisis
# - Presupuesto 2026: S/257,561 millones (+2.3%, el menor en una década)
# - Déficit fiscal meta: 1.8% del PBI (regla fiscal MMM 2026-2029)
# - Deuda pública: ~32% del PBI
# - Presión tributaria: 14.1-15.1% del PBI (LATAM promedio: 29.4%)
# - Informalidad laboral: 70.9%
# - Crecimiento PBI 2026: ~3-3.5% proyectado

VIABILIDADES = {

# ── 163: César Acuña (APP) ────────────────────────────────────────────────
"163": """## 1. PORTAFOLIO DE INFRAESTRUCTURA DE S/143 MIL MILLONES
**Qué propone:** 72 proyectos de infraestructura nacional, incluyendo carreteras, irrigaciones y puertos, con inversión total de S/143 mil millones en el quinquenio.

**Costo estimado:** S/28,600 millones anuales promedio, equivalente al 11% del presupuesto nacional actual.

**Precedentes internacionales:** Chile implementó planes de infraestructura similares en los 90s mediante APPs y concesiones. Colombia ejecutó las "4G" viales con participación privada estructurada. Brasil fracasó con el PAC (Programa de Aceleración del Crecimiento) por sobrecostos y corrupción.

**Restricciones:** La capacidad de ejecución del Estado peruano promedió 70% en inversión pública los últimos años. El ANIN (Autoridad Nacional de Infraestructura) ya enfrenta dificultades para ejecutar proyectos existentes. Las propuestas de infraestructura de gran escala en Perú históricamente presentan sobrecostos del 30-60%.

**Veredicto:** Baja viabilidad sin reforma institucional previa.

## 2. MINISTERIO DE INFRAESTRUCTURA
**Qué propone:** Crear un nuevo ministerio que centralice la planificación y ejecución de obras públicas.

**Costo estimado:** S/500-800 millones anuales en estructura ministerial adicional.

**Precedentes internacionales:** Argentina creó el Ministerio de Obras Públicas en 2019 sin mejoras sustanciales en ejecución. Chile mantiene sistema de ministerios sectoriales con coordinación efectiva sin un ministerio único.

**Restricciones:** La Constitución de 1993 limita el número de ministerios. El problema de ejecución en Perú es de capacidad institucional y anticorrupción, no de estructura orgánica.

**Veredicto:** Baja viabilidad. No resuelve el problema de fondo.

## 3. EXPANSIÓN MINERA Y PETROLERA — DUPLICAR PBI DE HIDROCARBUROS
**Qué propone:** Inversión de USD 6,000 millones en minería y duplicar el PBI de hidrocarburos mediante exploración masiva.

**Costo estimado:** Requiere incentivos fiscales y cambios regulatorios cuyo costo fiscal podría superar los S/3,000-5,000 millones anuales en exoneraciones.

**Precedentes internacionales:** Colombia aumentó su producción de petróleo mediante contratos de riesgo compartido. Ecuador expandió producción con Petroecuador pero generó conflictos socioambientales. México fracasó en su intento de revertir el declive con PEMEX.

**Restricciones:** Los precios de los minerales tienen alta volatilidad. La conflictividad social en zonas mineras del Perú (Chumbivilcas, Espinar, Tía María) es el principal obstáculo, no la regulación. El PBI de hidrocarburos depende de inversión privada que no responde a mandatos políticos.

**Veredicto:** Media viabilidad.

## 4. PROGRAMA ILA — INTERNET, LUZ Y AGUA PARA ESCUELAS
**Qué propone:** Garantizar internet, luz y agua en el 100% de escuelas públicas del país.

**Costo estimado:** S/2,500-4,000 millones en infraestructura y S/800-1,200 millones anuales en mantenimiento.

**Precedentes internacionales:** Uruguay implementó Plan Ceibal con conectividad universal en 5 años. Colombia conectó el 80% de escuelas rurales mediante asociaciones con operadores privados. Brasil fracasó en intentos similares por problemas de mantenimiento.

**Restricciones:** El 33% de escuelas rurales carece de electricidad según el MINEDU. La conectividad en zonas rurales remotas requiere satélite cuyo costo es 5-8 veces mayor que fibra. El presupuesto 2026 ya contempla crecimiento de solo 2.3%.

**Veredicto:** Media viabilidad en 5 años.

## 5. COAR POR REGIÓN — COLEGIOS DE ALTO RENDIMIENTO
**Qué propone:** Construir un Colegio de Alto Rendimiento en cada una de las 25 regiones del país.

**Costo estimado:** S/150-250 millones por COAR (infraestructura + equipamiento). Total: S/2,500-4,000 millones.

**Precedentes internacionales:** Perú ya tiene 25 COAR operativos — la propuesta implicaría duplicar la red existente. El modelo COAR ha demostrado resultados en acceso universitario.

**Restricciones:** Ya existe un COAR por región. La propuesta duplicaría la oferta en regiones que ya tienen uno, reduciendo su impacto marginal. El problema de calidad educativa no se resuelve solo con infraestructura de élite.

**Veredicto:** Baja viabilidad. Confunde cantidad con calidad.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Inconsistente. El portafolio de S/143 mil millones más las propuestas de expansión extractiva y nuevos programas sociales requieren entre S/35,000-50,000 millones adicionales anuales, equivalentes al 14-20% del presupuesto actual. El plan carece de fuentes de financiamiento específicas y mecanismos de ejecución.

**Restricciones estructurales:** La capacidad de ejecución institucional del Estado es el principal cuello de botella — no el dinero. El historial de ejecución presupuestal en grandes obras en Perú (Gasoducto Sur, línea 2 del Metro de Lima) muestra que la ambición no se traduce automáticamente en obras.

**Riesgo anticorrupción:** Dado el perfil del candidato con 132 investigaciones fiscales activas, un portafolio de infraestructura de S/143 mil millones sin mecanismos robustos de control representa un riesgo institucional significativo.

El plan tiene objetivos socialmente válidos pero es fiscalmente inviable en su escala y presenta serios riesgos de captura en la ejecución.""",

# ── 164: Pablo López Chau (Ahora Nación) ─────────────────────────────────
"164": """## 1. DESCENTRALIZACIÓN PRODUCTIVA — "TODO EL PODER A LAS REGIONES"
**Qué propone:** Transformar las regiones en polos exportadores con industrialización, innovación y cadenas de valor regionales como eje de crecimiento.

**Costo estimado:** S/8,000-12,000 millones en transferencias adicionales a gobiernos regionales, infraestructura productiva e innovación.

**Precedentes internacionales:** Corea del Sur implementó descentralización productiva exitosa en los 70s-80s con zonas económicas especiales. Chile desarrolló polos productivos regionales (vino, salmon, cobre) con resultados positivos. Brasil fracasó en la descentralización productiva por baja capacidad institucional regional.

**Restricciones:** Los gobiernos regionales peruanos tienen una tasa de ejecución promedio del 65% en inversión. La descentralización fiscal en Perú ha generado duplicidad de funciones y baja eficiencia. La presión tributaria de solo 14.1% del PBI limita los recursos disponibles.

**Veredicto:** Media viabilidad si va acompañada de reforma institucional regional.

## 2. MASIFICACIÓN DEL GAS CON TARIFA ÚNICA NACIONAL
**Qué propone:** Implementar tarifa única de gas natural a nivel nacional independientemente de la región, eliminando las diferencias actuales.

**Costo estimado:** Subsidio diferenciado de S/2,000-4,000 millones anuales para compensar diferencias de costo entre regiones.

**Precedentes internacionales:** Bolivia implementó tarifa única de gas con subsidio estatal — sostenible gracias a su producción propia pero generó presiones fiscales. Colombia tiene tarifas diferenciadas por región con subsidios focalizados. México unificó tarifas con alto costo fiscal.

**Restricciones:** El Perú tiene infraestructura gasífera concentrada en Lima y pocos corredores. Llevar gas a las 25 regiones requiere inversión en infraestructura de transporte y distribución estimada en USD 3,000-5,000 millones. La regla fiscal del 1.8% del PBI para 2026 no tiene espacio para un subsidio permanente de esta magnitud.

**Veredicto:** Baja viabilidad sin inversión previa en infraestructura.

## 3. UNIVERSIDADES COMO PLATAFORMAS CIENTÍFICAS
**Qué propone:** Convertir las universidades públicas en plataformas de ciencia, tecnología e innovación para potenciar las regiones.

**Costo estimado:** S/1,500-2,500 millones adicionales en equipamiento, investigación y conexión universidad-empresa.

**Precedentes internacionales:** Costa Rica logró atraer a Intel y empresas de alta tecnología apoyándose en el ITCR. Chile desarrolló el ecosistema de innovación con CORFO y universidades. Colombia implementó Colciencias con resultados mixtos.

**Restricciones:** El CONCYTEC tiene un presupuesto de solo S/350 millones anuales. El 73% de las universidades públicas tienen serias limitaciones de infraestructura según la SUNEDU. La investigación aplicada requiere vínculos empresariales que tardan décadas en consolidarse.

**Veredicto:** Media viabilidad en horizonte de 10+ años, no 5.

## 4. MIL AGRÓNOMOS JÓVENES CON UNIVERSIDADES PÚBLICAS
**Qué propone:** Desplegar mil agrónomos jóvenes financiados por el Estado en cada región para asistencia técnica agrícola.

**Costo estimado:** S/180-250 millones anuales en salarios, equipamiento y logística.

**Precedentes internacionales:** Brasil implementó EMBRAPA con asistencia técnica estatal con resultados muy positivos. Ecuador desplegó técnicos agrícolas con apoyo de universidades con impacto moderado. Colombia tiene los CERT (Centros de Excelencia y Apropiación) con resultados positivos en zonas rurales.

**Restricciones:** La oferta de agrónomos egresados de universidades públicas es de aproximadamente 3,000-4,000 anuales. Retener a jóvenes profesionales en zonas rurales remotas es el principal desafío. El MIDAGRI ya tiene programas similares con bajo nivel de ejecución.

**Veredicto:** Alta viabilidad. Es la propuesta más concreta y ejecutable del plan.

## 5. COBERTURA UNIVERSAL DE EDUCACIÓN INICIAL (3-5 AÑOS)
**Qué propone:** Garantizar que el 100% de niños de 3 a 5 años acceda a educación inicial con enfoque integral.

**Costo estimado:** S/3,500-5,000 millones adicionales en infraestructura, docentes y materiales para zonas rurales.

**Precedentes internacionales:** México logró cobertura del 90%+ en educación inicial mediante programa CONAFE. Chile universalizó pre-kínder y kínder con alta inversión pública. Ecuador implementó el Programa Creciendo con Nuestros Hijos con resultados positivos en zonas rurales.

**Restricciones:** La cobertura actual en Perú es de ~85% en zonas urbanas y ~65% en rurales. El MINEDU ya tiene programas de expansión pero con baja velocidad de avance. La formación de docentes de inicial tarda 4-5 años.

**Veredicto:** Media viabilidad.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Razonablemente consistente. López Chau propone crecimiento del 6% y déficit bajo el 1% del PBI — metas fiscalmente responsables. Sus propuestas más costosas (masificación del gas, descentralización productiva) requieren fuentes de financiamiento más específicas.

**Restricciones estructurales:** La capacidad institucional de los gobiernos regionales es el principal cuello de botella para su modelo descentralizador. La baja presión tributaria (14.1% del PBI) limita el espacio fiscal para financiar las reformas estructurales propuestas.

**Fortaleza del plan:** La propuesta de mil agrónomos jóvenes es la más concreta y ejecutable del campo electoral en agricultura. La masificación del gas requiere inversión previa en infraestructura que excede el quinquenio.

El plan tiene coherencia fiscal superior al promedio del campo electoral, con propuestas más realizables que las de candidatos con proyectos de infraestructura masiva, aunque la descentralización productiva requiere décadas, no cinco años.""",

# ── 165: Luis Olivera (Frente Esperanza) ─────────────────────────────────
"165": """## 1. UN MILLÓN DE EMPLEOS FORMALES ANUALES
**Qué propone:** Generar un millón de empleos formales por año mediante formalización empresarial masiva.

**Costo estimado:** S/3,000-5,000 millones en programas de formalización, subsidios de seguridad social y simplificación tributaria.

**Precedentes internacionales:** Colombia logró reducir la informalidad del 68% al 58% en una década mediante reforma laboral y simplificación tributaria. México generó empleos formales mediante expansión del IMSS con subsidios parciales. Chile tiene informalidad del 25% tras décadas de política consistente.

**Restricciones:** La informalidad laboral en Perú es del 70.9% — una de las más altas de América Latina. Generar un millón de empleos formales anuales requeriría cuadruplicar el ritmo actual de formalización. El presupuesto 2026 crece solo 2.3% y los ingresos tributarios son del 14.1% del PBI.

**Veredicto:** Baja viabilidad. La meta es 4-5 veces superior al ritmo histórico de formalización.

## 2. REDUCCIÓN PROGRESIVA DEL IGV AL 10% HACIA 2031
**Qué propone:** Reducir el Impuesto General a las Ventas del 18% actual al 10% progresivamente durante el quinquenio.

**Costo estimado:** Pérdida de recaudación de S/15,000-22,000 millones anuales al llegar al 10% (el IGV representa aproximadamente el 45% de la recaudación tributaria total).

**Precedentes internacionales:** Ecuador redujo el IVA temporalmente como estímulo económico, pero lo revirtió por presiones fiscales. Los países con IGV/IVA bajo como Canadá (5%) compensan con impuesto a la renta más alto. Ningún país de ingreso medio ha reducido el IGV en 8 puntos porcentuales en 5 años sin colapso fiscal.

**Restricciones:** El IGV recauda aproximadamente S/60,000-65,000 millones anuales. Reducirlo al 10% eliminaría entre S/25,000-30,000 millones de recaudación — el equivalente al 10% del presupuesto nacional. Con un déficit fiscal actual del 2.4% del PBI y una meta de 1.8% para 2026, esta propuesta es fiscalmente inviable.

**Veredicto:** Inviable. Provocaría una crisis fiscal de proporciones mayores.

## 3. ELIMINACIÓN DE INMUNIDAD PARA ALTAS AUTORIDADES + REFERÉNDUM
**Qué propone:** Eliminar la inmunidad parlamentaria y presidencial, y convocar a un referéndum para reformas institucionales.

**Costo estimado:** S/200-400 millones en costos electorales del referéndum y reforma normativa.

**Precedentes internacionales:** Ecuador eliminó la inmunidad legislativa mediante referéndum en 2008. Chile sometió a plebiscito la nueva Constitución en 2022 (rechazada). Bolivia reformó la Constitución mediante asamblea constituyente.

**Restricciones:** La eliminación de la inmunidad parlamentaria requiere reforma constitucional — que en Perú necesita dos legislaturas consecutivas o referéndum. El Congreso difícilmente aprobará su propia limitación de inmunidad. El TC peruano ha limitado el alcance de los referéndums en materias constitucionales.

**Veredicto:** Media viabilidad. Depende de la correlación de fuerzas en el Congreso.

## 4. AEROPUERTOS INTERNACIONALES REGIONALES
**Qué propone:** Construir nuevos aeropuertos internacionales en distintas regiones para impulsar el turismo.

**Costo estimado:** S/800-1,500 millones por aeropuerto internacional. Si son 5-6 nuevos: S/5,000-9,000 millones.

**Precedentes internacionales:** Colombia construyó aeropuertos regionales exitosos en Medellín, Cali y Cartagena que dinamizaron el turismo. Brasil invirtió en aeropuertos regionales con impacto mixto. Ecuador construyó el aeropuerto de Quito con financiamiento privado.

**Restricciones:** El Perú ya tiene 11 aeropuertos en concesión y varios proyectos pendientes como Chinchero (Cusco). La demanda aérea en regiones como Amazonas, Huancavelica o Apurímac no justifica aeropuertos internacionales. El ProInversión tiene proyectos aeroportuarios en cartera sin ejecutar.

**Veredicto:** Baja viabilidad. Prioridad incorrecta frente a infraestructura básica pendiente.

## 5. PLATAFORMAS DE TRANSPARENCIA EN TIEMPO REAL
**Qué propone:** Implementar mecanismos de transparencia en tiempo real sobre el uso de recursos públicos.

**Costo estimado:** S/300-500 millones en sistemas informáticos y capacitación.

**Precedentes internacionales:** Uruguay tiene el sistema SICE de transparencia presupuestal en tiempo real. Colombia implementó SECOP II para contrataciones públicas con resultados positivos. Brasil tiene el Portal de Transparencia con alta efectividad.

**Restricciones:** El Perú ya tiene el MEF con datos de ejecución presupuestal en línea y el SEACE para contrataciones. El problema no es la transparencia de datos sino la capacidad de procesarlos y actuar sobre ellos.

**Veredicto:** Alta viabilidad. Es la propuesta más factible del plan.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Gravemente inconsistente. La reducción del IGV al 10% provocaría la pérdida de entre S/25,000-30,000 millones de recaudación anual — una crisis fiscal que haría imposible cualquier otra propuesta del plan. Es la promesa más fiscalmente irresponsable del campo electoral 2026.

**Restricciones estructurales:** La combinación de reducción masiva de ingresos tributarios con promesas de un millón de empleos formales anuales es autocontradictoria — la formalización requiere más Estado, no menos recursos fiscales.

**Fortaleza del plan:** La propuesta de transparencia en tiempo real y la eliminación de inmunidades son institucionalmente valiosas pero requieren mayoría parlamentaria. La lucha anticorrupción como bandera es políticamente coherente con su historial.

El plan tiene objetivos anticorrupción valiosos pero la propuesta de reducción del IGV lo hace fiscalmente inviable en su conjunto.""",

# ── 166: Keiko Fujimori (Fuerza Popular) ─────────────────────────────────
"166": """## 1. SHOCK ANTICORRUPCIÓN DIGITAL — BLOCKCHAIN E IA
**Qué propone:** Implementar blockchain e inteligencia artificial en el 100% de contrataciones y obras estatales, con una criptomoneda estatal para transacciones públicas.

**Costo estimado:** S/1,500-3,000 millones en sistemas tecnológicos, capacitación y migración de datos.

**Precedentes internacionales:** Estonia usa blockchain para registros públicos con éxito. Georgia implementó blockchain en registros de tierras. Dubai usa blockchain en el 50% de transacciones gubernamentales. Ningún país ha implementado criptomoneda estatal exitosamente a escala nacional (El Salvador fracasó con Bitcoin).

**Restricciones:** La corrupción en el Estado peruano no es un problema tecnológico sino de incentivos, control y captura institucional. La implementación de blockchain requiere infraestructura digital que el 40% de entidades estatales aún no tiene. La criptomoneda estatal es una propuesta sin precedente exitoso en países de ingreso medio.

**Veredicto:** Baja viabilidad la criptomoneda estatal. Media viabilidad el blockchain para contrataciones.

## 2. REDUCCIÓN DE HOMICIDIOS EN 20% HACIA 2031
**Qué propone:** Reducir la tasa nacional de homicidios en 20% mediante patrullaje integrado, prevención juvenil y recuperación de espacios públicos.

**Costo estimado:** S/4,000-6,000 millones adicionales en modernización policial, mega penales y programas preventivos.

**Precedentes internacionales:** Colombia redujo homicidios en un 70% entre 1993 y 2015 con inversión policial masiva, negociaciones con grupos armados y políticas sociales. El Salvador redujo homicidios con mano dura extrema pero con críticas de DDHH. Ecuador redujo temporalmente la violencia con estado de excepción pero sin resultados sostenidos.

**Restricciones:** La tasa de homicidios del Perú es de 6.74 por 100 mil — moderada para la región. El crimen organizado en Perú tiene raíces económicas (narcotráfico, minería ilegal) que no responden solo a intervención policial. El 44% de comisarías opera sin servicios básicos y el 82% de vehículos policiales no funciona.

**Veredicto:** Media viabilidad. La meta del 20% es alcanzable con inversión sostenida.

## 3. CAPITALISMO POPULAR — FORMALIZACIÓN DE MYPES AL 60%
**Qué propone:** Elevar al 60% la formalidad de las MYPE con apertura electrónica instantánea de negocios e incentivos fiscales diferenciados.

**Costo estimado:** S/2,000-3,500 millones en incentivos tributarios y sistemas de formalización.

**Precedentes internacionales:** Colombia redujo la informalidad empresarial con la ley de simplificación de trámites. Chile tiene formalidad del 75%+ mediante costos bajos de apertura y sistema tributario simplificado. México tiene 57% de informalidad pese a reformas similares.

**Restricciones:** Más del 80% de microempresas opera en la informalidad en Perú. La informalidad tiene múltiples causas — no solo tributarias — incluyendo el acceso a crédito, la capacitación y los mercados. El régimen MYPE tributario ya existe con tasas del 1-1.5% de ingresos sin resultados definitivos.

**Veredicto:** Media viabilidad.

## 4. CUATRO METROS EN LIMA Y METROS REGIONALES
**Qué propone:** Poner operativos cuatro metros en Lima y desarrollar metros regionales en Arequipa, Trujillo y Piura.

**Costo estimado:** La Línea 2 (en construcción) ya costará más de S/15,000 millones. Cuatro metros nuevos + tres regionales: USD 12,000-18,000 millones.

**Precedentes internacionales:** Chile construyó Líneas 3, 6 y 7 del Metro de Santiago en un quinquenio con financiamiento mixto. Colombia tiene Transmilenio en Bogotá y metro en construcción. Brasil tiene metros en São Paulo, Río y otras ciudades con enormes sobrecostos.

**Restricciones:** La Línea 2 del Metro de Lima lleva más de 10 años en construcción con múltiples problemas. La Ley de Endeudamiento 2026 autoriza solo USD 2,840 millones de deuda externa. Cuatro metros nuevos en Lima más tres regionales en un quinquenio es técnica y financieramente inviable.

**Veredicto:** Inviable. No existe capacidad técnica ni financiera para ejecutarlo en 5 años.

## 5. REDUCCIÓN DE ANEMIA INFANTIL AL 20%
**Qué propone:** Reducir la anemia infantil al 20% mediante cobertura universal de vacunación, chequeos preventivos y servicios reforzados.

**Costo estimado:** S/2,500-4,000 millones adicionales en programas nutricionales, acceso a agua potable y servicios de salud.

**Precedentes internacionales:** Chile prácticamente eliminó la anemia infantil en tres décadas mediante suplementación universal y agua potable. Colombia redujo la anemia del 33% al 24% en 10 años. Perú ha tenido programas fallidos (Qali Warma, suplementación de hierro) por problemas de implementación.

**Restricciones:** La anemia infantil afecta al 43.1% de niños menores de 3 años según ENDES 2024. La principal causa es la falta de agua potable segura y alimentación adecuada — no solo la falta de atención médica. La meta del 20% en 5 años requeriría una reducción de más de 23 puntos porcentuales.

**Veredicto:** Baja viabilidad. La meta es muy ambiciosa sin abordar las causas estructurales.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Parcialmente consistente. Fujimori mantiene la disciplina del libre mercado y la Constitución de 1993, lo que limita el gasto discrecional. Sin embargo, sus propuestas de infraestructura de transporte masivo y modernización policial requieren financiamiento que excede el espacio fiscal disponible.

**Restricciones estructurales:** El presupuesto 2026 crece solo 2.3% y la regla fiscal establece un déficit máximo del 1.8% del PBI. Sus propuestas más costosas — metros en Lima y regiones, shock anticorrupción digital — requieren fuentes de financiamiento que el plan no especifica.

**Riesgo institucional:** Sus tres procesos penales por lavado de activos representan el mayor riesgo de gobernabilidad del plan — un presidente con procesos penales activos enfrenta limitaciones políticas que afectan la capacidad de implementación.

El plan tiene objetivos bien identificados y metas verificables, pero subestima los costos de implementación y sobreestima la capacidad de ejecución del Estado peruano en el quinquenio.""",

# ── 168: Rafael López Aliaga (Renovación Popular) ─────────────────────────
"168": """## 1. UNIFICACIÓN DE REGÍMENES TRIBUTARIOS + REDUCCIÓN DEL IGV
**Qué propone:** Unificar todos los regímenes tributarios en uno solo y reducir el IGV para incentivar la formalización.

**Costo estimado:** Depende del nivel al que se reduzca el IGV. Cada punto porcentual de reducción representa ~S/3,500-4,000 millones de menor recaudación.

**Precedentes internacionales:** Estonia tiene un sistema tributario simplificado con resultados positivos. Nueva Zelanda simplificó su GST con un solo régimen con alta efectividad. Chile tiene estructura tributaria más simplificada que Perú con mejores resultados de recaudación.

**Restricciones:** La presión tributaria del Perú es de solo 14.1% del PBI — ya muy baja para el nivel de servicios que el Estado debe proveer. Reducir el IGV sin compensar con otro tributo reduciría aún más los ingresos fiscales ya insuficientes. La unificación de regímenes es técnicamente factible pero requiere apoyo parlamentario y período de transición de 2-3 años.

**Veredicto:** Media viabilidad la unificación de regímenes. Baja viabilidad la reducción del IGV sin compensación.

## 2. META DE 7% DE CRECIMIENTO DEL PBI Y 2 MILLONES DE EMPLEOS
**Qué propone:** Alcanzar el 7% de crecimiento anual del PBI y generar 2 millones de nuevos empleos mediante industrialización.

**Costo estimado:** Requiere inversión privada de USD 15,000-20,000 millones adicionales anuales para sostener ese crecimiento.

**Precedentes internacionales:** Perú creció al 7% en la primera década del siglo (boom de commodities). Corea del Sur sostuvo 7%+ durante 30 años con política industrial activa. Chile no ha superado el 5% sostenido en la última década.

**Restricciones:** El crecimiento potencial del Perú se estima en 2.5-3.5% según el BCRP. El 7% requeriría un salto de productividad sin precedente en un quinquenio. La inversión privada ha caído sistemáticamente desde 2014. La conflictividad social y la inseguridad son los principales obstáculos a la inversión — no la tributación.

**Veredicto:** Inviable como meta quinquenal. Es aspiracional, no técnica.

## 3. TRENES DE ALTA VELOCIDAD LIMA-ICA Y LIMA-TRUJILLO + TÚNEL TRASANDINO
**Qué propone:** Construir trenes de alta velocidad entre Lima-Ica y Lima-Trujillo, y un túnel trasandino.

**Costo estimado:** Un tren de alta velocidad cuesta USD 20-40 millones por kilómetro. Lima-Ica (320 km) = USD 6,400-12,800 millones. Lima-Trujillo (560 km) = USD 11,200-22,400 millones. Túnel trasandino: USD 3,000-5,000 millones adicionales. Total: USD 20,000-40,000 millones.

**Precedentes internacionales:** España construyó la red AVE en 30 años. China construye trenes rápidos (no alta velocidad) a menor costo. México canceló tren Maya por sobrecostos y problemas ambientales.

**Restricciones:** El PBI del Perú es de aproximadamente USD 260,000 millones. Estos tres proyectos representarían entre el 8 y el 15% del PBI — más que todo el gasto de infraestructura acumulado en la última década. La Ley de Endeudamiento 2026 autoriza solo USD 2,840 millones de deuda externa.

**Veredicto:** Inviable. Es la propuesta más costosa y menos viable del campo electoral.

## 4. CENTRAL DE LUCHA CONTRA LA CORRUPCIÓN (CCC)
**Qué propone:** Crear una entidad con poderes plenos para infiltrar y capturar delitos de corrupción en flagrancia.

**Costo estimado:** S/500-1,000 millones en creación de la entidad, personal especializado y equipamiento.

**Precedentes internacionales:** Colombia tiene la Fiscalía General con unidades especializadas anticorrupción. Guatemala tuvo la CICIG (comisión internacional) con resultados positivos hasta su cierre político. Honduras tiene la MACCIH similar.

**Restricciones:** En Perú ya existen la Fiscalía Especializada en Corrupción de Funcionarios (FECOR), la PNP y la Contraloría. El problema no es la ausencia de instituciones sino la captura política de las existentes. Una nueva entidad con "poderes plenos" podría generar conflictos constitucionales con el MP y el PJ.

**Veredicto:** Media viabilidad si se articula con instituciones existentes.

## 5. PENALES DE ALTA MONTAÑA SIN COBERTURA MÓVIL
**Qué propone:** Construir penales en la Cordillera de la Viuda y otras zonas remotas sin cobertura de señal móvil.

**Costo estimado:** S/800-1,500 millones por penal de máxima seguridad. Si son 5 penales: S/4,000-7,500 millones.

**Precedentes internacionales:** El Salvador usa el Centro de Confinamiento del Terrorismo (CECOT) en zonas remotas. Estados Unidos tiene ADX Florence en Colorado (supermáximo). Perú ya tiene penales de alta seguridad como Challapalca (a 4,600 msnm).

**Restricciones:** Perú ya tiene Challapalca cuya efectividad es cuestionada por las condiciones inhumanas. La CIDH ha criticado las condiciones de este penal. Construir nuevos penales remotos sin abordar la sobrepoblación (248% de capacidad según INPE) no resuelve el problema penitenciario de fondo.

**Veredicto:** Baja viabilidad. No resuelve el problema penitenciario estructural.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Parcialmente inconsistente. López Aliaga propone reducir ingresos tributarios (IGV) mientras plantea gasto masivo en infraestructura (trenes de alta velocidad). La meta de 7% de crecimiento no tiene sustento técnico en el contexto fiscal actual. Sus propuestas de trenes de alta velocidad son las más costosas e inviables del campo electoral 2026.

**Restricciones estructurales:** El espacio fiscal del Perú (déficit máximo 1.8% del PBI en 2026, deuda del 32%) no tiene capacidad para financiar proyectos de esta magnitud. La inversión privada no responde automáticamente a señales políticas.

**Fortaleza del plan:** La CCC anticorrupción y la unificación de regímenes tributarios son las propuestas más viables del plan. Su énfasis en la formalización empresarial tiene respaldo técnico internacional.

El plan presenta la brecha más grande entre ambición y viabilidad fiscal del campo electoral 2026. Sus propuestas más emblemáticas son técnicamente inviables en el quinquenio.""",

# ── 169: Ricardo Belmont (Obras) ─────────────────────────────────────────
"169": """## 1. PLAN CHOQUE DE 1,500 OBRAS SOCIALES PARALIZADAS
**Qué propone:** Culminar 1,500 infraestructuras en abandono — escuelas y postas — en un máximo de 60 días desde la identificación hasta la reactivación.

**Costo estimado:** S/4,500-7,500 millones totales (promedio de S/3-5 millones por obra).

**Precedentes internacionales:** Colombia implementó el "Plan de Choque" de infraestructura escolar en 2017 con buenos resultados. Brasil tuvo el PAC educativo con resultados mixtos por corrupción. Chile acelera obras mediante el MOP con plazos contractuales estrictos.

**Restricciones:** El Perú tiene más de 2,500 obras paralizadas según la Contraloría General — no solo 1,500. El plazo de 60 días desde identificación hasta reactivación es técnicamente imposible dado los procesos de licitación (90-180 días mínimo según la Ley de Contrataciones del Estado). La capacidad de supervisión del Estado es limitada para 1,500 obras simultáneas.

**Veredicto:** Media viabilidad si se reforma el marco normativo de contrataciones.

## 2. COBERTURA DE SALUD AL 85% EN CINCO AÑOS
**Qué propone:** Elevar la cobertura de servicios de salud al 85% en cinco años, priorizando zonas rurales y vulnerables.

**Costo estimado:** S/5,000-8,000 millones adicionales en infraestructura, personal y equipamiento en zonas rurales.

**Precedentes internacionales:** Colombia logró cobertura del 95%+ mediante el Sistema General de Seguridad Social en Salud (SGSSS) en 20 años. México alcanzó alta cobertura con el Seguro Popular. Chile tiene cobertura casi universal con sistema mixto.

**Restricciones:** La cobertura actual es del 76% según el MINSA, con brechas severas en zonas rurales. Solo el 50.5% de la población rural tiene acceso efectivo a salud. Pasar del 76% al 85% requiere principalmente infraestructura rural y personal médico — ambos con plazos de formación de 5-7 años.

**Veredicto:** Media viabilidad. La meta es razonable pero el plazo es ajustado.

## 3. REDUCCIÓN DE LA DESNUTRICIÓN INFANTIL AL 10%
**Qué propone:** Reducir la tasa de desnutrición infantil crónica al 10% en cinco años (actualmente en 22% en zonas rurales).

**Costo estimado:** S/3,000-5,000 millones adicionales en programas nutricionales, agua potable y agricultura familiar.

**Precedentes internacionales:** Perú ya logró reducir la desnutrición crónica del 28% al 11% entre 2007-2016 con el programa CRECER. Brasil implementó el "Fome Zero" con resultados positivos. Ecuador redujo la desnutrición crónica del 41% al 27% en una década.

**Restricciones:** La meta del 10% requeriría reducir la desnutrición en 12 puntos porcentuales en 5 años — el mismo ritmo que Perú logró en 9 años durante su mejor período. El acceso a agua potable segura es el determinante principal que requiere infraestructura de largo plazo.

**Veredicto:** Media viabilidad. Perú tiene precedente de logro similar aunque en período más largo.

## 4. PLATAFORMA DIGITAL ÚNICA DE OBRAS PÚBLICAS
**Qué propone:** Sistema público de acceso abierto donde el ciudadano puede reportar incidencias sobre obras públicas con rendición de cuentas trimestral.

**Costo estimado:** S/150-300 millones en sistemas informáticos y capacitación.

**Precedentes internacionales:** Uruguay tiene el sistema SICE exitosamente. Colombia tiene SECOP II para contrataciones. Brasil tiene el Portal de Transparencia con alta efectividad.

**Restricciones:** El Perú ya tiene el INFOBRAS de la Contraloría que registra obras públicas. El problema es la capacidad de acción sobre los datos, no solo la transparencia.

**Veredicto:** Alta viabilidad. Es la propuesta más concreta y ejecutable del plan.

## 5. LEY DE OBRA PÚBLICA CON MANO DE OBRA FORMAL
**Qué propone:** Formalizar el 100% de trabajadores en obras estatales y que 20,000 MYPES del sector construcción accedan a licitaciones.

**Costo estimado:** S/800-1,500 millones en mayor costo laboral de obras + programas de capacitación de MYPES.

**Precedentes internacionales:** Colombia implementó cláusulas laborales en contratos públicos con resultados positivos. México tiene el programa de Compras a MIPYMES con impacto moderado. Chile exige formalidad laboral en contratos estatales desde 2010.

**Restricciones:** El sector construcción tiene 60-70% de informalidad laboral. Exigir formalidad encarecería las obras en 15-25% sin cambiar el sistema de control. Las MYPES de construcción tienen baja capacidad técnica para concursar en licitaciones sin capacitación previa.

**Veredicto:** Media viabilidad si se acompaña de capacitación y gradualidad.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Razonablemente consistente. Belmont no presenta propuestas macroeconómicas radicales ni promesas de gasto sin financiamiento evidente. Su Plan Choque es el más concreto y ejecutable del campo electoral en infraestructura social.

**Restricciones estructurales:** El plazo de 60 días para reactivar obras es la principal inconsistencia — los procesos de contratación pública toman 90-180 días mínimo. La meta de desnutrición al 10% en 5 años requiere el mismo ritmo del mejor período histórico peruano.

**Fortaleza del plan:** La Plataforma Digital de Obras y la Ley de Mano de Obra Formal son las propuestas más viables e institucionalmente valiosas. El Plan Choque tiene alta factibilidad si se reforma el régimen de contrataciones.

El plan es el más pragmático y ejecutable del campo electoral 2026 en infraestructura social, aunque subestima los plazos de los procesos administrativos.""",

# ── 170: José Luna Gálvez (Podemos Perú) ─────────────────────────────────
"170": """## 1. REACTIVACIÓN ECONÓMICA MEDIANTE INVERSIÓN PÚBLICA Y PRIVADA
**Qué propone:** Reactivar la economía con inversión en infraestructura y turismo sin metas específicas.

**Costo estimado:** Sin especificar en el plan de gobierno.

**Precedentes internacionales:** Sin referencias específicas en el plan.

**Restricciones:** La ausencia de metas cuantificables y fuentes de financiamiento hace imposible evaluar la viabilidad técnica. El presupuesto 2026 crece solo 2.3%. La inversión privada no responde a anuncios sin reformas estructurales específicas.

**Veredicto:** No evaluable. El plan carece de especificidad técnica mínima.

## 2. MEJORA DE LA CALIDAD EDUCATIVA Y CONECTIVIDAD DIGITAL
**Qué propone:** Mejorar la calidad educativa y la conectividad digital en las escuelas públicas sin metas específicas.

**Costo estimado:** Sin especificar.

**Precedentes internacionales:** Sin referencias específicas en el plan.

**Restricciones:** Sin metas ni financiamiento especificado. Replicaría propuestas ya existentes del MINEDU sin valor añadido diferencial.

**Veredicto:** No evaluable por falta de especificidad.

## 3. AMPLIACIÓN DE COBERTURA DE SALUD
**Qué propone:** Ampliar la cobertura de salud sin mecanismos de financiamiento claros ni metas verificables.

**Costo estimado:** Sin especificar.

**Restricciones:** El plan es el menos específico del campo electoral en este eje. La ausencia de financiamiento lo hace inviable por omisión más que por inconsistencia.

**Veredicto:** No evaluable.

## 4. INVERSIÓN EN INFRAESTRUCTURA VIAL
**Qué propone:** Inversión en infraestructura vial sin especificidades técnicas, metas ni fuentes de financiamiento.

**Costo estimado:** Sin especificar.

**Restricciones:** Sin diferenciación respecto a los programas ya existentes del MTC. La brecha de infraestructura vial supera los USD 30,000 millones según el MTC.

**Veredicto:** No evaluable.

## 5. PROPUESTAS AMBIENTALES GENÉRICAS
**Qué propone:** Propuestas de sostenibilidad ambiental sin compromisos medibles ni marcos de acción concretos.

**Costo estimado:** Sin especificar.

**Restricciones:** El plan más vago del campo electoral en materia ambiental.

**Veredicto:** No evaluable.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** No evaluable. El plan de gobierno de Podemos Perú es el menos específico del campo electoral — carece de metas cuantificables, fuentes de financiamiento y mecanismos de implementación en la mayoría de sus propuestas.

**Restricciones estructurales:** La ausencia de especificidad técnica es la principal restricción — no se puede evaluar la viabilidad de propuestas que no detallan ni sus objetivos ni sus medios.

**Riesgo institucional:** Las investigaciones de José Luna Gálvez por presunta manipulación de la ONPE y el Consejo Nacional de la Magistratura (CNM) representan el mayor riesgo institucional del campo electoral — amenazan directamente la independencia del sistema electoral y judicial. Este riesgo es independiente de la calidad del plan de gobierno.

El plan es el menos viable técnicamente del campo electoral por su falta de especificidad, y el candidato presenta el mayor riesgo institucional para la democracia por sus antecedentes judiciales.""",

# ── 171: Carlos Álvarez (País para Todos) ─────────────────────────────────
"171": """## 1. BLINDAJE MACROECONÓMICO — DÉFICIT AL 1% DEL PBI
**Qué propone:** Convergencia del déficit fiscal al 1% del PBI, disciplina fiscal y presión tributaria creciente al 17%.

**Costo estimado:** Sin costo adicional — es una restricción fiscal, no un gasto.

**Precedentes internacionales:** Chile mantuvo regla fiscal de balance estructural durante años con buenos resultados. Colombia tiene regla fiscal desde 2011. Perú tuvo regla del 1% antes de la pandemia.

**Restricciones:** El déficit actual es de 2.4% del PBI. Llegar al 1% requiere una consolidación fiscal de 1.4 puntos del PBI — equivalente a S/10,000-12,000 millones de reducción del déficit en el quinquenio. Es técnicamente factible pero políticamente difícil dado las presiones de gasto.

**Veredicto:** Media viabilidad. Requiere disciplina política excepcional.

## 2. REDUCCIÓN DE HOMICIDIOS DE 8.6 A 6 POR 100 MIL HABITANTES
**Qué propone:** Reducir la tasa de homicidios con Plataforma Nacional de Análisis Criminal, control territorial y metas de reducción de victimización.

**Costo estimado:** S/2,500-4,000 millones en modernización policial, tecnología y programas preventivos.

**Precedentes internacionales:** Colombia redujo homicidios del 80 al 24 por 100 mil en 20 años con inversión policial, social y negociaciones. Ecuador tuvo reducción temporal con estado de excepción. El Salvador redujo con mano dura extrema con críticas de DDHH.

**Restricciones:** La tasa de 8.6 por 100 mil en Perú es moderada para la región. La reducción a 6 requiere 30% de mejora — factible en 5 años con inversión sostenida. La Plataforma Nacional de Análisis Criminal es una propuesta técnicamente viable y con precedentes.

**Veredicto:** Alta viabilidad. Es una de las metas más técnicas y alcanzables del campo electoral.

## 3. DIGITALIZACIÓN TOTAL DEL ESTADO E INTEROPERABILIDAD
**Qué propone:** Digitalización completa del Estado con interoperabilidad, plataforma digital única y eliminación radical de trámites.

**Costo estimado:** S/2,000-3,500 millones en sistemas, infraestructura y capacitación.

**Precedentes internacionales:** Estonia tiene el 99% de servicios públicos en línea. Uruguay avanza en transformación digital con buenos resultados. Chile tiene el portal ChileAtiende con alta efectividad. Colombia tiene GovTech Perú como referente.

**Restricciones:** El Perú tiene la PIDE (Plataforma de Interoperabilidad del Estado) desde 2012 con avance limitado. El 40% de entidades estatales no tiene sistemas informáticos básicos. La resistencia burocrática al cambio es el mayor obstáculo.

**Veredicto:** Media viabilidad. Técnicamente factible pero con obstáculos institucionales significativos.

## 4. FAST TRACK PARA INVERSIONES + VENTANILLA ÚNICA TERRITORIAL
**Qué propone:** Aceleración de proyectos de inversión con ventanilla única digital territorial y reducción de plazos de tramitación.

**Costo estimado:** S/500-1,000 millones en sistemas y reforma normativa.

**Precedentes internacionales:** Singapur tiene uno de los sistemas de aprobación de inversiones más rápidos del mundo. Colombia implementó la Unidad de Proyección Normativa con resultados positivos. Chile tiene el MOP con procesos más ágiles que Perú.

**Restricciones:** Perú ya tiene el FIDE (Fast Track) y el APP Perú sin resultados transformadores. El problema no es la norma sino la capacidad de los funcionarios y la conflictividad social en proyectos de inversión.

**Veredicto:** Media viabilidad.

## 5. REDUCCIÓN DE INFORMALIDAD AL 55%
**Qué propone:** Reducir la informalidad laboral del 70.9% al 55% en cinco años.

**Costo estimado:** S/3,000-5,000 millones en programas de formalización, simplificación tributaria y seguridad social simplificada.

**Precedentes internacionales:** Colombia redujo informalidad del 68% al 58% en una década. México tiene 57% de informalidad pese a reformas. Chile tiene 25% tras décadas de política consistente.

**Restricciones:** Reducir la informalidad en 15.9 puntos en 5 años requeriría el doble del ritmo de formalización histórico más exitoso de Perú. El subsidio de seguridad social necesario para el tránsito formal tiene un costo fiscal significativo.

**Veredicto:** Baja viabilidad en el plazo propuesto. Media viabilidad en 10 años.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Razonablemente consistente. Álvarez propone disciplina fiscal y convergencia del déficit al 1% del PBI — coherente con el marco macroeconómico actual. Sus propuestas de gasto no son las más costosas del campo electoral.

**Restricciones estructurales:** La digitalización total del Estado y la reducción de informalidad en 5 años son las propuestas más cuestionables en términos de plazo. La meta de seguridad es la más técnica y alcanzable del plan.

**Fortaleza del plan:** La meta de reducción de homicidios con Plataforma Nacional de Análisis Criminal es la propuesta de seguridad más técnicamente articulada del campo electoral. La disciplina fiscal propuesta es coherente con el marco institucional.

El plan es uno de los más fiscalmente responsables del campo electoral, con la meta de seguridad más técnica. Su principal debilidad es la ambición de reducir la informalidad laboral en 15 puntos en solo cinco años.""",

# ── 172: María Pérez Tello (Primero la Gente) ─────────────────────────────
"172": """## 1. ECONOMÍA DIGITAL, BIOINDUSTRIA Y ACUICULTURA
**Qué propone:** Diversificación productiva con énfasis en economía digital, bioindustria, acuicultura y economía creativa como nuevos motores de crecimiento.

**Costo estimado:** S/3,000-5,000 millones en incentivos, infraestructura digital y centros tecnológicos sectoriales.

**Precedentes internacionales:** Costa Rica atrajo a Intel y empresas tecnológicas con incentivos focalizados y mano de obra calificada. Chile diversificó con salmon, vino y cobre mediante política de clústeres. Colombia desarrolló la economía naranja (economía creativa) con resultados positivos en empleo.

**Restricciones:** El Perú tiene ventajas comparativas reales en acuicultura (trucha, langostinos) y biodiversidad para bioindustria. La economía digital requiere conectividad que el 43% de la población rural aún no tiene. El ecosistema de innovación digital en Perú es incipiente — Lima tiene solo 400 startups activas según CONCYTEC.

**Veredicto:** Media viabilidad. Los sectores elegidos tienen potencial real pero requieren 8-10 años para madurar.

## 2. REDUCCIÓN DE INFORMALIDAD AL 55% CON FAST TRACK PARA INVERSIONES
**Qué propone:** Reducir informalidad al 55% con simplificación de trámites, ventanilla única y fast track para inversiones.

**Costo estimado:** S/2,500-4,000 millones en reforma normativa, sistemas digitales e incentivos tributarios.

**Precedentes internacionales:** Singapur tiene el proceso más ágil de apertura de negocios del mundo (1 día). Colombia redujo trámites con el modelo DOING BUSINESS. Chile tiene procesos de inversión más ágiles que Perú.

**Restricciones:** La informalidad en Perú es estructural y tiene raíces en el acceso al crédito, la cultura empresarial y los sobrecostos laborales — no solo en la tramitología. Reducir 15.9 puntos en 5 años es el mismo cuestionamiento que para los demás candidatos.

**Veredicto:** Media viabilidad la simplificación de trámites. Baja viabilidad la meta de 55% en 5 años.

## 3. DEROGAR LEYES PROCRIMEN Y MODERNIZACIÓN POLICIAL PREDICTIVA
**Qué propone:** Derogar las leyes que debilitaron la capacidad sancionadora del Estado y modernizar la Policía con tecnología predictiva.

**Costo estimado:** S/1,500-2,500 millones en modernización tecnológica policial.

**Precedentes internacionales:** El Salvador derogar normas procesales para endurecer penas. Ecuador implementó tecnología predictiva de delitos con resultados moderados. Colombia usa ShotSpotter y cámaras inteligentes en Bogotá.

**Restricciones:** La derogación de leyes requiere mayoría parlamentaria. La tecnología predictiva requiere bases de datos históricas que la PNP no tiene digitalizadas. El 82% de vehículos policiales no funciona — la tecnología avanzada requiere antes infraestructura básica operativa.

**Veredicto:** Media viabilidad la derogación de leyes. Baja viabilidad la tecnología predictiva sin modernización básica previa.

## 4. UNIVERSALIZAR EDUCACIÓN INICIAL Y MEJORAR CALIDAD DOCENTE
**Qué propone:** Garantizar cobertura universal de educación inicial (3-5 años) y mejorar la calidad docente con carrera pública meritocrática.

**Costo estimado:** S/4,000-6,000 millones adicionales en infraestructura, docentes y materiales.

**Precedentes internacionales:** Chile universalizó pre-kínder y kínder con inversión pública sostenida. México logró 90%+ de cobertura inicial con programa CONFIEP. Ecuador implementó el Programa Creciendo con Nuestros Hijos.

**Restricciones:** La cobertura actual en zonas rurales es del ~65%. La formación de docentes de inicial tarda 4-5 años. La carrera pública magisterial ya existe (Ley 29944) con implementación parcial — la propuesta la fortalecería, no la crearía.

**Veredicto:** Media viabilidad.

## 5. INTEGRAR SISTEMAS DE SALUD CON ÉNFASIS EN ATENCIÓN PRIMARIA
**Qué propone:** Integrar Minsa, EsSalud, FFAA y privados en sistema de cobertura universal efectiva con acceso por DNI.

**Costo estimado:** S/8,000-15,000 millones adicionales para universalizar la cobertura efectiva (no solo nominal).

**Precedentes internacionales:** Chile tiene el Plan AUGE/GES que garantiza 80+ enfermedades con cobertura real. Francia tiene sistema bismarckiano-beveridgiano con integración parcial. Colombia tiene el Sistema General de Seguridad Social en Salud (SGSSS) mixto.

**Restricciones:** La presión tributaria de solo 14.1% del PBI limita severamente el financiamiento universal. La integración de EsSalud y Minsa es técnicamente compleja — requiere modificar normas laborales, tarifarios y sistemas informáticos de dos grandes burocracias.

**Veredicto:** Media viabilidad. El énfasis en atención primaria es correcto pero la integración total tarda más de 5 años.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Razonablemente consistente. Pérez Tello propone inversión privada al 22% del PBI y diversificación productiva sin propuestas de gasto masivo. Sus propuestas son las más equilibradas técnicamente entre ambición y viabilidad.

**Restricciones estructurales:** La integración de sistemas de salud y la reducción de informalidad en 5 años son los principales cuellos de botella. La baja presión tributaria (14.1% del PBI) es la restricción estructural más importante para financiar sus propuestas sociales.

**Fortaleza del plan:** La diversificación productiva en acuicultura, bioindustria y economía digital es la propuesta más pertinente para las ventajas comparativas reales del Perú. La modernización policial con tecnología predictiva tiene precedentes internacionales.

El plan es uno de los más equilibrados técnicamente del campo electoral, con propuestas de diversificación productiva más pertinentes al contexto peruano que los candidatos focalizados en infraestructura masiva.""",

# ── 173: Roberto Sánchez (Juntos por el Perú) ─────────────────────────────
"173": """## 1. NUEVA CONSTITUCIÓN CON ECONOMÍA MIXTA Y SOBERANÍA SOBRE RECURSOS
**Qué propone:** Reforma constitucional para cambiar el modelo económico: Estado recupera soberanía sobre recursos naturales, economía mixta con control de precios en sectores en crisis.

**Costo estimado:** S/200-400 millones en costos del proceso constituyente. Costo económico indirecto: potencial fuga de capitales e incertidumbre para la inversión privada por USD 3,000-8,000 millones en el primer año.

**Precedentes internacionales:** Bolivia reformó la Constitución en 2009 con asamblea constituyente — recuperó recursos gasíferos con impacto positivo en ingresos fiscales pero tensiones con inversión privada. Venezuela reformó la Constitución en 1999 con efectos económicos negativos de largo plazo. Ecuador rechazó su nueva constitución en referéndum 2022.

**Restricciones:** En Perú, la reforma constitucional requiere dos legislaturas consecutivas o referéndum. La Constitución de 1993 ha sido el marco del crecimiento del período 2000-2014. Los mercados internacionales reaccionan negativamente a señales de cambio del modelo de inversión — la prima de riesgo país podría subir 200-300 puntos básicos.

**Veredicto:** Baja viabilidad política. Alta viabilidad técnica-legal pero con alto costo económico de transición.

## 2. PRESIÓN TRIBUTARIA AL 25% DEL PBI
**Qué propone:** Elevar la presión tributaria del 14.1% actual al 25% del PBI mediante impuesto a sobreganancias mineras y reforma tributaria progresiva.

**Costo estimado:** Sin costo directo — busca aumentar ingresos. El impuesto a sobreganancias mineras recaudaría S/8,000-15,000 millones adicionales anuales según estimaciones de CIES.

**Precedentes internacionales:** Chile aplicó royalty minero con recaudación significativa. Bolivia nacionalizó el gas con alta recaudación inicial pero desincentivó la exploración. Perú ya tuvo el Gravamen Especial a la Minería (GEM) entre 2011-2016 con recaudación moderada.

**Restricciones:** Pasar del 14.1% al 25% requeriría aumentar la recaudación en USD 15,000-18,000 millones anuales — prácticamente duplicar los ingresos tributarios. Es la meta de presión tributaria más ambiciosa del campo electoral y excede en 4-5 puntos el promedio de América Latina. Los contratos de estabilidad jurídica limitan la aplicación de nuevos tributos a muchos proyectos mineros.

**Veredicto:** Inviable en el quinquenio. Requeriría 20+ años de reforma tributaria sostenida.

## 3. INDUSTRIALIZACIÓN NACIONAL — PROHIBIR EXPORTAR MINERALES SIN PROCESAR
**Qué propone:** Prohibición gradual de exportar minerales sin procesamiento para industrializar la economía y generar valor agregado.

**Costo estimado:** Costo fiscal indirecto: el sector minero representa el 60% de las exportaciones. Restricciones a la exportación reducirían ingresos fiscales por S/10,000-15,000 millones anuales durante la transición.

**Precedentes internacionales:** Indonesia prohibió exportar níquel sin procesar en 2020 — logró atraer inversión en fundición pero generó disputa con la OMC. Bolivia procesó gas pero con alta inversión estatal. Chile exporta cobre refinado con mayor valor agregado que el promedio regional.

**Restricciones:** El Perú no tiene la capacidad de refinación industrial para el cobre, oro y zinc que exporta. Construir esa capacidad requeriría USD 20,000-30,000 millones de inversión privada. Las restricciones a la exportación violarían los TLC vigentes con EEUU, China y la UE.

**Veredicto:** Inviable sin inversión industrial masiva previa y renegociación de TLCs.

## 4. REDES INTEGRADAS DE SALUD EN TODO EL TERRITORIO
**Qué propone:** Implementar Redes Integradas de Salud (RIS) en todo el territorio nacional con tiempo máximo de espera de 72 horas para diagnósticos.

**Costo estimado:** S/6,000-10,000 millones adicionales en infraestructura, personal y equipamiento para integrar los sistemas de salud.

**Precedentes internacionales:** Costa Rica tiene el sistema CCSS (Caja Costarricense de Seguro Social) integrado y universal. Cuba tiene redes de salud integradas territorialmente. España tiene el Sistema Nacional de Salud con redes regionales integradas.

**Restricciones:** La integración de Minsa, EsSalud y gobiernos regionales requiere reforma normativa compleja. El tiempo de espera de 72 horas para diagnósticos es inviable sin inversión masiva en equipamiento — el Perú tiene 1.6 camas hospitalarias por 1,000 habitantes (OPS recomienda 3).

**Veredicto:** Media viabilidad la integración en redes. Baja viabilidad la meta de 72 horas en 5 años.

## 5. GASTO EN EDUCACIÓN AL 6% DEL PBI
**Qué propone:** Aumentar el gasto educativo al 6% del PBI con salario mínimo de 1 UIT para docentes e ingreso libre a educación superior.

**Costo estimado:** El gasto educativo actual es del ~4% del PBI. Elevar al 6% requiere S/14,000-18,000 millones adicionales anuales.

**Precedentes internacionales:** Cuba invierte el 13% del PBI en educación. Costa Rica invierte el 8%+. Chile invierte el 5.7%. La UNESCO recomienda el 6% como mínimo para países en desarrollo.

**Restricciones:** Con la presión tributaria del 14.1% del PBI, elevar el gasto educativo al 6% significaría destinar más del 40% de todos los ingresos tributarios solo a educación — sin espacio para salud, seguridad, infraestructura o servicio de la deuda. El ingreso libre a la educación superior sin selectividad tiene evidencia mixta sobre calidad.

**Veredicto:** Baja viabilidad en el contexto fiscal actual sin reforma tributaria previa.

## 📊 VEREDICTO GLOBAL
**Coherencia fiscal:** Gravemente inconsistente. La combinación de reforma constitucional del modelo económico, presión tributaria al 25% del PBI, industrialización con restricciones a la exportación minera y gasto educativo al 6% del PBI es el plan más fiscalmente radical del campo electoral. El costo de transición — incertidumbre para la inversión, fuga de capitales, caída de exportaciones durante la transición industrial — generaría una recesión en los primeros años de gobierno.

**Restricciones estructurales:** La interdependencia fiscal del Perú con el sector extractivo (60% de exportaciones, 30%+ de ingresos tributarios) hace que la transición industrial sin inversión previa sea el mayor riesgo macroeconómico del plan. La nueva Constitución, aunque técnicamente viable, generaría incertidumbre de inversión que el plan no aborda.

**Fortaleza del plan:** Las Redes Integradas de Salud y el aumento del gasto educativo son objetivos socialmente valiosos y técnicamente correctos — el problema es el plazo y el financiamiento. La reforma tributaria progresiva tiene respaldo técnico internacional si se implementa gradualmente.

El plan tiene la mayor coherencia social e ideológica del campo electoral pero la menor viabilidad fiscal en el quinquenio. Su implementación generaría una transición económica turbulenta que los propios sectores que busca beneficiar terminarían pagando."""

}

async def insertar_todo():
    from app.models.candidato import CacheAnalisis

    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    print(f"Insertando {len(VIABILIDADES)} análisis de viabilidad...")

    async with async_session() as db:
        for clave, texto in VIABILIDADES.items():
            try:
                stmt = pg_insert(CacheAnalisis).values(
                    tipo="viabilidad",
                    clave=clave,
                    contenido=texto
                ).on_conflict_do_update(
                    index_elements=["tipo", "clave"],
                    set_={"contenido": texto}
                )
                await db.execute(stmt)
                print(f"  ✅ viabilidad:{clave}")
            except Exception as e:
                print(f"  ❌ viabilidad:{clave}: {e}")

        await db.commit()

    await engine.dispose()
    print(f"\n🎉 ¡COMPLETADO! {len(VIABILIDADES)} análisis de viabilidad insertados en producción.")

asyncio.run(insertar_todo())
