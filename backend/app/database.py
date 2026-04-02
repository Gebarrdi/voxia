# database.py — conexión a PostgreSQL usando SQLAlchemy async
# Este archivo es el puente entre Python y PostgreSQL

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase
from app.config import get_settings
from typing import AsyncGenerator

settings = get_settings()

# Motor de conexión — es el "conductor" que maneja la conexión con PostgreSQL
# pool_size: cuántas conexiones simultáneas mantiene abiertas
# echo: si True, imprime cada SQL que ejecuta (útil para debug)
engine = create_async_engine(
    settings.database_url,
    pool_size=5,
    echo=settings.debug
)

# Fábrica de sesiones — cada request HTTP abre una sesión y la
# cierra al terminar
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False  # los objetos siguen accesibles después del commit
)


# Clase base para todos los modelos — todas las tablas heredan de aquí
class Base(DeclarativeBase):
    pass


# Función que FastAPI usará como dependencia en cada endpoint
# Abre una sesión, la entrega al endpoint, y la cierra automáticamente
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session           # entrega la sesión al endpoint
            await session.commit()  # guarda los cambios si todo salió bien
        except Exception:
            await session.rollback()  # deshace los cambios si hubo error
            raise
