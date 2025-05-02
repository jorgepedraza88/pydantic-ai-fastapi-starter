"""Basic Ollama agent"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.models.schemas import AgentResponse


class OllamaBasicAgent:
    """
    Basic AI agent implementation.

    This class provides a wrapper around the Ollama models to create
    a simple AI agent that can process text queries and return
    structured responses.

    Attributes:
        model: The AI model to use for generating responses.
        agent: The agent instance that handles message processing.
    """

    def __init__(self):
        """
        Initialize the basic agent.

        Sets up the Ollama model with the appropriate API key from settings
        and configures the agent with default parameters.
        """
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
            response=result.output, usage=usage, metadata={"model": "ollama:qwen2.5"}
        )
