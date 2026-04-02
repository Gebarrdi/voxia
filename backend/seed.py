import asyncio
from app.database import AsyncSessionLocal
from app.models.candidato import PartidoPolitico, Candidato, Tema


async def seed():
    async with AsyncSessionLocal() as db:

        datos = [
            ("AHORA NACION - AN", "AN",
             "Pablo Alfonso Lopez Chau Nava",
             "https://mpesije.jne.gob.pe/apidocs/"
             "ddfa74eb-cae3-401c-a34c-35543ae83c57.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2980.jpg"),
            ("ALIANZA ELECTORAL VENCEREMOS", "AEV",
             "Ronald Darwin Atencio Sotomayor",
             "https://mpesije.jne.gob.pe/apidocs/"
             "bac0288d-3b21-45ac-8849-39f9177fb020.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/3025.jpg"),
            ("ALIANZA PARA EL PROGRESO", "APP",
             "César Acuña Peralta",
             "https://mpesije.jne.gob.pe/apidocs/"
             "d6fe3cac-7061-474b-8551-0aa686a54bad.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/1257.jpg"),
            ("AVANZA PAIS - PARTIDO DE INTEGRACION SOCIAL", "AP",
             "José Daniel Williams Zapata",
             "https://mpesije.jne.gob.pe/apidocs/"
             "b60c471f-a6bb-4b42-a4b2-02ea38acbb0d.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2173.jpg"),
            ("FE EN EL PERU", "FEP",
             "Álvaro Gonzalo Paz de la Barra Freigeiro",
             "https://votoinformado.jne.gob.pe/assets/images/"
             "candidatos/ALVARO%20PAZ%20DE%20LA%20BARRA.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2898.jpg"),
            ("FUERZA POPULAR", "FP",
             "Keiko Sofia Fujimori Higuchi",
             "https://mpesije.jne.gob.pe/apidocs/"
             "251cd1c0-acc7-4338-bd8a-439ccb9238d0.jpeg",
             "https://votoinformado.jne.gob.pe/LogoOp/1366.jpg"),
            ("FUERZA Y LIBERTAD", "FYL",
             "Fiorella Giannina Molinelli Aristondo",
             "https://mpesije.jne.gob.pe/apidocs/"
             "1de656b5-7593-4c60-ab7a-83d618a3d80d.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/3024.jpg"),
            ("JUNTOS POR EL PERU", "JPP",
             "Roberto Helbert Sanchez Palomino",
             "https://mpesije.jne.gob.pe/apidocs/"
             "bb7c7465-9c6e-44eb-ac7d-e6cc7f872a1a.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/1264.jpg"),
            ("LIBERTAD POPULAR", "LP",
             "Rafael Jorge Belaunde Llosa",
             "https://mpesije.jne.gob.pe/apidocs/"
             "3302e45b-55c8-4979-a60b-2b11097abf1d.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2933.jpg"),
            ("PARTIDO APRISTA PERUANO", "PAP",
             "Pitter Enrique Valderrama Peña",
             "https://mpesije.jne.gob.pe/apidocs/"
             "d72c4b29-e173-42b8-b40d-bdb6d01a526a.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2930.jpg"),
            ("PARTIDO CIVICO OBRAS", "PCO",
             "Ricardo Pablo Belmont Cassinelli",
             "https://mpesije.jne.gob.pe/apidocs/"
             "78647f15-d5d1-4ed6-8ac6-d599e83eeea3.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2941.jpg"),
            ("PARTIDO DEL BUEN GOBIERNO", "PBG",
             "Jorge Nieto Montesinos",
             "https://mpesije.jne.gob.pe/apidocs/"
             "9ae56ed5-3d0f-49ff-8bb9-0390bad71816.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2961.jpg"),
            ("PARTIDO DEMOCRATA UNIDO PERU", "PDU",
             "Charlie Carrasco Salazar",
             "https://mpesije.jne.gob.pe/apidocs/"
             "12fa17db-f28f-4330-9123-88549539b538.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2867.jpg"),
            ("PARTIDO DEMOCRATA VERDE", "PDV",
             "Alex Gonzales Castillo",
             "https://mpesije.jne.gob.pe/apidocs/"
             "c0ae56bf-21c1-4810-890a-b25c8465bdd9.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2895.jpg"),
            ("PARTIDO DEMOCRATICO FEDERAL", "PDF",
             "Armando Joaquin Masse Fernandez",
             "https://mpesije.jne.gob.pe/apidocs/"
             "cb1adeb7-7d2f-430c-ae87-519137d8edfa.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2986.jpg"),
            ("PARTIDO DEMOCRATICO SOMOS PERU", "SP",
             "George Patrick Forsyth Sommer",
             "https://mpesije.jne.gob.pe/apidocs/"
             "b1d60238-c797-4cba-936e-f13de6a34cc7.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/14.jpg"),
            ("PARTIDO FRENTE DE LA ESPERANZA 2021", "FE",
             "Luis Fernando Olivera Vega",
             "https://mpesije.jne.gob.pe/apidocs/"
             "3e2312e1-af79-4954-abfa-a36669c1a9e9.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2857.jpg"),
            ("PARTIDO MORADO", "PM",
             "Mesías Antonio Guevara Amasifuén",
             "https://mpesije.jne.gob.pe/apidocs/"
             "1b861ca7-3a5e-48b4-9024-08a92371e33b.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2840.jpg"),
            ("PARTIDO PAIS PARA TODOS", "PPT",
             "Carlos Gonsalo Alvarez Loayza",
             "https://mpesije.jne.gob.pe/apidocs/"
             "2bd18177-d665-413d-9694-747d729d3e39.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2956.jpg"),
            ("PARTIDO PATRIOTICO DEL PERU", "PPP",
             "Herbert Caller Gutierrez",
             "https://mpesije.jne.gob.pe/apidocs/"
             "6ad6c5ff-0411-4ddd-9cf7-b0623f373fcf.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2869.jpg"),
            ("PARTIDO POLITICO COOPERACION POPULAR", "CP",
             "Yonhy Lescano Ancieta",
             "https://mpesije.jne.gob.pe/apidocs/"
             "b9db2b5c-02ff-4265-ae51-db9b1001ad70.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2995.jpg"),
            ("PARTIDO POLITICO INTEGRIDAD DEMOCRATICA", "ID",
             "Wolfgang Mario Grozo Costa",
             "https://mpesije.jne.gob.pe/apidocs/"
             "064360d1-ce49-4abe-939c-f4de8b0130a2.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2985.jpg"),
            ("PARTIDO POLITICO NACIONAL PERU LIBRE", "PL",
             "Vladimir Roy Cerrón Rojas",
             "https://mpesije.jne.gob.pe/apidocs/"
             "82ee0ff2-2336-4aba-9590-e576f7564315.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2218.jpg"),
            ("PARTIDO POLITICO PERU ACCION", "PPA",
             "Francisco Ernesto Diez-Canseco Távara",
             "https://mpesije.jne.gob.pe/apidocs/"
             "2d1bf7f2-6e88-4ea9-8ed2-975c1ae5fb92.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2932.jpg"),
            ("PARTIDO POLITICO PERU PRIMERO", "PP1",
             "Mario Enrique Vizcarra Cornejo",
             "https://mpesije.jne.gob.pe/apidocs/"
             "ee7a080e-bc81-4c81-9e5e-9fd95ff459ab.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2925.jpg"),
            ("PARTIDO POLITICO PRIN", "PRIN",
             "Walter Gilmer Chirinos Purizaga",
             "https://mpesije.jne.gob.pe/apidocs/"
             "a2d0f631-fe47-4c41-92ba-7ed9f4095520.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2921.jpg"),
            ("PARTIDO SICREO", "SC",
             "Alfonso Carlos Espá y Garcés-Alvear",
             "https://mpesije.jne.gob.pe/apidocs/"
             "85935f77-6c46-4eab-8c7e-2494ffbcece0.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2935.jpg"),
            ("PERU MODERNO", "PEMO",
             "Carlos Ernesto Jaico Carranza",
             "https://mpesije.jne.gob.pe/apidocs/"
             "7d91e14f-4417-4d61-89ba-3e686dafaa95.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2924.jpg"),
            ("PODEMOS PERU", "PODE",
             "José Leon Luna Galvez",
             "https://mpesije.jne.gob.pe/apidocs/"
             "a669a883-bf8a-417c-9296-c14b943c3943.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2731.jpg"),
            ("PRIMERO LA GENTE - COMUNIDAD, ECOLOGIA, "
             "LIBERTAD Y PROGRESO", "PLG",
             "María Soledad Perez Tello de Rodriguez",
             "https://mpesije.jne.gob.pe/apidocs/"
             "073703ca-c427-44f0-94b1-a782223a5e10.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2931.jpg"),
            ("PROGRESEMOS", "PROG",
             "Paul Davis Jaimes Blanco",
             "https://mpesije.jne.gob.pe/apidocs/"
             "929e1a63-335d-4f3a-ba26-f3c7ff136213.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2967.jpg"),
            ("RENOVACION POPULAR", "RP",
             "Rafael Bernardo Lopez Aliaga Cazorla",
             "https://mpesije.jne.gob.pe/apidocs/"
             "b2e00ae2-1e50-4ad3-a103-71fc7e4e8255.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/22.jpg"),
            ("SALVEMOS AL PERU", "SAP",
             "Antonio Ortiz Villano",
             "https://mpesije.jne.gob.pe/apidocs/"
             "8e6b9124-2883-4143-8768-105f2ce780eb.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2927.jpg"),
            ("UN CAMINO DIFERENTE", "UCD",
             "Rosario del Pilar Fernandez Bazan",
             "https://mpesije.jne.gob.pe/apidocs/"
             "ac0b0a59-ead5-4ef1-8ef8-8967e322d6ca.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/2998.jpg"),
            ("UNIDAD NACIONAL", "UN",
             "Roberto Enrique Chiabra Leon",
             "https://mpesije.jne.gob.pe/apidocs/"
             "5c703ce9-ba1e-4490-90bf-61006740166f.jpg",
             "https://votoinformado.jne.gob.pe/LogoOp/3023.jpg"),
        ]

        for (nombre_partido, siglas, nombre_candidato, foto_url,
             logo_url) in datos:
            partido = PartidoPolitico(
                nombre=nombre_partido,
                siglas=siglas,
                logo_url=logo_url
            )
            db.add(partido)
            await db.flush()

            candidato = Candidato(
                partido_id=partido.id,
                nombre=nombre_candidato,
                foto_url=foto_url,
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
        print(f"   {len(datos)} candidatos con fotos y logos oficiales JNE")
        print(f"   {len(temas)} temas")


if __name__ == "__main__":
    asyncio.run(seed())
