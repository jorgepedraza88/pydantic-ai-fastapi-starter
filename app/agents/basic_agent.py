"""Agente básico para interactuar con modelos de IA."""

from typing import Dict, Optional

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.core.config import settings
from app.models.schemas import AgentResponse


class BasicAgent:
    """Clase para el agente básico de IA."""

    def __init__(self):
        """Inicializa el agente básico."""
        # Usar la clave de API desde las variables de entorno
        self.model = OpenAIModel(
            "gpt-4o-mini",
            provider=OpenAIProvider(api_key=settings.OPENAI_API_KEY),
        )

        self.agent = Agent(
            self.model,
            system_prompt="Eres un asistente útil y profesional.",
            temperature=0.7,
            name="Agente Básico",
        )

    async def process_query(
        self, query: str, context: Optional[Dict] = None
    ) -> AgentResponse:
        """
        Procesa una consulta al agente.

        Args:
            query: La consulta a procesar
            context: Contexto adicional para la consulta (opcional)

        Returns:
            AgentResponse: La respuesta del agente
        """
        # Preparar el mensaje con contexto si existe
        message = query
        if context:
            # Aquí podrías formatear el mensaje con el contexto
            # Por ejemplo, añadiendo información relevante del contexto
            context_info = ", ".join([f"{k}: {v}" for k, v in context.items()])
            message = f"{query}\nContexto adicional: {context_info}"

        # Ejecutar la consulta
        result = await self.agent.run(message)

        # TODO: Ver como puedo sacar los datos y mas cosas de la respuestas

        print(result)

        # Crear y devolver la respuesta
        return AgentResponse(
            response=result.output,
            # usage=usage,  # En un caso real, esto podría venir del modelo
            sources=[],  # En un caso real, podrías añadir fuentes
            metadata={"model": "gpt-4o-mini"},
        )
