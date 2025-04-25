"""Configuración de la aplicación FastAPI con Pydantic AI."""

from fastapi import FastAPI

# from app.api.routes import router - Añadir más adelante para crear rutas de los agentes
from app.core.config import settings

# Inicializar la aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API con agentes de IA utilizando Pydantic AI",
    version="0.1.0",
)

# Incluir los endpoints
# app.include_router(router, prefix=settings.API_V1_STR)


# Ruta de prueba básica
@app.get("/")
async def root():
    """Ruta de prueba básica para verificar que la API está funcionando."""
    return {"message": "Bienvenido a mi proyecto FastAPI con Pydantic AI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
