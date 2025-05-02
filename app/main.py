"""FastAPI application configuration with Pydantic AI."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings

# Initialize FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API with AI agents using Pydantic AI",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include endpoints
app.include_router(router, prefix=settings.API_V1_STR)


# Basic test route
@app.get("/")
async def root():
    """Basic test route to verify that the API is working."""
    return {"message": "Welcome to my FastAPI project with Pydantic AI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
