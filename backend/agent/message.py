from langchain.messages import HumanMessage, AIMessage
from typing import List
from .xai_agent import get_xai_agent


def handle_message(last_message: str, history: List):
    agent = get_xai_agent()
    request = []
    for message in history:
        if message["role"] == "assistant":
            request.append(AIMessage(message["content"][0]["text"]))
        else:
            request.append(HumanMessage(message["content"][0]["text"]))
    request.append(HumanMessage(last_message))
    response = agent.invoke({"messages": request})

    return response["messages"][-1].content
