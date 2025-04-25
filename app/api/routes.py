from fastapi import APIRouter, Depends, HTTPException

from app.agents.basic_agent import BasicAgent
from app.models.schemas import AgentRequest, AgentResponse

router = APIRouter()


# Función para obtener una instancia del agente
def get_agent():
    """Función para obtener una instancia del agente de IA."""
    return BasicAgent()


@router.post("/agent/query", response_model=AgentResponse)
async def query_agent(request: AgentRequest, agent: BasicAgent = Depends(get_agent)):
    """
    Endpoint para consultar al agente de IA
    """
    try:
        result = await agent.process_query(query=request.query, context=request.context)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al procesar la consulta: {str(e)}"
        ) from e
