from backend.config import ArtemisConfig
from .openai_agent import get_openai_agent
from .openrouter_agent import get_openrouter_agent
from backend.tools.weather import get_weather


def get_agent():
    config = ArtemisConfig()
    tools = [get_weather]
    if config.llm_provider == "openai":
        return get_openai_agent(tools)
    return get_openrouter_agent(tools)
