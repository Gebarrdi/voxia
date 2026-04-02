# create_tables.py — crea todas las tablas en PostgreSQL
# Solo se ejecuta una vez al inicio del proyecto

import asyncio
from app.database import engine, Base
import app.models  # importa todos los modelos para que Base los conozca

async def create_tables():
    async with engine.begin() as conn:
        # Crea todas las tablas que hereden de Base
        # checkfirst=True — no falla si la tabla ya existe
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)
    print("✅ Tablas creadas correctamente")

if __name__ == "__main__":
    asyncio.run(create_tables())
