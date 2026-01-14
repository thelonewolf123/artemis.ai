---
sidebar_position: 3
title: Tokens Explained
---

# Tokens Explained

LLMs don't think in words or sentences. They operate on **tokens**.

## What is a Token?

A token is the smallest unit of text that an LLM processes. It can be:

- A complete word: `hello` → 1 token
- Part of a word: `understanding` → `under` + `standing` = 2 tokens
- Punctuation: `.` or `!` → 1 token each
- Whitespace: A space character → often 1 token

## Examples of Tokenization

Here's how common text gets broken into tokens:

| Text | Tokens | Count |
|------|--------|-------|
| `Hello world` | `Hello`, ` world` | 2 |
| `ChatGPT` | `Chat`, `G`, `PT` | 3 |
| `I'm running late` | `I`, `'m`, ` running`, ` late` | 4 |
| `https://example.com` | Many small pieces | ~7 |

:::tip Try it yourself
OpenAI provides a free [tokenizer tool](https://platform.openai.com/tokenizer) where you can paste text and see exactly how it's tokenized.
:::

## Why Tokens Matter

Understanding tokens is important for several reasons:

### 1. Pricing

API providers charge **per token**, not per word or character.

```
1,000 tokens ≈ 750 words (roughly)
```

### 2. Context Limits

Every LLM has a **context window** — the maximum number of tokens it can process at once:

| Model | Context Window |
|-------|---------------|
| GPT-3.5 | ~4,000 tokens |
| GPT-4 | ~8,000 - 128,000 tokens |
| Claude 3 | ~200,000 tokens |

If your input + output exceeds this limit, the request fails.

### 3. Generation Speed

LLMs generate **one token at a time**. A 100-token response requires 100 prediction steps. This is why:

- Longer responses take more time
- You see text appear word-by-word in chat interfaces

## The Tokenization Process

When you send text to an LLM:

1. Your text is converted into a sequence of token IDs
2. The model processes these IDs
3. The model outputs new token IDs
4. Those IDs are converted back to text

```
"Hello world" → [15496, 995] → Model → [1212, 318] → "How are"
```

You never see the token IDs — the API handles conversion automatically.

---

## Key Takeaways

- Tokens are the atomic units LLMs work with
- One token ≠ one word (often smaller)
- Tokens determine pricing and context limits
- LLMs generate output one token at a time

---

**Next:** [The Token Generation Loop](/understanding-llms/token-generation-loop) — See how tokens are generated step by step
