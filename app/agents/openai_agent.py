"""Basic OpenAI agent"""

from pydantic_ai import Agent, Tool
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.agents.base_agent import BaseAgent
from app.core.config import settings
from app.tools.common import get_today_date, get_user_name


class OpenAiBasicAgent(BaseAgent):
    """
    Basic AI agent implementation using OpenAI models.

    This class provides a wrapper around the OpenAI models to create
    a simple AI agent that can process text queries and return
    structured responses.
    """

    def __init__(self):
        """
        Initialize the basic agent.

        Sets up the OpenAI model with the appropriate API key from settings
        and configures the agent with default parameters.
        """
        super().__init__()

        # Use the API key from environment variables
        self.model = OpenAIModel(
            "gpt-4o-mini",
            provider=OpenAIProvider(api_key=settings.OPENAI_API_KEY),
        )

        self.agent = Agent(
            self.model,
            system_prompt="You are a helpful and professional assistant. "
            "Always use the user's name in the response. Use tools to get the user name.",
            temperature=0.7,
            name="OpenAI Basic Agent",
            tools=[
                Tool(get_today_date, takes_ctx=False),
                Tool(get_user_name, takes_ctx=True),
            ],
            # tools=[get_user_name] - This is a simple example of a tool
        )
