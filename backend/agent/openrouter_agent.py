from langchain_openai import ChatOpenAI

import os


def get_openrouter_llm(model: str = "x-ai/grok-4-fast"):
    return ChatOpenAI(
        model=model,
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1/",
    )
