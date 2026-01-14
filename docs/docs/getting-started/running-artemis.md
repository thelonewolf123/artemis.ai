---
sidebar_position: 2
title: Running Artemis
---

# Running Artemis

Once you've completed the [installation](/getting-started/installation), you can start Artemis in different modes.

## Running the Web Interface

Start Artemis with the Gradio chat interface:

```bash
python -m backend.main
```

This launches a web-based chat UI. Open your browser to the URL shown in the terminal (typically `http://localhost:7860`).

:::note Why `python -m`?
Running as a module (`python -m backend.main`) instead of a script (`python backend/main.py`) ensures Python correctly resolves imports. This is a best practice for non-trivial Python projects.
:::

## Running the Telegram Bot

To run Artemis as a Telegram bot:

1. Create a bot via [@BotFather](https://t.me/BotFather) on Telegram
2. Add your bot token to `.env`:

```bash
TELEGRAM_API_KEY=your_bot_token_here
```

3. Start the bot:

```bash
python -m backend.main
```

The bot will start polling for messages. Send a message to your bot on Telegram to test it.

## Configuration Options

Artemis behavior can be customized via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `openrouter` | LLM provider (`openai` or `openrouter`) |
| `LLM_MODEL_NAME` | `x-ai/grok-4-fast` | Model to use |
| `MAX_CONVERSATION_TOKEN_LIMIT` | `10240` | Max tokens in context |
| `OPENAI_API_KEY` | - | Your API key |
| `TELEGRAM_API_KEY` | - | Telegram bot token |

## Verifying It Works

Once running, try these test messages:

1. **Basic conversation**: "Hello, who are you?"
2. **Tool usage**: "What's the weather in London?"
3. **Memory test**: Tell it your name, then ask "What's my name?" in a follow-up message

If all three work, Artemis is properly configured.

---

## Next Steps

Now that Artemis is running, it's time to understand how it works. Start with [Understanding LLMs](/understanding-llms) to learn the fundamentals.
