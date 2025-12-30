from typing import List
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from tools.weather import get_weather
import os


def get_openai_agent():
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
