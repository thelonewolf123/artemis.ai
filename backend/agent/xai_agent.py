from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tools.weather import get_weather
import os


def get_xai_agent():
    llm = ChatOpenAI(
        model="x-ai/grok-4-fast",
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
    agent = create_agent(
        llm,
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    return agent
