import asyncio
from app.database import AsyncSessionLocal
from app.models.candidato import PartidoPolitico, Candidato, Tema


async def seed():
    async with AsyncSessionLocal() as db:

        datos = [
            (
                "AHORA NACION - AN",
                "AN",
                "Pablo Alfonso Lopez Chau Nava",
            ),
            (
                "ALIANZA ELECTORAL VENCEREMOS",
                "AEV",
                "Ronald Darwin Atencio Sotomayor",
            ),
            (
                "ALIANZA PARA EL PROGRESO",
                "APP",
                "César Acuña Peralta",
            ),
            (
                "AVANZA PAIS - PARTIDO DE INTEGRACION SOCIAL",
                "AP",
                "José Daniel Williams Zapata",
            ),
            (
                "FE EN EL PERU",
                "FEP",
                "Álvaro Gonzalo Paz de la Barra Freigeiro",
            ),
            (
                "FUERZA POPULAR",
                "FP",
                "Keiko Sofia Fujimori Higuchi",
            ),
            (
                "FUERZA Y LIBERTAD",
                "FYL",
                "Fiorella Giannina Molinelli Aristondo",
            ),
            (
                "JUNTOS POR EL PERU",
                "JPP",
                "Roberto Helbert Sanchez Palomino",
            ),
            (
                "LIBERTAD POPULAR",
                "LP",
                "Rafael Jorge Belaunde Llosa",
            ),
            (
                "PARTIDO APRISTA PERUANO",
                "PAP",
                "Pitter Enrique Valderrama Peña",
            ),
            (
                "PARTIDO CIVICO OBRAS",
                "PCO",
                "Ricardo Pablo Belmont Cassinelli",
            ),
            (
                "PARTIDO DEL BUEN GOBIERNO",
                "PBG",
                "Jorge Nieto Montesinos",
            ),
            (
                "PARTIDO DEMOCRATA UNIDO PERU",
                "PDU",
                "Charlie Carrasco Salazar",
            ),
            (
                "PARTIDO DEMOCRATA VERDE",
                "PDV",
                "Alex Gonzales Castillo",
            ),
            (
                "PARTIDO DEMOCRATICO FEDERAL",
                "PDF",
                "Armando Joaquin Masse Fernandez",
            ),
            (
                "PARTIDO DEMOCRATICO SOMOS PERU",
                "SP",
                "George Patrick Forsyth Sommer",
            ),
            (
                "PARTIDO FRENTE DE LA ESPERANZA 2021",
                "FE",
                "Luis Fernando Olivera Vega",
            ),
            (
                "PARTIDO MORADO",
                "PM",
                "Mesías Antonio Guevara Amasifuén",
            ),
            (
                "PARTIDO PAIS PARA TODOS",
                "PPT",
                "Carlos Gonsalo Alvarez Loayza",
            ),
            (
                "PARTIDO PATRIOTICO DEL PERU",
                "PPP",
                "Herbert Caller Gutierrez",
            ),
            (
                "PARTIDO POLITICO COOPERACION POPULAR",
                "CP",
                "Yonhy Lescano Ancieta",
            ),
            (
                "PARTIDO POLITICO INTEGRIDAD DEMOCRATICA",
                "ID",
                "Wolfgang Mario Grozo Costa",
            ),
            (
                "PARTIDO POLITICO NACIONAL PERU LIBRE",
                "PL",
                "Vladimir Roy Cerrón Rojas",
            ),
            (
                "PARTIDO POLITICO PERU ACCION",
                "PPA",
                "Francisco Ernesto Diez-Canseco Távara",
            ),
            (
                "PARTIDO POLITICO PERU PRIMERO",
                "PP1",
                "Mario Enrique Vizcarra Cornejo",
            ),
            (
                "PARTIDO POLITICO PRIN",
                "PRIN",
                "Walter Gilmer Chirinos Purizaga",
            ),
            (
                "PARTIDO SICREO",
                "SC",
                "Alfonso Carlos Espá y Garcés-Alvear",
            ),
            (
                "PERU MODERNO",
                "PEMO",
                "Carlos Ernesto Jaico Carranza",
            ),
            (
                "PODEMOS PERU",
                "PODE",
                "José Leon Luna Galvez",
            ),
            (
                "PRIMERO LA GENTE - COMUNIDAD, ECOLOGIA, "
                "LIBERTAD Y PROGRESO",
                "PLG",
                "María Soledad Perez Tello de Rodriguez",
            ),
            (
                "PROGRESEMOS",
                "PROG",
                "Paul Davis Jaimes Blanco",
            ),
            (
                "RENOVACION POPULAR",
                "RP",
                "Rafael Bernardo Lopez Aliaga Cazorla",
            ),
            (
                "SALVEMOS AL PERU",
                "SAP",
                "Antonio Ortiz Villano",
            ),
            (
                "UN CAMINO DIFERENTE",
                "UCD",
                "Rosario del Pilar Fernandez Bazan",
            ),
            (
                "UNIDAD NACIONAL",
                "UN",
                "Roberto Enrique Chiabra Leon",
            ),
        ]

        for nombre_partido, siglas, nombre_candidato in datos:
            partido = PartidoPolitico(
                nombre=nombre_partido,
                siglas=siglas
            )
            db.add(partido)
            await db.flush()

            candidato = Candidato(
                partido_id=partido.id,
                nombre=nombre_candidato,
                fuente_jne="https://votoinformado.jne.gob.pe"
            )
            db.add(candidato)

        await db.flush()

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
