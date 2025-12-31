from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from typing import Sequence

import os


def get_openrouter_agent(
    tools: Sequence[BaseTool],
    model: str = "x-ai/grok-4-fast",
):
    llm = ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
    agent = create_agent(
        llm,
        tools=tools,
        system_prompt="You are a helpful assistant",
    )
    return agent
