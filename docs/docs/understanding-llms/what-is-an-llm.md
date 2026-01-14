---
sidebar_position: 2
title: What is an LLM?
---

# What is an LLM?

At their core, **Large Language Models (LLMs) are autocomplete systems** — but extremely powerful ones.

## The Simplest Explanation

An LLM does **one job**:

> **Given some text, predict the most likely next token.**

That's it.

- No awareness
- No consciousness
- No understanding — at least not in the human sense

Yet, because these predictions are **statistically very accurate**, the output *feels* intelligent.

## An Analogy: Autocomplete on Steroids

You've used autocomplete on your phone. When you type "I'm running", your phone might suggest "late" as the next word.

LLMs work the same way, but:

- They're trained on billions of text examples
- They can predict many tokens in sequence
- They consider much more context (thousands of words)
- Their predictions are remarkably coherent

Think of an LLM as **the world's most sophisticated text prediction engine**.

## What LLMs Are NOT

Understanding what LLMs aren't is just as important:

| Common Belief | Reality |
|---------------|---------|
| LLMs "know" facts | They predict likely text based on training data |
| LLMs "think" about answers | They generate tokens sequentially without planning |
| LLMs "remember" conversations | Each request is stateless unless we add memory |
| LLMs "understand" meaning | They recognize patterns, not meaning |

:::info Key Insight
LLMs don't retrieve information from a database. They generate text that *seems* like it contains information because similar text appeared in their training data.
:::

## Why This Mental Model Matters

When you understand that LLMs are prediction engines, many behaviors make sense:

- **Hallucinations**: The model predicts plausible-sounding text even when facts don't exist
- **Consistency issues**: Each prediction is independent — there's no global "memory"
- **Prompt sensitivity**: Small wording changes affect which patterns the model activates

---

## Key Takeaways

- LLMs predict the next token given input text
- They don't "know" or "understand" — they pattern-match
- The output feels intelligent because predictions are statistically accurate
- Every request is stateless by default

---

**Next:** [Tokens Explained](/understanding-llms/tokens-explained) — Learn what tokens actually are
