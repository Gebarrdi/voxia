import asyncio
from app.database import AsyncSessionLocal
from app.models.candidato import PartidoPolitico, Candidato, Tema


async def seed():
    async with AsyncSessionLocal() as db:

        datos = [
            (
                "ALIANZA PARA EL PROGRESO",
                "APP",
                "César Acuña Peralta",
                "https://mpesije.jne.gob.pe/apidocs/"
                "d6fe3cac-7061-474b-8551-0aa686a54bad.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/1257.jpg",
            ),
            (
                "AHORA NACION - AN",
                "AN",
                "Pablo Alfonso Lopez Chau Nava",
                "https://mpesije.jne.gob.pe/apidocs/"
                "ddfa74eb-cae3-401c-a34c-35543ae83c57.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2980.jpg",
            ),
            (
                "PARTIDO FRENTE DE LA ESPERANZA 2021",
                "FE",
                "Luis Fernando Olivera Vega",
                "https://mpesije.jne.gob.pe/apidocs/"
                "3e2312e1-af79-4954-abfa-a36669c1a9e9.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2857.jpg",
            ),
            (
                "FUERZA POPULAR",
                "FP",
                "Keiko Sofia Fujimori Higuchi",
                "https://mpesije.jne.gob.pe/apidocs/"
                "251cd1c0-acc7-4338-bd8a-439ccb9238d0.jpeg",
                "https://votoinformado.jne.gob.pe/LogoOp/1366.jpg",
            ),
            (
                "PARTIDO DEL BUEN GOBIERNO",
                "PBG",
                "Jorge Nieto Montesinos",
                "https://mpesije.jne.gob.pe/apidocs/"
                "9ae56ed5-3d0f-49ff-8bb9-0390bad71816.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2961.jpg",
            ),
            (
                "RENOVACION POPULAR",
                "RP",
                "Rafael Bernardo Lopez Aliaga Cazorla",
                "https://mpesije.jne.gob.pe/apidocs/"
                "b2e00ae2-1e50-4ad3-a103-71fc7e4e8255.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/22.jpg",
            ),
            (
                "PARTIDO CIVICO OBRAS",
                "PCO",
                "Ricardo Pablo Belmont Cassinelli",
                "https://mpesije.jne.gob.pe/apidocs/"
                "78647f15-d5d1-4ed6-8ac6-d599e83eeea3.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2941.jpg",
            ),
            (
                "PODEMOS PERU",
                "PODE",
                "José Leon Luna Galvez",
                "https://mpesije.jne.gob.pe/apidocs/"
                "a669a883-bf8a-417c-9296-c14b943c3943.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2731.jpg",
            ),
            (
                "PARTIDO PAIS PARA TODOS",
                "PPT",
                "Carlos Gonsalo Alvarez Loayza",
                "https://mpesije.jne.gob.pe/apidocs/"
                "2bd18177-d665-413d-9694-747d729d3e39.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2956.jpg",
            ),
            (
                "PRIMERO LA GENTE - COMUNIDAD, ECOLOGIA, "
                "LIBERTAD Y PROGRESO",
                "PLG",
                "María Soledad Perez Tello de Rodriguez",
                "https://mpesije.jne.gob.pe/apidocs/"
                "073703ca-c427-44f0-94b1-a782223a5e10.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/2931.jpg",
            ),
            (
                "JUNTOS POR EL PERU",
                "JPP",
                "Roberto Helbert Sanchez Palomino",
                "https://mpesije.jne.gob.pe/apidocs/"
                "bb7c7465-9c6e-44eb-ac7d-e6cc7f872a1a.jpg",
                "https://votoinformado.jne.gob.pe/LogoOp/1264.jpg",
            ),
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
            Tema(nombre="Transporte", icono="truck",
                 descripcion="Infraestructura vial y transporte público"),
            Tema(nombre="Tecnología", icono="cpu",
                 descripcion="Transformación digital e innovación"),
            Tema(nombre="Medio Ambiente", icono="leaf",
                 descripcion="Recursos naturales y cambio climático"),
            Tema(nombre="Corrupción", icono="scale",
                 descripcion="Lucha anticorrupción e institucionalidad"),
        ]
        for tema in temas:
            db.add(tema)

        await db.commit()
        print("✅ Datos cargados correctamente")
        print(f"   {len(datos)} candidatos principales")
        print(f"   {len(temas)} temas")


if __name__ == "__main__":
    asyncio.run(seed())
