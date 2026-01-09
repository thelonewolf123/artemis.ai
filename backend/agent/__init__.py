from typing import Any
from backend.config import settings
from .openai_agent import get_openai_llm
from backend.memory import trim_messages
from langchain.agents import create_agent
from backend.tools.weather import get_weather
from .openrouter_agent import get_openrouter_llm
from backend.tools.memory import get_relevant_memories


def build_agent(checkpointer: Any):

    tools = [get_weather, get_relevant_memories]
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
