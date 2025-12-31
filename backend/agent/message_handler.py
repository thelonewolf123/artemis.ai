from langchain.messages import HumanMessage, AIMessage
from typing import List, Any


def handle_message(agent: Any, last_message: str, history: List):
    request = []
    for message in history:
        if message["role"] == "assistant":
            request.append(AIMessage(message["content"][0]["text"]))
        else:
            request.append(HumanMessage(message["content"][0]["text"]))
    request.append(HumanMessage(last_message))
    response = agent.invoke({"messages": request})

    return response["messages"][-1].content
