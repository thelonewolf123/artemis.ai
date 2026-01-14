---
sidebar_position: 1
title: Multi-Backend Support
---

# Chapter 3: Multi-Backend Support

Up until now, Artemis has behaved like a single-model system. But real-world agentic systems rarely stay that way.

Different models have different strengths:

| Model Type | Strengths |
|------------|-----------|
| Cheaper models | Lower cost, higher throughput |
| Faster models | Lower latency for real-time apps |
| Reasoning models | Better at complex tasks |
| Different providers | Avoid vendor lock-in |

## What You'll Learn

This chapter evolves Artemis from a **single-backend agent** into a **multi-LLM system** that can switch providers without changing UI or agent logic.

You'll learn how to:

- Add OpenRouter alongside OpenAI
- Switch LLM providers using configuration
- Isolate provider-specific logic behind an agent factory
- Use proper relative imports
- Run the project correctly with `python -m`

## Why This Matters

Hardcoding a single model creates tight coupling:

- UI depends on the model
- Agent depends on the provider
- Switching models requires code changes everywhere

Artemis adopts a simple rule:

> **The rest of the system should not care which LLM is being used.**

This is a foundational principle for scalable agent systems.

## Chapter Sections

| Section | Topic |
|---------|-------|
| 3.1 | [Why Multiple Backends?](/multi-backend-support/why-multiple-backends) |
| 3.2 | [The Configuration Layer](/multi-backend-support/configuration-layer) |
| 3.3 | [Agent Factory Pattern](/multi-backend-support/agent-factory-pattern) |
| 3.4 | [Adding OpenRouter](/multi-backend-support/adding-openrouter) |
| 3.5 | [Running as a Module](/multi-backend-support/running-as-module) |

---

**This is where Artemis becomes configurable, flexible, and production-aligned.**

Let's begin with [Why Multiple Backends?](/multi-backend-support/why-multiple-backends)
