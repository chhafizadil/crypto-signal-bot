import os
from dotenv import load_dotenv
from utils.signal_formatter import format_signal
from utils.market_analysis import analyze_market
import telepot
import schedule
import time

load_dotenv("config.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

def send_signal():
    signal_data = analyze_market()
    if signal_data:
        message = format_signal(signal_data)
        bot.sendMessage(TELEGRAM_CHAT_ID, message)

schedule.every(10).minutes.do(send_signal)

while True:
    schedule.run_pending()
    time.sleep(1)
