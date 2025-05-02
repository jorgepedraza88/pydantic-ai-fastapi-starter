"""Routes for the FastAPI application."""

from fastapi import APIRouter, Depends, HTTPException

from app.agents.gemini_agent import BasicGeminiAgent
from app.agents.openai_agent import BasicAgent
from app.agents.ollama_agent import OllamaBasicAgent
from app.models.schemas import AgentRequest, AgentResponse

router = APIRouter()


# Get an instance of the agent
def get_agent(request: AgentRequest) -> object:
    """Get an instance of the agent.

    This function creates an instance of the BasicAgent class,
    which is responsible for processing queries using the OpenAI API.

    The agent is initialized with the provided query and LLM provider
    specified in the request.

    Args:
        request (AgentRequest): The request object containing the query and LLM provider.

    Returns:
        BasicAgent: An instance of the BasicAgent class.
        BasicGeminiAgent: An instance of the BasicGeminiAgent class if the LLM provider is "gemini".
    """
    if request.llm_provider == "gemini":
        return BasicGeminiAgent()
    if request.llm_provider == "ollama":
        return OllamaBasicAgent()

    return BasicAgent()


# request:
# AgentRequest: FastAPI will automatically parse the request body to the AgentRequest model

# response_model=AgentResponse:
# Specifies that the response will follow the structure defined in AgentResponse

# agent:
# BasicAgent = Depends(get_agent):
# FastAPI will invoke get_agent() and pass its result as the agent parameter


@router.post("/agent/query", response_model=AgentResponse)
async def query_agent(request: AgentRequest, agent: BasicAgent = Depends(get_agent)):
    """Process a query using the AI agent.

    This endpoint receives a query request and processes it using the appropriate AI agent
    based on the specified LLM provider.

    Args:
        request (AgentRequest): The request containing the query and LLM provider.
        agent (BasicAgent): The agent instance obtained via dependency injection.

    Returns:
        AgentResponse: The processed response from the AI agent.

    Raises:
        HTTPException: If an error occurs during query processing.
    """
    try:
        result = await agent.process_query(query=request.query)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing the query: {str(e)}"
        ) from e
