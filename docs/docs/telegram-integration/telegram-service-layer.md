---
sidebar_position: 4
title: The Telegram Service Layer
---

# The Telegram Service Layer

Telegram integration lives in a dedicated service module, separate from agent logic.

## The Service Structure

`backend/services/telegram.py`:

```python
from typing import Callable, Optional
from backend.config import settings

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    Application,
    MessageHandler,
)
```

This layer handles:

- Receiving messages from Telegram
- Extracting user/chat identity
- Passing messages to the agent
- Sending responses back

It does **not** contain any agent logic.

## The Telegram Class

```python
class Telegram:
    app: Application
    handle_message: Callable[[str, int], str]

    def __init__(
        self,
        on_message: Optional[Callable[[str, int], str]] = None,
    ):
        self.app = ApplicationBuilder().token(
            settings.telegram_api_key
        ).build()
        
        if on_message:
            self.handle_message = on_message
```

The constructor:

1. Builds a Telegram application using the API token
2. Stores the message handler callback

## Handling Commands

Register a `/start` command for first-time users:

```python
self.app.add_handler(CommandHandler("start", self.hello))
```

The handler:

```python
async def hello(
    self,
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}"
    )
```

This provides a friendly greeting when users first interact with the bot.

## Handling Messages

Register a handler for all text messages:

```python
self.app.add_handler(
    MessageHandler(None, self.message_handler, True)
)
```

The handler:

```python
async def message_handler(
    self,
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    thread_id = update.effective_chat.id
    user_text = update.message.text

    ai_response = self.handle_message(user_text, thread_id)

    await update.message.reply_text(ai_response)
```

This is the **most important part** — it connects Telegram to your agent.

## Starting the Bot

```python
def start(self):
    print("Telegram AI bot is running!")
    self.app.run_polling()
```

`run_polling()` starts an infinite loop that:

1. Polls Telegram for new messages
2. Dispatches them to handlers
3. Sends responses back

## Service Layer Principles

| Principle | Implementation |
|-----------|----------------|
| **Single responsibility** | Only handles Telegram transport |
| **Callback-based** | Agent logic injected via `on_message` |
| **Stateless transport** | No conversation state in this layer |
| **Clean interface** | Just text in, text out |

---

## Key Takeaways

- Telegram logic lives in a dedicated service layer
- The service handles transport, not reasoning
- Message handling is callback-based
- The agent is injected, not embedded

---

**Next:** [Multi-User Handling](/telegram-integration/multi-user-handling)
