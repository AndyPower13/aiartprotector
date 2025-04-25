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
    response = requests.post(url, json=data)
    print(f"Sent message to {chat_id}: {text}", response.text)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received update:", data)

    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]

        if "text" in message:
            text = message["text"].strip().lower()

            if text == "/start":
                send_message(chat_id, "👋 Welcome to <b>AI ArtProtector</b>! Send an image or type /donate to support us.")
            elif text == "/donate":
                send_message(chat_id, f"Support us: <a href=\"{BMC_URL}\">BuyMeACoffee</a>")
            elif text == "/language":
                send_message(chat_id, "Choose your language (feature coming soon)")
            else:
                send_message(chat_id, f"You said: {text}")

        elif "photo" in message:
            send_message(chat_id, "Thanks for the photo! Image protection is being processed (feature coming soon).")

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    

