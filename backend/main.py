from load_dotenv import load_dotenv
import gradio as gr

from backend.agent.message_handler import handle_message
from backend.agent import build_agent
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

if __name__ == "__main__":

    thread_id = "1"  # hard coded for simplicity, replace it later!
    with SqliteSaver.from_conn_string("./db/short_memory.db") as checkpointer:
        agent = build_agent(checkpointer)

        gr.ChatInterface(
            fn=lambda prompt, _: handle_message(agent, prompt, thread_id),
            title="Artemis AI",
        ).launch()
