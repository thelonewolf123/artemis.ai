---
sidebar_position: 1
title: Building Agents
---

# Chapter 2: Building Agents

In the previous chapter, we learned how to:

- Talk to an LLM using an API
- Structure messages
- Enable tool calling
- Build a request → tool → response loop

Now it's time to **organize that logic into a real system**.

## What You'll Learn

This chapter walks through the **actual implementation** used in Artemis:

- Why an agent layer exists (separation of concerns)
- How tools are defined and registered
- How conversation history is reconstructed
- How the agent is invoked and returns a response
- How the agent connects to a Gradio UI

No pseudocode. No theory-only diagrams. Only what exists in the codebase.

## The Architecture

Here's the high-level structure:

```
backend/
├── agent/
│   └── openai_agent.py    ← LLM orchestration
├── tools/
│   └── weather.py         ← External capabilities
├── main.py                ← User interface (Gradio)
```

Each directory has a single responsibility:

- `tools/` → External capabilities
- `agent/` → LLM orchestration
- `main.py` → User interface

This separation is intentional and enables clean scaling.

## Chapter Sections

| Section | Topic |
|---------|-------|
| 2.1 | [Why an Agent Layer?](/building-agents/why-agent-layer) |
| 2.2 | [Defining Tools](/building-agents/defining-tools) |
| 2.3 | [Creating the Agent](/building-agents/creating-the-agent) |
| 2.4 | [Handling Messages](/building-agents/handling-messages) |
| 2.5 | [Connecting to Gradio](/building-agents/connecting-to-gradio) |

---

**This is where Artemis becomes a usable application — not just an experiment.**

Let's begin with [Why an Agent Layer?](/building-agents/why-agent-layer)
