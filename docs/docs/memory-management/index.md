---
sidebar_position: 1
title: Memory Management
---

# Chapter 4: Memory Management

In Chapter 0, we learned a fundamental truth about LLMs:

> **LLMs do not have memory.**

They don't remember past conversations, users, or previous answers. Every request is stateless unless *we* make it stateful.

This chapter introduces **conversation memory** into Artemis.

## What You'll Learn

By the end of this chapter, you'll understand:

- Why LLMs are stateless by design
- What context windows are and why they matter
- How to handle thread-based conversations
- Where to store conversation memory
- How to trim old messages automatically

## The Memory Problem

Until now, Artemis handled conversation continuity by:

1. Collecting all previous messages
2. Re-sending them to the LLM with each new query

This worked because conversations were short and token usage was low.

But this approach has a serious limitation: **it doesn't scale**.

## Chapter Sections

| Section | Topic |
|---------|-------|
| 4.1 | [LLM Statelessness](/memory-management/llm-statelessness) |
| 4.2 | [The Context Window Problem](/memory-management/context-window-problem) |
| 4.3 | [Thread-Based Memory](/memory-management/thread-based-memory) |
| 4.4 | [Memory Storage](/memory-management/memory-storage) |
| 4.5 | [Trimming Middleware](/memory-management/trimming-middleware) |

---

**This is where Artemis gains controlled, scalable memory.**

Let's begin with [LLM Statelessness](/memory-management/llm-statelessness)
