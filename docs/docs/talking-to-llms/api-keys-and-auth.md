---
sidebar_position: 3
title: API Keys and Authentication
---

# API Keys and Authentication

Before you can call an LLM API, you need an **API key**.

## What is an API Key?

An API key is a secret string that tells the server:

- **Who you are** — Your account identity
- **How much to bill** — Usage is tracked per key
- **Whether you're authorized** — Access control

Think of it like a password specifically for API access.

## Getting an API Key

### OpenAI

1. Visit [platform.openai.com](https://platform.openai.com)
2. Create an account or sign in
3. Navigate to **API Keys** section
4. Click **Create new secret key**
5. Copy and save the key immediately (you won't see it again)

### OpenRouter

1. Visit [openrouter.ai](https://openrouter.ai)
2. Create an account
3. Go to **Keys** section
4. Generate a new key

## Storing API Keys Safely

**Never hardcode API keys in your source code.**

Instead, use environment variables:

```bash
# Linux / macOS
export OPENAI_API_KEY="your_api_key_here"

# Or create a .env file
echo 'OPENAI_API_KEY=your_api_key_here' > .env
```

In Python, access the key like this:

```python
import os

API_KEY = os.environ.get("OPENAI_API_KEY")
```

## Why Environment Variables?

| Approach | Security | Flexibility |
|----------|----------|-------------|
| Hardcoded in code | Very bad — exposed in git | Poor |
| Environment variable | Good — not in code | Good |
| `.env` file (git-ignored) | Good — local only | Very good |
| Secret manager | Best — encrypted | Excellent |

For development, a `.env` file is the sweet spot.

:::warning Security Reminder
- Add `.env` to your `.gitignore`
- Never commit API keys to version control
- Rotate keys if they're ever exposed
:::

## Using the Key in Requests

API keys are typically sent in the `Authorization` header:

```python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}
```

The `Bearer` prefix is a standard pattern for token-based authentication.

---

## Key Takeaways

- API keys authenticate your requests
- Never hardcode keys in source code
- Use environment variables or `.env` files
- Keys are sent in the `Authorization` header

---

**Next:** [The Chat Completion Format](/talking-to-llms/chat-completion-format)
