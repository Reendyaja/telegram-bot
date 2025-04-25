import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("7889177275:AAGnkdUs9f6Voq3RZ8AJF9-AG3O-q0TQUPA")

async def start(update: Update, context):
    logger.info("Received /start command")
    await update.message.reply_text("Halo! Saya bot auto-respon, aktif 24/7!")

async def auto_reply(update: Update, context):
    user_message = update.message.text
    logger.info(f"Received message: {user_message}")
    await update.message.reply_text(f"Kamu bilang: {user_message}. Saya balas otomatis!")

def main():
    logger.info("Starting bot...")
    # Gunakan Application alih-alih Updater
    app = Application.builder().token(TOKEN).build()

    # Tambahkan handler
    app.add_handler(CommandHandler("start", start))
    # Gunakan filters alih-alih Filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    logger.info("Bot started polling")
    app.run_polling()

if __name__ == "__main__":
    main()
