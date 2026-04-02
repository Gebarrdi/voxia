# seed.py — candidatos presidenciales reales Peru 2026
import asyncio
from app.database import AsyncSessionLocal
from app.models.candidato import PartidoPolitico, Candidato, Tema


async def seed():
    async with AsyncSessionLocal() as db:

        # Partidos y candidatos reales JNE 2026
        datos = [
            ("Fuerza Popular", "FP",
             "Keiko Sofia Fujimori Higuchi",
             "Candidata presidencial por Fuerza Popular. Ex "
             "congresista y tres veces candidata presidencial. "
             "Hija del ex presidente Alberto Fujimori."),
            ("Alianza para el Progreso", "APP",
             "César Acuña Peralta",
             "Candidato presidencial por APP. Ex gobernador "
             "regional de La Libertad y fundador de la "
             "Universidad César Vallejo."),
            ("Renovación Popular", "RP",
             "Rafael López Aliaga",
             "Candidato presidencial por Renovación Popular. "
             "Empresario del sector transporte y ex candidato "
             "presidencial 2021."),
            ("Avanza País", "AP",
             "José Daniel Williams Zapata",
             "Candidato presidencial por Avanza País. Ex "
             "congresista y ex presidente del Congreso de la "
             "República."),
            ("Perú Libre", "PL",
             "Vladimir Cerrón Rojas",
             "Candidato presidencial por Perú Libre. Ex "
             "gobernador regional de Junín. Tiene condena por "
             "corrupción."),
            ("Somos Perú", "SP",
             "George Forsyth Sommer",
             "Candidato presidencial por Somos Perú. Ex alcalde "
             "de La Victoria y ex futbolista profesional."),
            ("Partido Aprista Peruano", "PAP",
             "Pitter Enrique Valderrama Peña",
             "Candidato presidencial por el APRA. Secretario "
             "político nacional del histórico partido aprista."),
            ("Alianza Electoral Venceremos", "AEV",
             "Ronald Darwin Atencio Sotomayor",
             "Candidato presidencial por Alianza Venceremos. "
             "Abogado defensor de causas políticas."),
            ("Ahora Nación", "AN",
             "Pablo Alfonso Lopez Chau Nava",
             "Candidato presidencial por Ahora Nación. Ex "
             "rector de la Universidad Nacional de Ingeniería."),
            ("Fe en el Perú", "FEP",
             "Álvaro Gonzalo Paz de la Barra Freigeiro",
             "Candidato presidencial por Fe en el Perú. Ex "
             "alcalde del distrito de La Molina."),
            ("Fuerza y Libertad", "FYL",
             "Fiorella Giannina Molinelli Aristondo",
             "Candidata presidencial por Fuerza y Libertad. Ex "
             "ministra de Salud durante el gobierno de Martín "
             "Vizcarra."),
            ("Juntos por el Perú", "JPP",
             "Roberto Helbert Sanchez Palomino",
             "Candidato presidencial por Juntos por el Perú. Ex "
             "ministro de Comercio Exterior y Turismo."),
            ("Libertad Popular", "LP",
             "Rafael Jorge Belaunde Llosa",
             "Candidato presidencial por Libertad Popular. "
             "Sobrino del ex presidente Fernando Belaunde "
             "Terry."),
            ("Partido Cívico Obras", "PCO",
             "Ricardo Pablo Belmont Cassinelli",
             "Candidato presidencial por Partido Cívico Obras. "
             "Ex alcalde de Lima Metropolitana en los años 90."),
            ("Partido del Buen Gobierno", "PBG",
             "Jorge Nieto Montesinos",
             "Candidato presidencial por Partido del Buen "
             "Gobierno. Ex ministro de Educación y ex ministro "
             "de Defensa."),
            ("Partido Demócrata Unido Perú", "PDU",
             "Charlie Carrasco Salazar",
             "Candidato presidencial por Demócrata Unido Perú. "
             "Político con trayectoria regional."),
            ("Partido Morado", "PM",
             "Mesías Guevara Amasifuén",
             "Candidato presidencial por el Partido Morado. Ex "
             "gobernador regional de Cajamarca."),
            ("Cooperación Popular", "CP",
             "Yonhy Lescano Ancieta",
             "Candidato presidencial por Cooperación Popular. Ex "
             "congresista y ex candidato presidencial 2021 por "
             "Acción Popular."),
            ("Partido Democrático Federal", "PDF",
             "Armando Massé Rivera",
             "Candidato presidencial por el Partido Democrático "
             "Federal. Empresario con trayectoria política."),
            ("Integridad Democrática", "ID",
             "Wolfgang Grozo Oporto",
             "Candidato presidencial por Integridad Democrática. "
             "Profesional con trayectoria en gestión pública."),
            ("Perú Moderno", "PEMO",
             "Carlos Jaico Carranza",
             "Candidato presidencial por Perú Moderno. Ex "
             "secretario general de la Presidencia de la "
             "República."),
            ("Salvemos al Perú", "SAP",
             "Antonio Ortiz Villano",
             "Candidato presidencial por Salvemos al Perú. "
             "Empresario elegido candidato tras empate en "
             "proceso interno."),
            ("Sí Creo", "SC",
             "Carlos Espá Palacios",
             "Candidato presidencial por Sí Creo. Profesional "
             "con enfoque en políticas sociales."),
            ("Frente de la Esperanza", "FE",
             "Fernando Olivera Vega",
             "Candidato presidencial por Frente de la Esperanza. "
             "Ex ministro del Interior y fundador del FIM."),
            ("Progresemos", "PROG",
             "Paul Jaimes Cárdenas",
             "Candidato presidencial por Progresemos. Político "
             "con trayectoria en gestión regional."),
            ("PRIN", "PRIN",
             "Walter Chirinos Chirinos",
             "Candidato presidencial por PRIN. Político con "
             "respaldo unánime de delegados del partido."),
            ("Un Camino Diferente", "UCD",
             "Rosario Fernández Figueroa",
             "Candidata presidencial por Un Camino Diferente. Ex "
             "ministra de Justicia del gobierno de Alan García."),
            ("Partido Patriótico del Perú", "PPP",
             "Herbert Caller Ferreyra",
             "Candidato presidencial por el Partido Patriótico "
             "del Perú."),
            ("Partido de la Gente", "PG",
             "George Forsyth Sommer",
             "Candidato con trayectoria en gestión municipal en "
             "Lima."),
            ("Podemos Perú", "PP",
             "José Luna Gálvez",
             "Candidato presidencial por Podemos Perú. Ex "
             "congresista y empresario del sector educativo."),
            ("Acción Popular", "ACPop",
             "Alfredo Barnechea García",
             "Candidato presidencial por Acción Popular. Ex "
             "candidato presidencial 2016 y escritor."),
            ("Partido Humanista Peruano", "PHP",
             "Sigrid Bazán Ferreyra",
             "Candidata presidencial por el Partido Humanista. "
             "Ex congresista y activista de derechos humanos."),
            ("Victoria Nacional", "VN",
             "Richard Swing",
             "Candidato presidencial por Victoria Nacional. "
             "Cantante y personaje mediático."),
            ("Partido Verde", "PV",
             "Marco Arana Zegarra",
             "Candidato presidencial por el Partido Verde. "
             "Sacerdote, ex congresista y activista "
             "medioambiental."),
            ("Alianza País", "ALIPA",
             "Óscar Ugarte Ubilluz",
             "Candidato presidencial por Alianza País. Ex "
             "ministro de Salud durante el gobierno de Alan "
             "García."),
        ]

        # Crear partidos y candidatos
        for nombre_partido, siglas, nombre_candidato, biografia in datos:
            partido = PartidoPolitico(
                nombre=nombre_partido,
                siglas=siglas
            )
            db.add(partido)
            await db.flush()

            candidato = Candidato(
                partido_id=partido.id,
                nombre=nombre_candidato,
                biografia=biografia,
                fuente_jne="https://votoinformado.jne.gob.pe"
            )
            db.add(candidato)

        await db.flush()

        # Temas
        temas = [
            Tema(nombre="Economía", icono="chart-bar",
                 descripcion="Política económica, empleo y desarrollo"),
            Tema(nombre="Seguridad", icono="shield",
                 descripcion="Seguridad ciudadana y crimen organizado"),
            Tema(nombre="Educación", icono="book",
                 descripcion="Política educativa y calidad"),
            Tema(nombre="Salud", icono="heart",
                 descripcion="Sistema de salud y cobertura"),
            Tema(nombre="Corrupción", icono="scale",
                 descripcion="Lucha anticorrupción e institucionalidad"),
            Tema(nombre="Medio Ambiente", icono="leaf",
                 descripcion="Recursos naturales y cambio climático"),
        ]
        for tema in temas:
            db.add(tema)

        await db.commit()
        print("✅ Datos cargados correctamente")
        print(f"   {len(datos)} candidatos presidenciales reales")
        print(f"   {len(temas)} temas")


if __name__ == "__main__":
    asyncio.run(seed())
