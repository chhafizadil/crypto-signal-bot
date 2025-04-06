import os
from dotenv import load_dotenv
from utils.signal_formatter import format_signal
from utils.market_analysis import analyze_market
import telepot
import schedule
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Load environment variables
load_dotenv("config.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

# Health Check - Dummy HTTP Server (Listening on port 8000)
class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':  # Respond to /ping path
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Healthy')  # Respond with a healthy message

def run_health_check_server():
    httpd = HTTPServer(('0.0.0.0', 8000), PingHandler)  # Listening on port 8000
    httpd.serve_forever()

# Market analysis and bot signal sending
def send_signal():
    signal_data = analyze_market()
    if signal_data:
        message = format_signal(signal_data)
        bot.sendMessage(TELEGRAM_CHAT_ID, message)

# Run health check server in a separate thread
threading.Thread(target=run_health_check_server, daemon=True).start()

# Schedule the task to send signals every 10 minutes
schedule.every(10).minutes.do(send_signal)

# Run the bot
while True:
    schedule.run_pending()
    time.sleep(1)
