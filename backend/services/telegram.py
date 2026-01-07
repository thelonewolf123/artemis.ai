from typing import Callable, Optional
from backend.config import settings

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    Application,
    MessageHandler,
)


class Telegram:
    app: Application
    handle_message: Callable[[str, int], str]

    def __init__(
        self,
        on_message: Optional[Callable[[str, int], str]] = None,
    ):
        self.app = ApplicationBuilder().token(settings.telegram_api_key).build()
        self.app.add_handler(CommandHandler("start", self.hello))
        if on_message != None:
            self.handle_message = on_message
            self.app.add_handler(MessageHandler(None, self.message_handler, True))

    async def hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f"Hello {update.effective_user.first_name}")

    async def message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        thread_id = update.effective_chat.id
        user_text = update.message.text
        ai_response = self.handle_message(user_text, thread_id)
        await update.message.reply_text(ai_response)

    def start(self):
        print("Telegram ai bot is running!")
        self.app.run_polling()
