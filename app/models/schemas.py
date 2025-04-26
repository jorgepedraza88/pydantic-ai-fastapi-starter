"""Esquemas de datos para la API."""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


# Aqui se define el esquema de la solicitud al agente
# Puedes añadir más campos según sea necesario
class AgentRequest(BaseModel):
    """Esquema para solicitudes al agente."""

    query: str = Field(..., description="Consulta o pregunta para el agente")


class TokenUsage(BaseModel):
    """Estructura para el uso de tokens."""

    requests: int = Field(0, description="Numero de solicitudes realizadas")
    request_tokens: int = Field(0, description="Tokens utilizados en el input")
    response_tokens: int = Field(0, description="Tokens utilizados en la respuesta")
    total_tokens: int = Field(0, description="Total de tokens utilizados")


# Aqui se define el esquema de la respuesta del agente
# Puedes añadir más campos según sea necesario
class AgentResponse(BaseModel):
    """Esquema para respuestas del agente."""

    response: str = Field(..., description="Respuesta del agente")
    usage: TokenUsage = Field(default=None, description="Uso del agente en la consulta")
    sources: Optional[List[str]] = Field(
        default=None, description="Fuentes utilizadas para la respuesta"
    )
    metadata: Optional[Dict] = Field(
        default=None, description="Metadatos adicionales de la respuesta"
    )
