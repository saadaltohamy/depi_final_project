import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
import asyncio
from test import send_post_request

# Replace this with your bot token
TELEGRAM_API_TOKEN = "7757640919:AAHBDM3km1BEbY8F6iL4bNLURdnDfjIfP8Q"

async def start(update: Update, context) -> None:
    await update.message.reply_text("Welcome! Please send me a paragraph to summarize.")

async def summarize(update: Update, context) -> None:
    user_input = update.message.text
    if user_input:
        # Make a request to the FastAPI summarization endpoint
            summary = send_post_request(user_input).json().get("summary")
            await update.message.reply_text(f"Summary: {summary}")
    else:
        await update.message.reply_text("Please send a paragraph for summarization.")

def main() -> None:
    # Set up the Telegram bot application
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, summarize))

    # Start the bot and run polling
    application.run_polling()

# Check if there's an event loop already running (e.g., in Jupyter or Replit)
try:
    asyncio.get_running_loop()
except RuntimeError:  # No loop is running
    main()
else:  # If loop is running (Jupyter/Colab), run main without blocking the loop
    asyncio.create_task(main())
