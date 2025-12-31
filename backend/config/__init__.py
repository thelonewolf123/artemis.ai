from typing import Literal, Any
from backend.memory.storage import get_memory_saver
from os import environ


class ArtemisConfig:
    llm_provider: Literal["openrouter", "openai"]
    max_conversation_limit: int
    checkpointer: Any

    def __init__(self):
        self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
        self.max_conversation_limit = environ.get("MAX_CONVERSATION_LIMIT", 50)
        self.checkpointer = get_memory_saver()


settings = ArtemisConfig()  # global object to prevent memory being recreated
