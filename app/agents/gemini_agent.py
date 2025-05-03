"""Basic Gemini Agent"""

from pydantic_ai import Agent, Tool
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from app.agents.base_agent import BaseAgent
from app.core.config import settings
from app.tools.common import get_today_date, get_user_name


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
            deps_type=str,
            system_prompt="You are a helpful and professional assistant. "
            "Use tools to get the user name. "
            "Use the user name in the response.",
            temperature=0.7,
            name="Gemini Basic Agent",
            tools=[
                Tool(get_today_date, takes_ctx=False),
                Tool(get_user_name, takes_ctx=True),
            ],
        )

        # We can also add tools using decorators, e.g.:
        # @self.agent.tool()
        # def get_user_name(ctx: RunContext[str]) -> str:
        #     """Get the user's name."""
        #     return ctx.deps

        # _ = get_user_name  # <- Remove unused variable warning
