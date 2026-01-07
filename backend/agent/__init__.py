from .openai_agent import get_openai_llm
from .openrouter_agent import get_openrouter_llm
from langchain.agents import create_agent
from backend.tools.weather import get_weather
from backend.memory import trim_messages
from backend.config import settings
from typing import Any


def build_agent(checkpointer: Any):

    tools = [get_weather]
    llm = None

    if settings.llm_provider == "openai":
        llm = get_openai_llm()
    else:
        llm = get_openrouter_llm(settings.llm_model)

    agent = create_agent(
        llm,
        tools=tools,
        system_prompt="You are a helpful assistant",
        checkpointer=checkpointer,
        middleware=[trim_messages],
    )
    return agent
