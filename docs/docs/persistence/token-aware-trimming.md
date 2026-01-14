---
sidebar_position: 4
title: Token-Aware Trimming
---

# Token-Aware Trimming

With persistent memory, conversations can grow very long. The previous message-count trimming isn't precise enough.

## The Problem with Message Counts

Trimming by message count is unreliable:

| Message | Tokens |
|---------|--------|
| "Hi" | 2 |
| "Please write a 500 word essay..." | 8 |
| Long code block | 500+ |
| Tool call with large response | 1000+ |

10 messages might be 50 tokens... or 5000 tokens. Message count doesn't tell you.

## The Solution: Token-Based Limits

Models enforce **token limits**, not message limits. Trimming must be token-aware.

## Precise Trimming Middleware

`backend/memory/__init__.py`:

```python
from langgraph.middleware import before_model
from langgraph.types import AgentState, Runtime
from langchain.messages import trim_messages as lc_trim_messages
from typing import Any


@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
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
```

## Understanding the Parameters

| Parameter | Purpose |
|-----------|---------|
| `strategy="last"` | Keep the most recent messages |
| `token_counter` | Function to count tokens |
| `max_tokens` | Budget for conversation history |
| `start_on="human"` | Trim to start on a human message |
| `end_on=("human", "tool")` | Preserve conversation boundaries |

## What This Guarantees

| Guarantee | Description |
|-----------|-------------|
| **Token budget** | Context never exceeds limit |
| **Recency** | Most recent conversation preserved |
| **Clean boundaries** | Doesn't cut mid-conversation |
| **Tool preservation** | Tool calls stay paired with results |
| **Automatic** | UI remains unaware |

This is **semantic trimming**, not blunt deletion.

## Configuration-Driven Limits

`backend/config/__init__.py`:

```python
self.max_conversation_token_limit = environ.get(
    "MAX_CONVERSATION_TOKEN_LIMIT", 10240
)
```

Configure via environment:

```bash
# Allow more history (higher cost)
MAX_CONVERSATION_TOKEN_LIMIT=20000

# Reduce history (lower cost)
MAX_CONVERSATION_TOKEN_LIMIT=5000
```

## Why This Matters

Different models have different context windows:

| Model | Suggested Limit |
|-------|-----------------|
| GPT-3.5 (4k) | 3000 |
| GPT-4 (8k) | 6000 |
| GPT-4 (128k) | 100000 |

Tune limits without code changes.

---

## Key Takeaways

- Message count doesn't reflect token usage
- Token-aware trimming respects model limits
- Semantic trimming preserves conversation structure
- Limits are configurable via environment variables

---

**Next:** [Configurable Models](/persistence/configurable-models)
