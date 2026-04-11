import asyncio
from app.database import AsyncSessionLocal
from sqlalchemy import text

async def ver():
    async with AsyncSessionLocal() as db:
        result = await db.execute(text(
            "SELECT constraint_name, column_name "
            "FROM information_schema.key_column_usage "
            "WHERE table_name = 'cache_analisis'"
        ))
        for row in result:
            print(row)

asyncio.run(ver())
