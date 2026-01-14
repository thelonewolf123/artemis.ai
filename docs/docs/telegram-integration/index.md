---
sidebar_position: 1
title: Telegram Integration
---

# Chapter 6: Telegram Integration

Until now, Artemis lived in controlled environments:

- A local web UI
- A single user
- Short-lived sessions

That's useful for learning — but not how assistants are used in real life.

This chapter integrates Artemis with **Telegram**, turning it into a **real, always-on, multi-user AI agent**.

## What You'll Learn

By the end of this chapter, you'll understand:

- Why Telegram is a great first integration
- How to create a bot using BotFather
- How to wire Artemis to Telegram
- How to handle multiple users safely
- How to map Telegram chats to agent memory

## Why Telegram?

Telegram provides exactly what an agent system needs:

| Feature | Benefit |
|---------|---------|
| Text-first interface | Perfect for LLMs |
| Built-in user IDs | Easy identity handling |
| Long-running bots | Always available |
| No UI maintenance | Focus on logic |
| Multi-user native | Real-world testing |

Most importantly:

> **Telegram forces you to design memory and identity correctly.**

## Chapter Sections

| Section | Topic |
|---------|-------|
| 6.1 | [Why Telegram?](/telegram-integration/why-telegram) |
| 6.2 | [Creating a Bot with BotFather](/telegram-integration/creating-bot-botfather) |
| 6.3 | [The Telegram Service Layer](/telegram-integration/telegram-service-layer) |
| 6.4 | [Multi-User Handling](/telegram-integration/multi-user-handling) |
| 6.5 | [Wiring It Together](/telegram-integration/wiring-it-together) |

---

**This is where Artemis leaves the browser and becomes an always-on, multi-user assistant.**

Let's begin with [Why Telegram?](/telegram-integration/why-telegram)
