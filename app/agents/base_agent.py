"""Base Agent with common functionality"""

from typing import List, Optional

from pydantic_ai.agent import AgentRunResult
from pydantic_ai.messages import ModelMessage

from app.models.schemas import AgentResponse


class BaseAgent:
    """
    Base agent implementation with common functionality.

    This class provides shared methods for all agent types.

    Attributes:
        model: The AI model to use for generating responses.
        agent: The agent instance that handles message processing.
    """

    def __init__(self):
        """Initialize base attributes."""
        self.model = None
        self.agent = None

    async def process_query(
        self, query: str, history: Optional[List[ModelMessage]] = None
    ) -> AgentResponse:
        """
        Process a query to the agent.

        This method takes a user query, sends it to the AI model,
        and returns a structured response.

        Args:
            query: The text query to process.
            history: Optional list of previous messages exchanged with the agent,
                    providing context for the current query.

        Returns:
            AgentResponse: The structured response from the agent,
            including the generated text, token usage, and message history.
        """
        # Prepare message with context if it exists
        message = query

        # Execute the query
        result: AgentRunResult[str] = await self.agent.run(
            message, message_history=history
        )

        # Get token usage
        usage = result.usage()

        # Get message history if available
        new_messages = result.new_messages()

        # Create and return the response
        return AgentResponse(
            response=result.output,
            usage=usage,
            history=new_messages,
        )
