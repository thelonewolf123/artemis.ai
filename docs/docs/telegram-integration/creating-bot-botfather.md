---
sidebar_position: 3
title: Creating a Bot with BotFather
---

# Creating a Bot with BotFather

Telegram bots are managed by a special bot called **BotFather**.

## Step 1: Find BotFather

1. Open Telegram
2. Search for **@BotFather**
3. Start a chat with it

## Step 2: Create Your Bot

Send the following commands:

```
/start
```

Then:

```
/newbot
```

BotFather will ask for:

1. **Display name** — What users see (e.g., "Artemis AI")
2. **Username** — Must end with `bot` (e.g., "artemis_ai_bot")

## Step 3: Get Your Token

After creation, BotFather provides a **Bot Token**:

```
Use this token to access the HTTP API:
123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
```

:::warning Keep This Secret
This token gives full control of your bot. Never share it publicly or commit it to git.
:::

## Step 4: Save the Token

Create or update your `.env` file:

```bash
TELEGRAM_API_KEY=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
```

Make sure `.env` is in your `.gitignore`.

## Step 5: Configure Artemis

Update your configuration to read the token:

`backend/config/__init__.py`:

```python
self.telegram_api_key = environ.get("TELEGRAM_API_KEY")
```

## Step 6: Install Dependencies

Artemis uses `python-telegram-bot`:

```bash
# Using uv
uv add python-telegram-bot

# Using pip
pip install python-telegram-bot
```

## Verifying Your Bot

Before coding, test that your bot exists:

1. Open Telegram
2. Search for your bot's username
3. Start a chat
4. Send a message

The message won't get a response yet (no code running), but you should see the bot exists.

---

## Key Takeaways

- BotFather creates and manages Telegram bots
- Each bot gets a unique token for authentication
- Store tokens in environment variables, not code
- Install `python-telegram-bot` for the integration

---

**Next:** [The Telegram Service Layer](/telegram-integration/telegram-service-layer)
