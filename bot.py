from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from flask import Flask, request
import os

app = Flask(__name__)
TOKEN = os.getenv("7889177275:AAGnkdUs9f6Voq3RZ8AJF9-AG3O-q0TQUPA")
updater = Updater(TOKEN, use_context=True)

def start(update, context):
    update.message.reply_text("Halo! Saya bot auto-respon!")

def auto_reply(update, context):
    user_message = update.message.text
    update.message.reply_text(f"Kamu bilang: {user_message}!")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), updater.bot)
    updater.dispatcher.process_update(update)
    return "OK"

def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))
    updater.bot.set_webhook(f"https://{os.getenv('RAILWAY_STATIC_URL')}/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

if __name__ == "__main__":
    main()
