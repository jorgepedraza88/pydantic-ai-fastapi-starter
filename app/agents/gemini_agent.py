"""Agente para interactuar con modelos de Gemini (Google)."""

import asyncio
from typing import Dict, Optional

try:
    import google.generativeai as genai
except ImportError:
    print(
        "Error: Necesitas instalar el paquete 'google-generativeai' para usar este agente."
    )
    print("Ejecuta: pip install google-generativeai")

from app.core.config import settings
from app.models.schemas import AgentResponse


class GeminiAgent:
    """Clase para el agente de Gemini."""

    def __init__(self):
        """Inicializa el agente de Gemini."""
        # Configurar la API de Gemini
        genai.configure(api_key=settings.GEMINI_API_KEY)

        # Obtener el modelo
        self.model = genai.GenerativeModel("gemini-1.5-pro")

        # Configuración del sistema
        self.system_prompt = "Eres un asistente útil y profesional."

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
            # Formatear el mensaje con el contexto
            context_info = ", ".join([f"{k}: {v}" for k, v in context.items()])
            message = f"{query}\nContexto adicional: {context_info}"

        # Configurar el chat
        chat = self.model.start_chat(history=[])

        # Ejecutar la consulta - usar asyncio para no bloquear
        # Gemini no tiene API async nativa, así que usamos to_thread
        response = await asyncio.to_thread(
            chat.send_message, message, system_instruction=self.system_prompt
        )

        # Crear y devolver la respuesta
        return AgentResponse(
            response=response.text,
            confidence=0.90,  # En un caso real, esto podría venir del modelo
            sources=[],  # En un caso real, podrías añadir fuentes
            metadata={"model": "gemini-1.5-pro"},
        )
