"""Agente básico para interactuar con el modelo de OpenAI."""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Se carga la clave de API de OpenAI desde las variables de entorno automáticamente
# TODO: Averiguar como hacerlo
model = OpenAIModel(
    "gpt-4o-mini",
    provider=OpenAIProvider(
        api_key="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"
    ),
)

basic_agent = Agent(
    model, system_prompt="Eres un asistente útil.", temperature=0.7, name="BasicAgent"
)

result = basic_agent.run_sync("¿Cuál es la capital de Dinamarca?")
print(result)
