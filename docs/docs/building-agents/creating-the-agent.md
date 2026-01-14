---
sidebar_position: 4
title: Creating the Agent
---

# Creating the Agent

The agent lives in `backend/agent/openai_agent.py`.

## Agent Construction

```python
from langchain.agents import create_agent
from tools.weather import get_weather


def get_openai_agent():
    agent = create_agent(
        "gpt-4.1",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    return agent
```

This single function defines the **entire reasoning unit**.

## Breaking Down the Parameters

| Parameter | Purpose |
|-----------|---------|
| `"gpt-4.1"` | Model selection |
| `tools=[get_weather]` | Available capabilities |
| `system_prompt` | Behavioral baseline |

This function fully defines:

> *What the agent is capable of*

## Why Return a Function?

The agent is created via a factory function (`get_openai_agent()`) rather than a global variable. This allows:

1. **Fresh state per request** — No shared global state
2. **Easy testing** — Create agents in tests
3. **Configuration flexibility** — Pass different parameters later

## Agent Creation Per Request

In the current design, the agent is created **inside** the request handler:

```python
def handle_message(last_message, history):
    agent = get_openai_agent()  # Fresh agent each time
    # ...
```

This means:

- No shared global state
- No hidden memory between requests
- Every request is deterministic

:::info Early Design Choice
This is intentional for learning. Memory will be introduced explicitly in later chapters.
:::

## What the Agent "Knows"

When created, the agent knows:

1. **Which model to use** — Determines capabilities and behavior
2. **Which tools exist** — Enables external actions
3. **Its personality** — Via the system prompt

It does NOT know:

- Previous conversations (no memory yet)
- Who the user is
- The current time (unless you add a tool)

## The System Prompt

The system prompt sets the agent's baseline behavior:

```python
system_prompt="You are a helpful assistant"
```

This can be more detailed:

```python
system_prompt="""You are Artemis, a knowledgeable AI assistant.

Capabilities:
- You can check weather using the get_weather tool
- Always be concise and helpful
- If you don't know something, say so

Do not make up information."""
```

The system prompt shapes every response the agent generates.

---

## Key Takeaways

- Agents are created via factory functions
- Three key parameters: model, tools, system prompt
- Creating agents per request ensures determinism
- The agent only knows what you explicitly provide

---

**Next:** [Handling Messages](/building-agents/handling-messages)
