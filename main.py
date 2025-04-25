
import os
from flask import Flask, request
import requests

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = f"https://aiartprotector.onrender.com/{TOKEN}"
BMC_URL = "https://www.buymeacoffee.com/aiartprotector"

app = Flask(__name__)

def send_message(chat_id, text, reply_markup=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(url, json=data)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        if "text" in message:
            text = message["text"]
            if text == "/start":
                send_message(chat_id, "👋 Welcome to AI ArtProtector!")
            elif text == "/donate":
                send_message(chat_id, f"Support us: {BMC_URL}")
            else:
                send_message(chat_id, "I received your message!")
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
