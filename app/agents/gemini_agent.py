"""Basic Gemini Agent"""

from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from app.agents.base_agent import BaseAgent
from app.core.config import settings


class BasicGeminiAgent(BaseAgent):
    """
    Basic Gemini agent implementation.

    This class provides a wrapper around the Gemini models to create
    a simple AI agent that can process text queries and return
    structured responses.
    """

    def __init__(self):
        """
        Initialize the basic agent.

        Sets up the Gemini model with the appropriate API key from settings
        and configures the agent with default parameters.
        """
        super().__init__()

        # Use the API key from environment variables
        self.model = GeminiModel(
            "gemini-2.0-flash",
            provider=GoogleGLAProvider(api_key=settings.GEMINI_API_KEY),
        )

        self.agent = Agent(
            model=self.model,
            system_prompt="You are a helpful and professional assistant",
            temperature=0.7,
            name="Gemini Basic Agent",
            retries=2,
        )
