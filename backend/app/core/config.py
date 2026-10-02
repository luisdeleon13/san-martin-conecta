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
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
