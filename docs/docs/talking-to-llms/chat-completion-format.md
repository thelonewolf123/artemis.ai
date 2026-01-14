---
sidebar_position: 4
title: The Chat Completion Format
---

# The Chat Completion Format

Most modern LLM APIs use a **chat-based format**, even if you're not building a chatbot.

## The Message Structure

A typical API request contains:

- A **model** name
- A list of **messages**

Each message has:

- A `role`: `system`, `user`, or `assistant`
- A `content` string

## Understanding Roles

| Role | Purpose | Example |
|------|---------|---------|
| `system` | Sets behavior and personality | "You are a helpful assistant" |
| `user` | The human's input | "What is an LLM?" |
| `assistant` | The model's response | "An LLM is a language model..." |

## Example Message List

```json
[
  { "role": "system", "content": "You are a helpful assistant." },
  { "role": "user", "content": "What is an LLM?" }
]
```

When you send this, the model's job is:

> **Predict the next `assistant` message.**

## Why Chat Format?

Even for single questions, the chat format is useful because:

1. **System messages** let you control behavior
2. **History** can be included for context
3. **It's standardized** across providers

## A Full Conversation Example

Here's how a multi-turn conversation looks:

```json
[
  { "role": "system", "content": "You are a helpful assistant." },
  { "role": "user", "content": "What is Python?" },
  { "role": "assistant", "content": "Python is a programming language known for its readability." },
  { "role": "user", "content": "What can I build with it?" }
]
```

The model sees the entire history and generates a response that continues the conversation naturally.

## The Request and Response

### Request Body

```json
{
  "model": "gpt-4",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "Hello!" }
  ]
}
```

### Response Body

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      }
    }
  ]
}
```

The response is wrapped in a `choices` array (to support multiple completions, though usually there's just one).

---

## Key Takeaways

- LLM APIs use a chat-based message format
- Three roles: `system`, `user`, `assistant`
- System messages configure behavior
- The model predicts the next assistant message
- Full conversation history is sent each time

---

**Next:** [Calling an LLM from Python](/talking-to-llms/calling-llm-from-python)
