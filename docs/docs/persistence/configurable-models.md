---
sidebar_position: 5
title: Configurable Models
---

# Configurable Models

Supporting multiple providers is only half the story. Within each provider, there are many models with different trade-offs.

## The Model Selection Problem

Hardcoding a model defeats flexibility:

```python
# Hardcoded - inflexible
llm = ChatOpenAI(model="gpt-4")
```

Different models suit different needs:

| Need | Better Model |
|------|--------------|
| Speed | gpt-3.5-turbo |
| Reasoning | gpt-4 |
| Cost | cheaper alternatives |
| Context | gpt-4-128k |

## Environment-Driven Configuration

`backend/config/__init__.py`:

```python
self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
self.llm_model = environ.get("LLM_MODEL_NAME", "x-ai/grok-4-fast")
```

This introduces clean separation:

| Setting | Controls |
|---------|----------|
| `LLM_PROVIDER` | Where requests go |
| `LLM_MODEL_NAME` | Which model is used |

## Using Configuration

`backend/agent/openrouter_agent.py`:

```python
def get_openrouter_llm(model: str):
    return ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
```

And in the agent builder:

```python
from backend.config import settings

llm = get_openrouter_llm(settings.llm_model)
```

No code changes required to switch models.

## Example Configurations

### Development (Fast and Cheap)

```bash
LLM_PROVIDER=openrouter
LLM_MODEL_NAME=openai/gpt-3.5-turbo
MAX_CONVERSATION_TOKEN_LIMIT=4000
```

### Production (Quality)

```bash
LLM_PROVIDER=openrouter
LLM_MODEL_NAME=anthropic/claude-3-opus
MAX_CONVERSATION_TOKEN_LIMIT=50000
```

### Testing (Local/Mock)

```bash
LLM_PROVIDER=mock
LLM_MODEL_NAME=test-model
```

## Why Global Settings?

```python
settings = ArtemisConfig()  # Single instance
```

If settings were recreated per request:

- Memory limits could diverge
- Model selection could drift
- Debugging becomes unpredictable

A single global configuration ensures:

> **Every component agrees on memory and model policy**

## The Complete Agent Constructor

```python
agent = create_agent(
    llm,
    tools=tools,
    system_prompt="You are a helpful assistant",
    checkpointer=checkpointer,
    middleware=[trim_messages],
)
```

This single line now defines:

- LLM backend
- Model selection
- Tool capabilities
- Persistent memory
- Context trimming policy

Nothing is hidden. Nothing is accidental.

---

## Chapter Summary

In this chapter, you learned:

- Persistent agents require checkpointing
- SQLite is sufficient for early-stage systems
- Context must be token-aware, not message-aware
- Middleware is the right abstraction for memory control
- Model and provider selection should be configuration-driven

Artemis is now:

- **Persistent** — State survives restarts
- **Bounded** — Token-aware context control
- **Configurable** — Models and limits via config
- **Correct** — No hidden assumptions

---

## What's Next

So far, Artemis has become a persistent, stateful agent. But it's still tied to a web browser.

In the next chapter, we'll make it usable **anywhere**:

- Integrating with Telegram
- Handling multiple users
- Mapping chat IDs to thread IDs
- Reusing the same agent logic

**Continue to:** [Telegram Integration](/telegram-integration)
