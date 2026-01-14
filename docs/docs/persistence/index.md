---
sidebar_position: 1
title: Persistence & Context Control
---

# Chapter 5: Persistence & Context Control

Chapter 4 marked a fundamental shift in Artemis:

> **Conversation state moved from the UI into the agent.**

However, that version of memory still had two major limitations:

1. **Memory was ephemeral** — Restarting the app lost all conversations
2. **Context trimming was coarse** — Based on message count, not token size

This chapter refactors Artemis to solve both problems properly.

## What You'll Learn

By the end of this chapter, you'll understand:

- Why persistent checkpointing matters
- How to use SQLite for conversation storage
- Why token-aware trimming is important
- How to make model selection configurable

## Why This Refactor Was Necessary

Early prototypes often "work" by accident. Before this refactor:

| Issue | Impact |
|-------|--------|
| In-memory state | Everything lost on restart |
| Message-count limits | Doesn't match token limits |
| Hardcoded models | Inflexible |
| Hidden state | Hard to debug |

These issues don't show up immediately — but they **break real agent systems** over time.

## Chapter Sections

| Section | Topic |
|---------|-------|
| 5.1 | [Why Persistence?](/persistence/why-persistence) |
| 5.2 | [SQLite Checkpointing](/persistence/sqlite-checkpointing) |
| 5.3 | [Token-Aware Trimming](/persistence/token-aware-trimming) |
| 5.4 | [Configurable Models](/persistence/configurable-models) |

---

**This is where Artemis becomes a long-running, production-ready agent.**

Let's begin with [Why Persistence?](/persistence/why-persistence)
