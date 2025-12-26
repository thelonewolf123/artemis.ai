from typing import List
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage

from tools.weather import get_weather


def get_openai_agent():
    agent = create_agent(
        "gpt-4.1",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    return agent


def handle_message(last_message: str, history: List):
    agent = get_openai_agent()
    request = []
    for message in history:
        if message["role"] == "assistant":
            request.append(AIMessage(message["content"][0]["text"]))
        else:
            request.append(HumanMessage(message["content"][0]["text"]))
    request.append(HumanMessage(last_message))
    response = agent.invoke({"messages": request})

    return response["messages"][-1].content
