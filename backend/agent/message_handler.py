from typing import Any
from langchain.messages import HumanMessage


def handle_message(agent: Any, last_message: str, user_id: int):
    request = [HumanMessage(last_message)]
    response = agent.invoke(
        {"messages": request}, {"configurable": {"thread_id": str(user_id)}}
    )

    return response["messages"][-1].content
