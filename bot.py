from telegram.ext import (
    MessageHandler,
    CommandHandler,
    ConversationHandler,
    ContextTypes,
    Application,
    filters,
)
from telegram import Update

import os
import dotenv;dotenv.load_dotenv()

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello")

async def greeting(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello")



token = os.getenv("TOEKN")
application = Application.builder().token(token).build()

application.add_handler(CommandHandler("start",start))
application.add_handler(MessageHandler(filters.Text(["hello","hi"]),greeting))

application.run_polling()
