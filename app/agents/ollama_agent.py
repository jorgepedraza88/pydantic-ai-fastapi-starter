"""Basic Ollama agent"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.agents.base_agent import BaseAgent


class OllamaBasicAgent(BaseAgent):
    """
    Basic AI agent implementation using Ollama.

    This class provides a wrapper around the Ollama models to create
    a simple AI agent that can process text queries and return
    structured responses.
    """

    def __init__(self):
        """
        Initialize the basic agent.

        Sets up the Ollama model with the appropriate API key from settings
        and configures the agent with default parameters.
        """
        super().__init__()

        # Use the API key from environment variables
        self.model = OpenAIModel(
            "qwen2.5",
            provider=OpenAIProvider(base_url="http://127.0.0.1:11434/v1"),
        )

        self.agent = Agent(
            self.model,
            system_prompt="You are a helpful and professional assistant.",
            temperature=0.7,
            name="Ollama Basic Agent",
        )
