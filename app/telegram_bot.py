import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Replace this with your bot token
TELEGRAM_API_TOKEN = os.getenv("API_KEY")

# FastAPI URL for summarization
API_URL = 'http://localhost:8000/summarize'  # Replace with your Docker container's FastAPI URL

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Please send me a paragraph to summarize.")

def summarize(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    if user_input:
        # Make a request to the FastAPI summarization endpoint
        response = requests.post(API_URL, json={"paragraph": user_input})
        if response.status_code == 200:
            summary = response.json().get("summary")
            update.message.reply_text(f"Summary: {summary}")
        else:
            update.message.reply_text("Sorry, something went wrong.")
    else:
        update.message.reply_text("Please send a paragraph for summarization.")

def main() -> None:
    # Set up the Telegram bot
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, summarize))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
