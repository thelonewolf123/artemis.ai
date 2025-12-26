from langchain.agents import create_agent
from langchain.messages import HumanMessage
from load_dotenv import load_dotenv

from tools.weather import get_weather

load_dotenv()


def main():
    agent = create_agent(
        "gpt-4.1",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    response = {"messages": []}
    while True:
        message = input("User: ")
        response["messages"].append(HumanMessage(message))

        response = agent.invoke(response)
        print("Ai: ", response["messages"][-1].content)


if __name__ == "__main__":
    main()
