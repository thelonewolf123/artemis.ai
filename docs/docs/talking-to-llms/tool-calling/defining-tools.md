---
sidebar_position: 3
title: Defining Tools
---

# Defining Tools

To enable tool calling, you need to:

1. Create the tool function
2. Describe it to the LLM
3. Handle the LLM's tool call requests

## Step 1: Create the Tool Function

Let's create a simple weather tool:

```python
from typing import Dict

def get_weather(arguments: Dict):
    """Get weather for a city"""
    city = arguments["city"]

    # Fake data for demonstration
    fake_db = {
        "Chennai": {"temp": 32, "condition": "Humid"},
        "London": {"temp": 12, "condition": "Cloudy"},
    }

    result = fake_db.get(city, {"temp": 22, "condition": "Unknown"})
    return {"city": city, **result}
```

This is just a regular Python function. It:

- Takes arguments as a dictionary
- Returns structured data
- Could call a real API, database, etc.

## Step 2: Describe the Tool to the LLM

The LLM needs to know:

- What tools exist
- What each tool does
- What parameters each tool accepts

This is done via the **system prompt**:

```python
SYSTEM_PROMPT = """
You are an AI assistant that uses tool calling.

Available tool:
{
  "name": "getWeather",
  "description": "Get current weather for a city",
  "input_schema": {
    "type": "object",
    "properties": {
      "city": { "type": "string", "description": "City name" }
    },
    "required": ["city"]
  }
}

When the user asks for weather, return ONLY a JSON object:
{
  "tool": "getWeather",
  "arguments": { "city": "..." }
}

Do not include any other text.
"""
```

This prompt acts like a **contract** between you and the LLM.

## The Tool Description Schema

Each tool description includes:

| Field | Purpose |
|-------|---------|
| `name` | Identifier for the tool |
| `description` | What the tool does (helps LLM decide when to use it) |
| `input_schema` | JSON Schema defining the parameters |

The input schema uses standard [JSON Schema](https://json-schema.org/) format.

## Step 3: Map Tool Names to Functions

Create a registry to connect tool names to implementations:

```python
TOOLS = {
    "getWeather": get_weather,
}
```

When the LLM requests a tool, you look it up here and execute it.

## Complete Tool Definition

Here's everything together:

```python
from typing import Dict

# 1. The function
def get_weather(arguments: Dict):
    city = arguments["city"]
    fake_db = {
        "Chennai": {"temp": 32, "condition": "Humid"},
        "London": {"temp": 12, "condition": "Cloudy"},
    }
    return {"city": city, **fake_db.get(city, {"temp": 22, "condition": "Unknown"})}

# 2. The registry
TOOLS = {
    "getWeather": get_weather,
}

# 3. The system prompt (describes tools to the LLM)
SYSTEM_PROMPT = """..."""  # As shown above
```

---

## Key Takeaways

- Tools are regular Python functions
- You describe tools to the LLM via the system prompt
- A registry maps tool names to functions
- The LLM learns what tools exist from your description

---

**Next:** [The Execution Loop](/talking-to-llms/tool-calling/tool-execution-loop)
