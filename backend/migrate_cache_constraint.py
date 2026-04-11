"""
Migra la constraint de cache_analisis de UNIQUE(clave) a UNIQUE(tipo, clave).
Ejecutar UNA sola vez.
"""
import asyncio
from app.database import AsyncSessionLocal
from sqlalchemy import text

async def migrar():
    async with AsyncSessionLocal() as db:
        print("Iniciando migración de constraint...")

        # 1. Eliminar constraint única actual (solo en clave)
        await db.execute(text(
            "ALTER TABLE cache_analisis DROP CONSTRAINT IF EXISTS cache_analisis_clave_key"
        ))
        print("✅ Constraint antigua eliminada")

        # 2. Crear nueva constraint única en (tipo, clave)
        await db.execute(text(
            "ALTER TABLE cache_analisis ADD CONSTRAINT cache_analisis_tipo_clave_key "
            "UNIQUE (tipo, clave)"
        ))
        print("✅ Nueva constraint UNIQUE(tipo, clave) creada")

        await db.commit()
        print("✅ Migración completada")

asyncio.run(migrar())
