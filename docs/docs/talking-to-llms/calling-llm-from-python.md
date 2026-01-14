---
sidebar_position: 5
title: Calling an LLM from Python
---

# Calling an LLM from Python

Let's put everything together and make an actual API call.

## A Minimal LLM Client

Here's a simple Python function that calls a chat completion API:

```python
import os
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENAI_API_KEY")

def call_llm(messages, model="x-ai/grok-4-fast"):
    response = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        json={
            "model": model,
            "messages": messages,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
```

## Breaking Down the Code

### 1. Configuration

```python
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENAI_API_KEY")
```

- The URL is the API endpoint
- The key comes from environment variables

### 2. Headers

```python
headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}
```

- `Content-Type` tells the server we're sending JSON
- `Authorization` provides our API key

### 3. Request Body

```python
json={
    "model": model,
    "messages": messages,
}
```

- `model` specifies which LLM to use
- `messages` is the conversation history

## Using the Function

```python
# Simple question
response = call_llm([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is 2 + 2?"}
])

# Extract the answer
answer = response["choices"][0]["message"]["content"]
print(answer)  # "4" or "2 + 2 equals 4"
```

## What Can We Do Now?

At this point:

- We can send messages
- We can receive text responses
- The model understands context

But the model is still **passive**. It can only talk — it can't take actions.

To build an *agent*, we need to enable **tool calling**.

---

## Key Takeaways

- LLM calls are simple HTTP POST requests
- Send messages, receive a response
- The model parameter selects which LLM to use
- Response content is in `choices[0]["message"]["content"]`

---

**Next:** [Tool Calling](/talking-to-llms/tool-calling/) — Enable your LLM to take real actions
