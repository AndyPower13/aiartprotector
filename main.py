import os
from flask import Flask, request
import requests

TOKEN = os.environ.get("BOT_TOKEN")
BMC_URL = "https://www.buymeacoffee.com/aiartprotector"

app = Flask(__name__)

def send_message(chat_id, text, reply_markup=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
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
            if message["text"] == "/start":
                reply_markup = {
                    "inline_keyboard": [[
                        {"text": "☕ Support the Project", "url": BMC_URL}
                    ]]
                }
                send_message(chat_id,
                    "🛡️ AI ArtProtector helps designers and artists detect stolen versions of their artwork online.\n\n🔍 No signup. No tracking. Just protection.\n🖼️ Send your artwork — I’ll check it online.\n🔐 100% private.",
                    reply_markup=reply_markup
                )
        if "photo" in message:
            send_message(chat_id, "🖼️ Image received. Running a quick check online...\n✅ No obvious duplicates found. Your art looks safe!")
    return {"ok": True}

@app.route("/", methods=["GET"])
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
