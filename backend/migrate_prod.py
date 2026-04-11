"""
migrate_prod.py — Migración de constraint en DB de producción.
Ejecutar UNA sola vez.

Uso:
    cd D:\\VoxIA\\backend
    python migrate_prod.py
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

# Leer DATABASE_URL desde .env.prod
from dotenv import load_dotenv
load_dotenv(".env.prod")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no encontrada en .env.prod")

print(f"Conectando a: {DATABASE_URL[:50]}...")

async def migrar():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:

        # 1. Eliminar constraint única actual (solo en clave)
        await conn.execute(text(
            "ALTER TABLE cache_analisis "
            "DROP CONSTRAINT IF EXISTS cache_analisis_clave_key"
        ))
        print("✅ Constraint antigua eliminada")

        # 2. Crear nueva constraint única en (tipo, clave)
        await conn.execute(text(
            "ALTER TABLE cache_analisis "
            "ADD CONSTRAINT IF NOT EXISTS cache_analisis_tipo_clave_key "
            "UNIQUE (tipo, clave)"
        ))
        print("✅ Nueva constraint UNIQUE(tipo, clave) creada")

    await engine.dispose()
    print("✅ Migración completada — listo para warm_cache")

asyncio.run(migrar())
