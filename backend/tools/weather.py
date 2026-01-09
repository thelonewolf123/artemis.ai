import random
from langchain.tools import tool


@tool
def get_weather(city: str) -> int:
    """Return weather for given city in celsius"""
    return random.randint(20, 50)
