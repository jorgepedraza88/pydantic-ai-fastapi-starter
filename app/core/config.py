"""Configuración de la aplicación FastAPI con Pydantic AI."""

import os

from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()


class Settings:  # pylint: disable=too-few-public-methods
    """Configuración de la aplicación."""

    PROJECT_NAME: str = "Mi Proyecto FastAPI con Pydantic AI"
    API_V1_STR: str = "/api/v1"

    # Configuración para tu modelo/agente de IA
    AI_MODEL_KEY: str = os.getenv("AI_MODEL_KEY", "")
    # OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    # OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    # SUPABASE_URL: str = os.getenv("SUPABASE_URL", "https://your-supabase-url.supabase.co")
    # SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "your-supabase-key")

    def get_api_url(self) -> str:
        """Devuelve la URL base de la API."""
        return self.API_V1_STR


settings = Settings()
