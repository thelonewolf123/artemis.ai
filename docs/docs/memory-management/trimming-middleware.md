---
sidebar_position: 6
title: Trimming Middleware
---

# Trimming Middleware

Now that memory persists, we need to control its size to avoid context window overflow.

## The Problem

Without trimming:

```
Turn 1: 100 tokens
Turn 2: 200 tokens
Turn 3: 150 tokens
...
Turn 50: 180 tokens
─────────────────────
Total: 8,500 tokens → EXCEEDS LIMIT
```

The conversation grows until requests fail.

## The Solution: Middleware

Middleware allows you to intercept and modify state before the model runs.

`backend/memory/__init__.py`:

```python
from langgraph.middleware import before_model
from langgraph.types import AgentState, Runtime
from langchain.messages import RemoveMessage


@before_model
def trim_messages(state: AgentState, runtime: Runtime):
    messages = state["messages"]
    remove_messages = []

    # Keep only the most recent messages
    for message in messages[::-1][settings.max_conversation_limit:]:
        remove_messages.append(RemoveMessage(id=message.id))

    return {"messages": remove_messages}
```

## How It Works

1. **Intercept state** — Before the LLM runs
2. **Check message count** — How many messages exist
3. **Mark old messages** — Identify messages to remove
4. **Return removals** — The system deletes them

## The Trimming Logic

```python
messages[::-1][settings.max_conversation_limit:]
```

This reverses the message list and takes everything beyond the limit:

```
Original: [msg1, msg2, msg3, msg4, msg5]  # limit=3
Reversed: [msg5, msg4, msg3, msg2, msg1]
Beyond limit: [msg2, msg1]  # These get removed
Result: [msg3, msg4, msg5]  # Most recent kept
```

## Configurable Limits

The maximum conversation size is configurable:

```python
self.max_conversation_limit = environ.get("MAX_CONVERSATION_LIMIT", 50)
```

This allows you to:

| Adjustment | Trade-off |
|------------|-----------|
| Higher limit | More context, higher cost |
| Lower limit | Less context, lower cost |

## Registering Middleware

Middleware is registered when creating the agent:

```python
agent = create_agent(
    llm,
    tools=tools,
    system_prompt="You are a helpful assistant",
    checkpointer=settings.checkpointer,
    middleware=[trim_messages],  # Register here
)
```

The trimming happens **automatically** — the UI doesn't know or care.

## Before and After

### Without Trimming

```
Messages grow unbounded → Request fails
```

### With Trimming

```
Messages capped at limit → Always works
```

---

## Chapter Summary

In this chapter, you learned:

- LLMs are stateless — systems provide memory
- Unlimited history doesn't scale
- Thread IDs isolate conversations
- Memory storage is configurable
- Middleware trims old messages automatically

Artemis now has:

- Persistent conversation memory
- Thread-based session handling
- Automatic context trimming
- Configurable memory limits
- Zero UI complexity added

This is a **major milestone**.

---

## What's Next

Memory alone is not enough. The current implementation:

- Lives in RAM (lost on restart)
- Uses message count, not token count

In the next chapter, we'll refactor for **durability and correctness**:

- Persistent state using SQLite
- Token-aware context trimming
- Configurable model selection

**Continue to:** [Persistence](/persistence)
