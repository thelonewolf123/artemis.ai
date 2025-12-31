from langchain.agents.middleware import before_model
from langchain.messages import RemoveMessage
from langchain.agents import AgentState
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime
from backend.config import settings

from typing import Any


@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """Keep only the last few messages to fit context window."""
    messages = state["messages"]
    remove_messages = []
    for message in messages[::-1][settings.max_conversation_limit :]:
        remove_messages.append(RemoveMessage(id=message.id))

    return {"messages": remove_messages}
