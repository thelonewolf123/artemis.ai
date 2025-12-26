from load_dotenv import load_dotenv
import gradio as gr

from agent.openai_agent import handle_message

load_dotenv()

if __name__ == "__main__":
    gr.ChatInterface(
        fn=handle_message,
    ).launch()
