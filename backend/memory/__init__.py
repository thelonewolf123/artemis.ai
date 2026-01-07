from langchain.agents.middleware import before_model
from langchain.agents import AgentState
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime
from backend.config import settings
from langchain_core.messages.utils import (
    trim_messages as lc_trim_messages,
    count_tokens_approximately,
)

from typing import Any


@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """Keep only the last few messages to fit context window."""
    messages = state["messages"]
    new_messages = lc_trim_messages(
        messages,
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=settings.max_conversation_token_limit,
        start_on="human",
        end_on=("human", "tool"),
    )

    return {"messages": new_messages}
