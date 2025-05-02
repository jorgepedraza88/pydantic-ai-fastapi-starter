"""Settings for FastAPI application with Pydantic AI."""

import os

from dotenv import load_dotenv

# Loads environment variables from .env file
load_dotenv()


class Settings:  # pylint: disable=too-few-public-methods
    """App configuration"""

    PROJECT_NAME: str = "Mi Proyecto FastAPI con Pydantic AI"
    API_V1_STR: str = "/api/v1"

    # Configuración para tu modelo/agente de IA
    AI_MODEL_KEY: str = os.getenv("AI_MODEL_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    def get_api_url(self) -> str:
        """Return the base URL for the API."""
        return self.API_V1_STR


settings = Settings()
