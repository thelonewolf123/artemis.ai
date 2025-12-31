from typing import Literal
from os import environ


class ArtemisConfig:
    llm_provider: Literal["openrouter", "openai"]

    def __init__(self):
        self.llm_provider = environ.get("LLM_PROVIDER", "openrouter")
