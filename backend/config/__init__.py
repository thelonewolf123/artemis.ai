from typing import Literal
from os import environ


class ArtemisConfig:
    llm_provider: Literal["openrouter", "openai"]
    llm_model: str
    max_conversation_token_limit: int
    telegram_api_key: str
    embedding_model: str

    conv_buffer_db_path: str
    vector_db_path: str

    def __init__(self):
        self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
        self.llm_model = environ.get("LLM_MODEL_NAME", "x-ai/grok-4-fast")
        self.max_conversation_token_limit = environ.get(
            "MAX_CONVERSATION_TOKEN_LIMIT", 10240
        )  # 10k token limit

        self.telegram_api_key = environ.get("TELEGRAM_API_KEY")
        self.embedding_model = environ.get(
            "OPENROUTER_EMBED_MODEL",
            "text-embedding-3-small",
        )

        self.conv_buffer_db_path = "./db/short_memory.db"
        self.vector_db_path = "./db/vector_memory.db"


settings = ArtemisConfig()  # global object to prevent memory being recreated
