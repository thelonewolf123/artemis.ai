from langchain.agents import create_agent
from langchain.tools import BaseTool
from typing import Sequence
from backend.tools.weather import get_weather


def get_openai_agent(tools: Sequence[BaseTool]):
    agent = create_agent(
        "gpt-4.1",
        tools=tools,
        system_prompt="You are a helpful assistant",
    )
    return agent
