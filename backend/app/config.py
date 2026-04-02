# config.py — configuración central de la app
# Lee las variables del archivo .env y las expone al resto del proyecto

from pydantic_settings import BaseSettings
# lee variables de entorno automáticamente
from functools import lru_cache
# para cachear la configuración (no leer .env mil veces)


class Settings(BaseSettings):
    # Variables que deben existir en el .env
    database_url: str
    redis_url: str
    anthropic_api_key: str
    app_name: str = "VoxIA"      # valor por defecto si no está en .env
    app_version: str = "1.0.0"
    debug: bool = True

    class Config:
        env_file = ".env"         # le dice a Pydantic dónde buscar el archivo


@lru_cache()  # ejecuta get_settings() una sola vez y cachea el resultado
def get_settings() -> Settings:
    return Settings()
