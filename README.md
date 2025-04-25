# AI ArtProtector Bot (Telegram) — Render Deployment

## 🚀 Як розгорнути бота на Render.com

1. Увійди або зареєструйся на [https://render.com](https://render.com)
2. Створи новий **Web Service**
3. Завантаж цей архів як код
4. У вкладці Environment:
   - Додай нову змінну:
     - `BOT_TOKEN` → встав сюди свій Telegram токен

5. Вибери:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

6. Натисни **Deploy**

## 🧠 Готово!
Твій бот почне працювати одразу після запуску.
