---
sidebar_position: 2
title: Why Tool Calling
---

# Why Tool Calling

Let's understand why tool calling exists and what it enables.

## The LLM's Isolation

Imagine an LLM as a very smart person locked in a room:

- They can read anything you slide under the door
- They can write responses back
- But they can't leave the room
- They can't make phone calls
- They can't look things up online

This is the LLM's reality. It only knows what's in its training data and what you tell it.

## Asking for Help

Now imagine this smart person can write notes asking *you* to do things:

> "Please look up the current weather in London and tell me the result."

You go check, come back, and slide the answer under the door:

> "It's 12°C and cloudy."

Now they can write a complete response using real, current information.

**This is tool calling.**

## What Tools Enable

With tool calling, your LLM can:

| Category | Examples |
|----------|----------|
| **Information** | Weather, search, stock prices |
| **Actions** | Send email, create calendar event |
| **Computation** | Calculate, run code |
| **Data** | Query database, read files |
| **Integration** | Call any API |

## The Trust Model

Tool calling has a clear trust boundary:

```
┌─────────────────────────────────────────────┐
│                 Your System                  │
│                                              │
│  ┌─────────────┐    ┌─────────────────────┐ │
│  │    LLM      │    │       Tools         │ │
│  │             │    │                     │ │
│  │  Decides    │───▶│  You control what   │ │
│  │  what to    │    │  tools exist and    │ │
│  │  call       │    │  how they work      │ │
│  └─────────────┘    └─────────────────────┘ │
└─────────────────────────────────────────────┘
```

- The LLM can suggest tool calls
- Your code decides whether to execute them
- You control what tools exist
- You control what they can do

## Real-World Analogy

Think of a personal assistant (the LLM) who can:

1. Understand your requests
2. Know what services are available (tools)
3. Ask you to call those services on their behalf
4. Use the results to give you a complete answer

They're helpful because of what you've enabled them to access — not because they have direct access themselves.

---

## Key Takeaways

- LLMs are isolated — they can't access external systems
- Tool calling lets LLMs express intent
- Your code executes tools safely
- This pattern enables real-world capabilities while maintaining control

---

**Next:** [Defining Tools](/talking-to-llms/tool-calling/defining-tools)
