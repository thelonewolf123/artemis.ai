from load_dotenv import load_dotenv
import gradio as gr

from backend.agent.message_handler import handle_message
from backend.agent import get_agent

load_dotenv()

if __name__ == "__main__":

    thread_id = "1"  # hard coded for simplicity, replace it later!
    gr.ChatInterface(
        fn=lambda prompt, _: handle_message(get_agent(), prompt, thread_id),
        title="Artemis AI",
    ).launch()
