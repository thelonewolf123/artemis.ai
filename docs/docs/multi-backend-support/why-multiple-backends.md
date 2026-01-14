---
sidebar_position: 2
title: Why Multiple Backends?
---

# Why Multiple Backends?

Before adding the code, let's understand why this flexibility matters.

## The Single-Provider Problem

If your agent is hardcoded to use one provider:

```python
# Hardcoded - bad
llm = ChatOpenAI(model="gpt-4")
```

You face several issues:

| Problem | Impact |
|---------|--------|
| **Vendor lock-in** | Can't easily switch if prices change |
| **No fallbacks** | If OpenAI is down, your app is down |
| **No optimization** | Can't use cheaper models for simple tasks |
| **Testing is hard** | Can't swap in mock LLMs |

## The Multi-Provider Solution

With configuration-based selection:

```python
# Configurable - good
llm = get_llm(config.provider, config.model)
```

You gain:

| Benefit | Description |
|---------|-------------|
| **Flexibility** | Switch providers via config |
| **Resilience** | Add fallback providers |
| **Optimization** | Route to different models by task |
| **Testability** | Inject mock LLMs for testing |

## Real-World Scenarios

### Scenario 1: Cost Optimization

Use a cheaper model for simple questions:

```
Simple query → gpt-3.5 (cheap)
Complex reasoning → gpt-4 (expensive)
```

### Scenario 2: Provider Outage

OpenAI has an outage? Fail over to Anthropic:

```
Primary: OpenAI GPT-4
Fallback: Anthropic Claude
```

### Scenario 3: Compliance

Some data can't leave certain regions:

```
EU users → EU-hosted model
US users → US-hosted model
```

## The Key Principle

> **The rest of the system should not care which LLM is being used.**

The UI doesn't care.
The tools don't care.
The message handler doesn't care.

Only the agent factory knows — and that's intentional.

---

## Key Takeaways

- Single-provider setups create lock-in
- Configuration-based selection enables flexibility
- Real apps need fallbacks and optimization
- Isolate provider choice to one location

---

**Next:** [The Configuration Layer](/multi-backend-support/configuration-layer)
