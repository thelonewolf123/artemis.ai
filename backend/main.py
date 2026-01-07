from load_dotenv import load_dotenv

load_dotenv()

from backend.agent.message_handler import handle_message
from backend.agent import build_agent
from backend.services.telegram import Telegram
from langgraph.checkpoint.sqlite import SqliteSaver


if __name__ == "__main__":

    with SqliteSaver.from_conn_string("./db/short_memory.db") as checkpointer:
        agent = build_agent(checkpointer)
        telegram = Telegram(
            on_message=lambda prompt, thread_id: handle_message(
                agent, prompt, thread_id
            )
        )

        telegram.start()
