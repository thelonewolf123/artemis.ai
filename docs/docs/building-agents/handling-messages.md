---
sidebar_position: 5
title: Handling Messages
---

# Handling Messages

Gradio provides conversation history in a UI-specific format. The agent expects LangChain message objects. Translation happens in `handle_message`.

## The Message Handler

```python
from langchain.messages import HumanMessage, AIMessage
from typing import List


def handle_message(last_message: str, history: List):
    agent = get_openai_agent()
    request = []

    # Convert history to LangChain format
    for message in history:
        if message["role"] == "assistant":
            request.append(AIMessage(message["content"][0]["text"]))
        else:
            request.append(HumanMessage(message["content"][0]["text"]))

    # Add the new message
    request.append(HumanMessage(last_message))

    # Invoke the agent
    response = agent.invoke({"messages": request})

    return response["messages"][-1].content
```

## Understanding the Flow

### Input Parameters

- `last_message` — The latest user input
- `history` — Full conversation from Gradio

### Gradio's Format

Gradio stores messages like this:

```json
{
  "role": "assistant",
  "content": [{ "text": "Hello!" }]
}
```

### LangChain's Format

LangChain expects:

- `HumanMessage("text")` for user messages
- `AIMessage("text")` for assistant messages

## Reconstructing the Conversation

The loop converts each historical message:

```python
for message in history:
    if message["role"] == "assistant":
        request.append(AIMessage(message["content"][0]["text"]))
    else:
        request.append(HumanMessage(message["content"][0]["text"]))
```

This **replays the entire conversation** so the LLM has full context.

:::tip Why Replay?
Remember: LLMs are stateless. They don't remember previous messages. The only way to maintain context is to send the full history each time.
:::

## Adding the New Message

```python
request.append(HumanMessage(last_message))
```

Now the message list contains:

- Full conversation history
- Latest user input at the end

This mirrors how chat-completion APIs work internally.

## Invoking the Agent

```python
response = agent.invoke({"messages": request})
```

At this point:

- The agent receives all messages
- It decides if a tool is needed
- Tools may be executed internally
- The agent produces a final response

All of that happens **inside the agent abstraction**. The UI doesn't know or care about the details.

## Extracting the Response

```python
return response["messages"][-1].content
```

The agent returns a list of messages. We extract:

- The **last message** (the final response)
- Its **content** (the text to display)

That's all the UI needs.

---

## Key Takeaways

- UI and agent use different message formats
- Conversation history is reconstructed each time
- The agent handles tools internally
- Only the final response is returned to the UI

---

**Next:** [Connecting to Gradio](/building-agents/connecting-to-gradio)
