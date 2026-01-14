---
sidebar_position: 6
title: Running as a Module
---

# Running as a Module

With the new multi-file structure, how you run Python matters.

## The Import Problem

With relative imports like:

```python
from backend.agent.message_handler import handle_message
from backend.agent import get_agent
```

Running the script directly fails:

```bash
python backend/main.py
# ModuleNotFoundError: No module named 'backend'
```

Python doesn't know `backend` is a package.

## The Solution: Run as Module

Instead of running as a script:

```bash
# Wrong
python backend/main.py
```

Run as a module:

```bash
# Correct
python -m backend.main
```

## Why This Works

When you use `python -m`:

1. Python treats the current directory as the package root
2. It resolves `backend` as a package
3. Relative imports work correctly
4. The project behaves like an installable application

## The Updated Entry Point

`backend/main.py`:

```python
from load_dotenv import load_dotenv
import gradio as gr

from backend.agent.message_handler import handle_message
from backend.agent import get_agent

load_dotenv()

if __name__ == "__main__":
    gr.ChatInterface(
        fn=lambda prompt, history: handle_message(get_agent(), prompt, history),
        title="Artemis AI",
    ).launch()
```

Notice the imports use full paths:

```python
from backend.agent.message_handler import handle_message
from backend.agent import get_agent
```

## Best Practice

This is a **best practice** for non-trivial Python projects:

| Approach | When to Use |
|----------|-------------|
| `python script.py` | Single-file scripts |
| `python -m package.module` | Multi-file packages |

As your project grows, always use module execution.

## Quick Reference

```bash
# Development
python -m backend.main

# With environment variables
LLM_PROVIDER=openai python -m backend.main

# Using .env file
# (load_dotenv handles this automatically)
python -m backend.main
```

---

## Chapter Summary

In this chapter, you learned:

- Why multi-backend support matters
- How to create a configuration layer
- The agent factory pattern for provider selection
- Adding OpenRouter as an alternative backend
- Running Python projects as modules

The system is now **provider-agnostic** — switching backends requires only a config change.

---

## What's Next

In the next chapter, we'll tackle a fundamental problem:

> Replaying full history breaks at scale.

You'll learn:

- Why LLMs are stateless
- What context windows are
- How to introduce memory without breaking agent purity
- How to trim old messages automatically

**Continue to:** [Memory Management](/memory-management)
