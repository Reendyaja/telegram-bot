from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Ambil token dari variabel lingkungan untuk keamanan
TOKEN = os.getenv("7889177275:AAGnkdUs9f6Voq3RZ8AJF9-AG3O-q0TQUPA")

def start(update, context):
    update.message.reply_text("Halo! Saya bot auto-respon, aktif 24/7!")

def auto_reply(update, context):
    user_message = update.message.text
    update.message.reply_text(f"Kamu bilang: {user_message}. Saya balas otomatis!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
