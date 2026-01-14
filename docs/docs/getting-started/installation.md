---
sidebar_position: 1
title: Installation
---

# Installation

This guide will help you set up Artemis AI on your local machine.

## Prerequisites

Before you begin, make sure you have:

- **Python 3.10+** installed
- **pip** or **uv** package manager
- An **API key** from OpenAI or OpenRouter

## Step 1: Clone the Repository

```bash
git clone https://github.com/thelonewolf123/artemis.ai.git
cd artemis.ai
```

## Step 2: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Required: Your API key
OPENAI_API_KEY=your_api_key_here

# Optional: Choose your LLM provider
LLM_PROVIDER=openrouter  # or "openai"

# Optional: Choose your model (for OpenRouter)
LLM_MODEL_NAME=x-ai/grok-4-fast
```

:::tip Getting an API Key

- **OpenAI**: Visit [platform.openai.com](https://platform.openai.com) to create an account and generate an API key
- **OpenRouter**: Visit [openrouter.ai](https://openrouter.ai) for access to multiple models through a single API
  :::

## Step 3: Install Dependencies

Using **uv** (recommended):

```bash
cd backend
uv sync
```

Or using **pip**:

```bash
cd backend
pip install -e .
```

## Project Structure

After installation, your project should look like this:

```
artemis.ai/
├── docs/           ← This documentation
├── backend/        ← The runnable implementation
│   ├── agent/      ← LLM orchestration
│   ├── tools/      ← External capabilities
│   ├── memory/     ← Conversation storage
│   ├── config/     ← Configuration
│   ├── services/   ← Telegram, etc.
│   └── main.py     ← Entry point
└── .env            ← Your environment variables
```

---

## Next Steps

Once installed, proceed to [Running Artemis](/getting-started/running-artemis) to start the application.
