import telebot
from flask import Flask
import threading
import os

# توکن از تنظیمات سرور خوانده می‌شود
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من بیدار شدم و ۲۴ ساعته آماده به کارم!")

# --- کدهای مینی‌سایت برای جلوگیری از خوابیدن ربات ---
app = Flask(__name__)
@app.route('/')
def index():
    return "Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()
bot.infinity_polling()
