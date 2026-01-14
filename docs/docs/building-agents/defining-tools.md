---
sidebar_position: 3
title: Defining Tools
---

# Defining Tools in Artemis

Tools in Artemis are Python functions decorated with `@tool`.

## A Real Tool Example

Here's the weather tool from `backend/tools/weather.py`:

```python
from langchain.tools import tool
import random


@tool
def get_weather(city: str) -> int:
    """Return weather for given city in celsius"""
    return random.randint(20, 50)
```

## How the Decorator Works

The `@tool` decorator does several things automatically:

| Feature | How It Works |
|---------|--------------|
| **Name** | Derived from function name (`get_weather`) |
| **Description** | Extracted from docstring |
| **Input Schema** | Generated from type hints (`city: str`) |
| **Discoverability** | Makes tool usable by agents |

## Type Hints Matter

The function signature becomes the tool's input schema:

```python
def get_weather(city: str) -> int:
#              ↑ Required parameter of type string
#                       ↑ Return type (for documentation)
```

The LLM sees this as:

```json
{
  "name": "get_weather",
  "description": "Return weather for given city in celsius",
  "parameters": {
    "type": "object",
    "properties": {
      "city": { "type": "string" }
    },
    "required": ["city"]
  }
}
```

## Docstrings Are Important

The docstring becomes the tool's description:

```python
"""Return weather for given city in celsius"""
```

This helps the LLM decide **when** to use the tool. Write clear, descriptive docstrings.

## Execution Happens Automatically

When using LangChain agents:

1. You register tools with the agent
2. The LLM decides to call a tool
3. LangChain automatically executes the function
4. The result is passed back to the LLM

You don't need to write the execution loop manually.

## Adding More Tools

To add a new tool:

1. Create a new file in `backend/tools/`
2. Define your function with `@tool`
3. Register it in the agent

Example: A search tool

```python
# backend/tools/search.py
from langchain.tools import tool


@tool
def search_web(query: str) -> str:
    """Search the web for information"""
    # Call a search API here
    return f"Results for: {query}"
```

Then register it:

```python
# backend/agent/openai_agent.py
from tools.weather import get_weather
from tools.search import search_web

agent = create_agent(
    "gpt-4.1",
    tools=[get_weather, search_web],
    system_prompt="...",
)
```

---

## Key Takeaways

- Tools are Python functions with `@tool` decorator
- Type hints define the input schema
- Docstrings describe when to use the tool
- LangChain handles execution automatically
- Adding tools is simple: define and register

---

**Next:** [Creating the Agent](/building-agents/creating-the-agent)
