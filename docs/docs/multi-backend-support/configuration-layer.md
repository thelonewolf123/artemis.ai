---
sidebar_position: 3
title: The Configuration Layer
---

# The Configuration Layer

The first step toward multi-backend support is a central configuration object.

## The Configuration Class

`backend/config/__init__.py`:

```python
from typing import Literal
from os import environ


class ArtemisConfig:
    llm_provider: Literal["openrouter", "openai"]

    def __init__(self):
        self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
```

## How It Works

| Feature | Implementation |
|---------|----------------|
| **Type hints** | `Literal["openrouter", "openai"]` documents valid options |
| **Environment-driven** | Reads from `LLM_PROVIDER` env var |
| **Sensible default** | Falls back to `"openrouter"` if not set |

## Using Environment Variables

Set the provider when running:

```bash
# Use OpenRouter
export LLM_PROVIDER=openrouter
python -m backend.main

# Use OpenAI
export LLM_PROVIDER=openai
python -m backend.main
```

Or in a `.env` file:

```bash
LLM_PROVIDER=openrouter
OPENAI_API_KEY=your_key_here
```

## Why Environment Variables?

Environment variables are ideal for configuration because:

1. **No code changes** — Switch providers without touching code
2. **12-factor app pattern** — Industry standard
3. **Secrets stay out of git** — API keys never in source
4. **Easy deployment** — Different envs have different configs

## Accessing Configuration

Throughout the codebase:

```python
from backend.config import ArtemisConfig

config = ArtemisConfig()
print(config.llm_provider)  # "openrouter" or "openai"
```

## Making Configuration Global

To prevent recreating config objects:

```python
# backend/config/__init__.py
settings = ArtemisConfig()  # Single instance
```

Now import it directly:

```python
from backend.config import settings

print(settings.llm_provider)
```

This ensures consistent configuration across all modules.

---

## Key Takeaways

- Configuration is centralized in one class
- Environment variables drive behavior
- Defaults are explicit in code
- A global `settings` object prevents recreation

---

**Next:** [Agent Factory Pattern](/multi-backend-support/agent-factory-pattern)
