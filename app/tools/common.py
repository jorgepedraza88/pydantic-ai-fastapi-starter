"""Common tools for the AI agents"""

from datetime import datetime

from pydantic_ai import RunContext


def get_today_date() -> str:
    """Get today's date in YYYY-MM-DD format."""

    return datetime.now().strftime("%Y-%m-%d")


def get_user_name(ctx: RunContext[str]) -> str:
    """Get the user's name."""
    return ctx.deps
