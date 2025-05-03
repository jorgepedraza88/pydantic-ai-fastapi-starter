# Pydantic AI + FastAPI Starter

![image](https://github.com/user-attachments/assets/0aada21f-bc6e-4685-9bfc-0274c3e442c9)

A FastAPI microservice for AI agent interactions using Pydantic AI. This project provides a simple API wrapper around multiple LLM providers (OpenAI, Google Gemini, and Ollama) with a consistent interface.

## Features

- 🚀 FastAPI-based microservice with clean architecture
- 🤖 Multiple AI agent implementations (OpenAI, Google Gemini, Ollama)
- 📝 Structured requests and responses using Pydantic models
- 🔄 Support for conversation history
- 🛠️ Custom tools for enhanced agent capabilities
- 👤 User context integration through dependencies

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/pydantic-ai-fastapi-starter.git
cd pydantic-ai-fastapi-starter
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Application

Start the FastAPI server with:

```bash
python -m app.main
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Root endpoint

- `GET /`: Basic test route that returns a welcome message

### Agent Query Endpoint

- `POST /api/v1/agent/query`: Process a query using an AI agent

Request body:
```json
{
  "query": "What is artificial intelligence?",
  "history": [], 
  "llm_provider": "openai",
  "deps": "John"
}
```

Supported LLM providers:
- `openai`: Uses OpenAI models
- `gemini`: Uses Google Gemini models
- `ollama`: Uses local Ollama models

## Tools Integration

The agents in this project are enhanced with custom tools that extend their capabilities:

- **get_today_date**: A tool that provides the agents with the current date
- **get_user_name**: A context-aware tool that retrieves the user's name from dependencies

These tools can be accessed by the agents through:

1. Direct tool registration:
```python
tools=[
    Tool(get_today_date, takes_ctx=False),
    Tool(get_user_name, takes_ctx=True),
]
```

2. Decorator-based registration (alternative approach):
```python
@agent.tool()
def get_user_name(ctx: RunContext[str]) -> str:
    """Get the user's name."""
    return ctx.deps
```

## Project Structure

```
pydantic-ai-microservice/
├── app/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── gemini_agent.py
│   │   ├── ollama_agent.py
│   │   └── openai_agent.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── schemas.py
│   ├── tools/
│   │   └── common.py
│   └── main.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Development

This project uses Ruff for linting and formatting. Configuration can be found in `pyproject.toml`.

## License

MIT License
