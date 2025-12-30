# 🏹 Artemis AI

**A Practical Guide to Building Agentic AI Systems**

Artemis is a **learning-first AI project** focused on understanding how modern **Large Language Models (LLMs)** can be composed into real, extensible, and controllable **agentic AI systems**.

This repository is intentionally designed as:

> 📘 **A book you can read**  
> 🧪 **A system you can run**

Rather than hiding complexity behind frameworks, Artemis exposes the _core building blocks_ behind agentic systems—step by step, from first principles.

---

## 🎯 Why Artemis?

Most LLM tutorials jump straight to frameworks.

Artemis does the opposite.

It starts by answering:

- What an LLM _actually_ is
- How token prediction works
- How models are accessed over APIs
- How tools, memory, and control flow emerge naturally

Only then does it move toward **agents**.

---

## 🧠 What Artemis Will Become

Artemis aims to evolve into a fully capable **personal AI assistant**, with support for:

- Natural conversational querying
- Internet access for real-time information
- Long-term memory storage
- Document ingestion with **RAG**
- Structured user data
- Tool extensibility (MCP-style)
- Reminders and scheduled actions
- Multi-step reasoning and workflows

Each capability is introduced **incrementally**, not magically.

---

## 📚 Learning-First Structure

The repository is split into **two major parts**:

```

artemis.ai/
├── docs/        ← The book (concepts & explanations)
├── backend/     ← Runnable implementation

```

### Why this split?

- `docs/` explains **why things exist**
- `backend/` shows **how they actually work**
- You can read without running
- Or run without reading
- Best experience comes from doing both

---

## 📖 Chapters (Docs)

All chapters live inside the `docs/` folder and are meant to be read **in order**.

---

### **Chapter 0 — Understanding LLMs**

📄 `docs/CHAPTER-0.md`

**Conceptual foundations**

This chapter answers the most important questions first:

- What is a Large Language Model, really?
- Why are LLMs described as “autocomplete on steroids”?
- What are tokens?
- How does token-by-token generation work?
- Why does chat feel conversational?

You’ll learn:

- Why LLMs are not intelligent in the human sense
- How sequential token prediction creates fluent language
- Where the illusion of reasoning comes from

➡️ **Start here if you’re new to LLMs or want first-principles clarity**

---

### **Chapter 1 — Talking to an LLM**

📄 `docs/CHAPTER-1.md`

**From theory to real code**

This chapter bridges concepts to implementation:

- Where LLMs actually run (remote servers)
- How we talk to them using HTTP APIs
- What API keys are and why they exist
- How chat-completion style APIs work
- Why **tool calling** is the foundation of agentic systems

You’ll see:

- A minimal Python LLM client
- Structured message formats (`system`, `user`, `assistant`)
- A full **tool-calling loop**
- How LLMs express _intent_ instead of executing code

➡️ **This is where Artemis starts behaving like an agent**

---

### **Chapter 2 — Building an Agent and Connecting It to a UI**

📄 `docs/CHAPTER-2.md`

In this chapter, we move from isolated LLM calls to a **structured agent architecture** and connect it to a real user interface.

This chapter explains the **exact code used in the Artemis backend**, including:

- Why an `openai_agent` layer exists
- How tools are defined and registered
- How conversation history from Gradio is reconstructed into LLM messages
- How the agent is invoked and returns a final response
- How the agent is wired into a Gradio `ChatInterface`

You’ll walk through:

- `backend/agent/openai_agent.py` — the orchestration layer that owns reasoning
- `backend/tools/weather.py` — a minimal example of tool calling
- `backend/main.py` — a thin Gradio UI that delegates all logic to the agent

This chapter emphasizes **clean boundaries**:

- The UI stays simple
- The agent owns control flow
- Tools remain explicit and safe

➡️ **This is where Artemis becomes a usable application — not just an experiment**

---

## 🧪 Backend (Runnable Code)

The `backend/` directory contains a **minimal but real implementation** of Artemis.

```

backend/
├── agent/
│   └── openai_agent.py     ← LLM + tools orchestration
├── tools/
│   └── weather.py          ← Example external tool
├── main.py                 ← Gradio chat interface
├── pyproject.toml
└── .env (ignored)

```

### Key Ideas Demonstrated

- **Agent abstraction**: LLM + tools
- **Tool registration** and invocation
- **Conversation history replay**
- **UI layer separated from agent logic**

The backend intentionally stays simple so the **architecture remains visible**.

---

## ▶️ Running Artemis Locally

1. Set up environment variables:

```bash
export OPENAI_API_KEY=your_key_here
```

2. Install dependencies (using `uv`, `pip`, or similar)

3. Start the app:

```bash
python backend/main.py
```

This launches a simple **Gradio chat UI** connected to the agent.

---

## 🧭 Roadmap (High Level)

Upcoming chapters will cover:

- Prompt roles and behavioral control
- Memory (short-term vs long-term)
- RAG pipelines (documents → embeddings → retrieval)
- Tool routing and orchestration
- Scheduling and background execution
- Multi-agent patterns
- Failure handling and guardrails

Each topic will follow the same rule:

> **Concept first, code second**

---

## 🤝 Who Is This For?

Artemis is ideal for:

- Developers curious about **agentic AI**
- Engineers tired of black-box abstractions
- People who want to _understand_, not just integrate
- Builders who prefer **first principles over frameworks**

---

## 🏁 Final Note

Artemis is intentionally built **slowly, transparently, and honestly**.

If you follow the chapters in order, you won’t just learn how to _use_ LLMs —
you’ll learn how to **design systems around them**.

Welcome to Artemis. 🏹
