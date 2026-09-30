"""
Configuración central del proyecto.

Este archivo lee las variables definidas en el archivo ".env" y las deja
disponibles en todo el backend como un solo objeto "settings".

Así, en el resto del código NUNCA escribimos contraseñas, números de
WhatsApp ni claves directamente — siempre las leemos desde aquí.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Base de datos ---
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "san_martin_conecta"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""

    # --- Seguridad ---
    SECRET_KEY: str = "changeme"

    # --- Datos generales de la plataforma ---
    PLATFORM_NAME: str = "San Martin Conecta"
    WHATSAPP_NUMBER: str = "50200000000"

    # --- Entorno ---
    ENVIRONMENT: str = "development"

    @property
    def DATABASE_URL(self) -> str:
        """
        Arma la cadena de conexión a PostgreSQL a partir de las piezas
        anteriores. La usaremos en la Fase 3 al configurar SQLAlchemy.
        """
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # Le decimos a pydantic-settings que lea el archivo ".env"
    # ubicado en la carpeta "backend/".
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Instancia única que se importa desde cualquier parte del backend:
#   from app.core.config import settings
settings = Settings()
