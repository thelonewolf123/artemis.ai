from load_dotenv import load_dotenv
import gradio as gr

from backend.agent.message_handler import handle_message
from backend.agent import get_agent

load_dotenv()

if __name__ == "__main__":

    gr.ChatInterface(
        fn=lambda prompt, history: handle_message(get_agent(), prompt, history),
        title="Artemis AI",
    ).launch()
