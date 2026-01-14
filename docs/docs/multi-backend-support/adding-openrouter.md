---
sidebar_position: 5
title: Adding OpenRouter
---

# Adding OpenRouter

OpenRouter allows you to route requests to multiple models using a single API. Here's how to add it as a backend.

## OpenRouter Overview

OpenRouter is a meta-provider that gives you access to:

- OpenAI models (GPT-4, GPT-3.5)
- Anthropic models (Claude)
- Google models (Gemini)
- Open source models (Llama, Mistral)
- And many more

All through one API endpoint.

## The OpenRouter Agent

`backend/agent/openrouter_agent.py`:

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from typing import Sequence
import os


def get_openrouter_agent(
    tools: Sequence[BaseTool],
    model: str = "x-ai/grok-4-fast",
):
    llm = ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )

    agent = create_agent(
        llm,
        tools=tools,
        system_prompt="You are a helpful assistant",
    )
    return agent
```

## Key Observations

### 1. OpenAI-Compatible Interface

OpenRouter uses the same API format as OpenAI:

```python
llm = ChatOpenAI(
    ...
    base_url="https://openrouter.ai/api/v1/",  # Different URL
)
```

Only the `base_url` differs. Everything else is identical.

### 2. Same Credentials

OpenRouter accepts the same key format:

```python
api_key=os.environ.get("OPENAI_API_KEY"),
```

You just need an OpenRouter API key stored in the same variable.

### 3. Model Selection

Different model names:

| Provider | Model Name |
|----------|------------|
| OpenAI | `gpt-4` |
| OpenRouter | `openai/gpt-4` or `x-ai/grok-4-fast` |

OpenRouter uses the format `provider/model`.

## Comparing Implementations

### OpenAI Agent

```python
def get_openai_agent(tools):
    agent = create_agent(
        "gpt-4.1",  # Direct model name
        tools=tools,
        system_prompt="You are a helpful assistant",
    )
    return agent
```

### OpenRouter Agent

```python
def get_openrouter_agent(tools, model="x-ai/grok-4-fast"):
    llm = ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
    agent = create_agent(
        llm,
        tools=tools,
        system_prompt="You are a helpful assistant",
    )
    return agent
```

The difference is minimal — just the LLM initialization.

## Important Design Insight

> **Agents depend on behavior, not providers.**

Both agents:

- Accept the same tools
- Use the same system prompt
- Return the same interface
- Handle messages identically

The provider is an implementation detail.

---

## Key Takeaways

- OpenRouter uses the OpenAI-compatible API format
- Only `base_url` and model names differ
- The agent interface remains identical
- Provider choice is hidden from the rest of the system

---

**Next:** [Running as a Module](/multi-backend-support/running-as-module)
