from langchain.messages import HumanMessage, AIMessage
from typing import Any


def handle_message(agent: Any, last_message: str, user_id: str):
    request = []
    request.append(HumanMessage(last_message))
    response = agent.invoke(
        {"messages": request}, {"configurable": {"thread_id": user_id}}
    )

    return response["messages"][-1].content
