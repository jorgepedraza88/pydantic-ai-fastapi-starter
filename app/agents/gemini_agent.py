"""Basic Gemini Agent"""

from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from app.core.config import settings
from app.models.schemas import AgentResponse


class BasicGeminiAgent:
    """
    Basic Gemini agent implementation.

    This class provides a wrapper around the Gemini models to create
    a simple AI agent that can process text queries and return
    structured responses.

    Attributes:
        model: The AI model to use for generating responses.
        model_settings: Settings for the AI model, including token limits
            and temperature settings.
        agent: The agent instance that handles message processing.
    """

    def __init__(self):
        """
        Initialize the basic agent.

        Sets up the Gemini model with the appropriate API key from settings
        and configures the agent with default parameters.
        """
        # Use the API key from environment variables
        self.model = GeminiModel(
            "gemini-2.0-flash",
            provider=GoogleGLAProvider(api_key=settings.GEMINI_API_KEY),
        )

        # This does not tell the model to use 30 tokens, but rather that for the response once it reaches 30 tokens
        # self.model_settings = ModelSettings(max_tokens=30)

        self.agent = Agent(
            model=self.model,
            system_prompt="You are a helpful and professional assistant",
            temperature=0.7,
            name="Gemini Basic Agent",
            retries=2,
        )

    async def process_query(self, query: str) -> AgentResponse:
        """
        Process a query to the agent.

        This method takes a user query, sends it to the AI model,
        and returns a structured response.

        Args:
            query: The text query to process.

        Returns:
            AgentResponse: The structured response from the agent containing
                the generated text, token usage statistics, and metadata.
        """
        # Prepare message with context if it exists
        message = query

        # Execute the query
        result = await self.agent.run(message)

        # Get token usage
        usage = result.usage().__dict__

        # Create and return the response
        return AgentResponse(
            response=result.output,
            usage=usage,
            metadata={"model": "gemini-2.0-flash"},
        )
