import os
import threading

import telebot
from flask import Flask

TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello 👋")


@app.get("/")
def home():
    return "Telegram bot is running!", 200


@app.get("/health")
def health():
    return "OK", 200


def run_bot():
    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
