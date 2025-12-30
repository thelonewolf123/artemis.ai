from langchain.agents import create_agent

from tools.weather import get_weather


def get_openai_agent():
    agent = create_agent(
        "gpt-4.1",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    return agent
