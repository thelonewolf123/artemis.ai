from typing import Literal, Any
from os import environ


class ArtemisConfig:
    llm_provider: Literal["openrouter", "openai"]
    llm_model: str
    max_conversation_token_limit: int

    def __init__(self):
        self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
        self.llm_model = environ.get("LLM_MODEL_NAME", "x-ai/grok-4-fast")
        self.max_conversation_token_limit = environ.get(
            "MAX_CONVERSATION_TOKEN_LIMIT", 10240
        )  # 10k token limit


settings = ArtemisConfig()  # global object to prevent memory being recreated
