import os
from langchain_openai import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings(
    model=os.environ.get(
        "OPENROUTER_EMBED_MODEL",
        "text-embedding-3-small",
    ),
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1/",
)
