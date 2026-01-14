# **Chapter 5 — Refactoring for Persistence, Checkpointing, and Precise Context Control**

Chapter 4 marked a fundamental shift in Artemis:

> **Conversation state moved from the UI into the agent.**

We stopped manually replaying history and started treating memory as a first-class system concern.

However, that version of memory still had two major limitations:

1. **Memory was ephemeral** — restarting the app lost all conversations
2. **Context trimming was coarse** — based on message count, not token size

In this chapter, we refactor Artemis to solve both problems properly by introducing:

- **Persistent conversation state** using SQLite checkpoints
- **Token-aware context trimming** via middleware
- Cleaner agent construction boundaries
- Configurable LLM **provider and model selection**

This chapter is less about new features and more about **making the system correct and scalable**.

---

## **Why This Refactor Was Necessary**

Early prototypes often “work” by accident.

Before this refactor:

- Conversation state lived in memory
- Context grew without strict limits
- Restarting the app reset everything
- Debugging agent state was difficult

These issues don’t show up immediately—but they **break real agent systems** over time.

Instead of layering fixes, Artemis changes the architecture.

---

## **From Ephemeral State to Persistent Checkpoints**

The most important change in this chapter is **checkpointing**.

Rather than storing conversation state in RAM, Artemis now persists agent state to disk using **SQLite**.

---

## **SQLite-Based Checkpointing**

### **`backend/main.py`**

```python
from langgraph.checkpoint.sqlite import SqliteSaver

thread_id = "1"  # hard coded for simplicity, replace it later!

with SqliteSaver.from_conn_string("./db/short_memory.db") as checkpointer:
    agent = build_agent(checkpointer)
```

What this gives us:

- Conversation state survives restarts
- Agent state becomes inspectable
- Multi-turn flows become reliable
- No external infrastructure is required

SQLite is intentionally chosen:

- File-based
- Simple
- Good enough for local agents and early deployments

Each `thread_id` represents a **single conversation timeline**.

Later, this naturally maps to:

- User IDs
- Sessions
- Devices

---

## **Why `thread_id` Is Explicit**

Checkpointing only works if the agent knows _which_ state to load.

That’s why each invocation includes a thread identifier.

### **`backend/agent/message_handler.py`**

```python
response = agent.invoke(
    {"messages": request},
    {"configurable": {"thread_id": user_id}}
)
```

This makes conversation ownership explicit and avoids hidden global state.

---

## **What Disappeared After This Refactor**

You may notice what’s **no longer present**:

- No manual history replay
- No UI-side conversation storage
- No role conversion logic

Once checkpointing is enabled:

> **The agent owns memory.**

The UI sends only the new user message.
Everything else is recovered automatically.

This is a major simplification—and a sign of a healthy architecture.

---

## **The Context Window Is Still Finite**

Persistent memory introduces a new challenge.

If an agent remembers _everything_, it will eventually exceed the model’s context window.

Earlier versions trimmed memory like this:

- “Keep the last N messages”

This is unreliable because:

- Messages vary widely in token size
- Tool calls can inject large payloads
- Models enforce **token limits**, not message limits

To fix this, memory trimming must be **token-aware**.

---

## **Token-Aware Context Trimming with Middleware**

Instead of trimming memory inside UI or agent logic, Artemis introduces a **middleware layer**.

Middleware allows us to:

- Intercept agent state before the model runs
- Enforce global memory policy
- Keep agent logic clean

This is the correct abstraction for context control.

---

## **Precise Trimming Middleware**

### **`backend/memory/__init__.py`**

```python
@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    messages = state["messages"]
    new_messages = lc_trim_messages(
        messages,
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=settings.max_conversation_token_limit,
        start_on="human",
        end_on=("human", "tool"),
    )

    return {"messages": new_messages}
```

This is not a heuristic—it is **token-budget enforcement**.

---

## **What This Trimming Guarantees**

- Context never exceeds token budget
- Recent conversation is preserved
- Trimming starts at a human message
- Tool boundaries are respected
- The UI remains unaware of memory management

This is **semantic trimming**, not blunt deletion.

---

## **Configuration-Driven Memory Limits**

Token limits are configurable via environment variables.

### **`backend/config/__init__.py`**

```python
self.max_conversation_token_limit = environ.get(
    "MAX_CONVERSATION_TOKEN_LIMIT", 10240
)
```

Why this matters:

- Different models → different context windows
- Limits can be tuned without code changes
- Cost vs recall trade-offs become adjustable

Memory becomes **policy-driven**, not implementation-driven.

---

## **Making the OpenRouter Model Configurable**

Supporting multiple LLM providers is only half the story.

Within OpenRouter itself, there are many models with different trade-offs:

- Speed vs reasoning
- Cost vs quality
- Short vs long context

Hardcoding a model would defeat the flexibility of the system.

So Artemis makes the **model name configurable via environment variables**.

---

## **Model Configuration**

### **`backend/config/__init__.py`**

```python
self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
self.llm_model = environ.get("LLM_MODEL_NAME", "x-ai/grok-4-fast")
```

This introduces a clean separation of concerns:

- **Provider** decides _where_ requests go
- **Model name** decides _which model_ is used

No code changes are required to switch models.

---

## **Using the Configured Model**

### **`backend/agent/openrouter_agent.py`**

```python
def get_openrouter_llm(model: str):
    return ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
```

And in the agent builder:

```python
llm = get_openrouter_llm(settings.llm_model)
```

The agent remains provider-agnostic.
Configuration controls behavior.

---

## **Why `settings` Is a Global Object**

```python
settings = ArtemisConfig()
```

This is intentional.

If settings were recreated per request:

- Memory limits could diverge
- Middleware behavior could drift
- Debugging would become unpredictable

A single global configuration ensures:

> **Every component agrees on memory and model policy**

---

## **The Refactored Agent Constructor**

### **`backend/agent/__init__.py`**

```python
agent = create_agent(
    llm,
    tools=tools,
    system_prompt="You are a helpful assistant",
    checkpointer=checkpointer,
    middleware=[trim_messages],
)
```

This single line now defines:

- LLM backend
- Model selection
- Tool capabilities
- Persistent memory
- Context trimming policy

Nothing is hidden.
Nothing is accidental.

This is the _ideal shape_ of an agent constructor.

---

## **What Changed Conceptually**

Before:

- Memory was accidental
- Context growth was uncontrolled
- State lived outside the agent

After:

- Memory is intentional
- Context is bounded
- State lives with the agent

This is the difference between:

> **A chatbot that works** > **An agent that lasts**

---

## **End-to-End Flow After Refactor**

1. User sends input
2. Agent loads state from SQLite (`thread_id`)
3. Middleware trims context to token budget
4. Model is invoked
5. Updated state is checkpointed
6. Response is returned

The loop is now:

- Deterministic
- Persistent
- Scalable

---

## **Key Takeaways**

- Persistent agents require checkpointing
- SQLite is sufficient for early-stage systems
- Context must be token-aware, not message-aware
- Middleware is the right abstraction for memory control
- Model and provider selection should be configuration-driven

---

## **What’s Next**

So far, Artemis has become a **persistent, stateful agent** with controlled memory and flexible model selection.

The next step is to make it **usable outside a browser**.

In the next chapter, we’ll explore:

- Integrating Artemis with **Telegram**
- Mapping Telegram chats to `thread_id`s
- Handling multi-user conversations safely
- Reusing the same agent logic without UI changes

This is where Artemis moves from a local experiment
to a **real, always-available personal assistant**.
