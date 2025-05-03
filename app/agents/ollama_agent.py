"""Basic Ollama agent"""

from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.agents.base_agent import BaseAgent
from app.tools.common import get_today_date


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
            deps_type=str,
            system_prompt="You are a helpful and professional assistant. "
            "Alawys use the user name in the response.",
            temperature=0.7,
            name="Ollama Basic Agent",
            tools=[
                Tool(get_today_date, takes_ctx=False),
                # Note: Ollama struggles to get the user name from the context
                # Tool(get_user_name, takes_ctx=True),
            ],
        )

        #  We can add more system prompts using decorators, e.g.:
        #  This seems to work better than tools with Ollama
        @self.agent.system_prompt
        def add_the_users_name(ctx: RunContext[str]) -> str:
            return f"The user's name is {ctx.deps}."

        _ = add_the_users_name  # <- Remove unused variable warning
