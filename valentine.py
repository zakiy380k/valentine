from fastapi import FastAPI, Request
from telebot import TeleBot, types
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles


TOKEN = "8488578422:AAEWZlmb5wmI5xc1QOyMaQeoo2TwUVIk5Gw"
WEBHOOK_URL = "https://valentine-rthw.onrender.com/webhook"

bot = TeleBot(TOKEN)
app = FastAPI()
app.mount("/photos", StaticFiles(directory="photos"), name="photos")
app.mount("/music", StaticFiles(directory="music"), name="music")


# ====== ОБРАБОТЧИК СТАРТА ======
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo("https://valentine-rthw.onrender.com")
    btn = types.KeyboardButton("Открыть", web_app=web_app)
    markup.add(btn)

    bot.send_message(message.chat.id, "Нажми кнопку", reply_markup=markup)


# ====== WEBHOOK ПРИЕМ ======
@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.body()
        update = types.Update.de_json(data.decode("utf-8"))
        bot.process_new_updates([update])
    except Exception as e:
        print("Webhook error:", e)
    return {"ok": True}


# ====== ГЛАВНАЯ СТРАНИЦА (WEB APP) ======
@app.get("/")
async def home():
    html = Path("templates/index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)


# ====== УСТАНОВКА WEBHOOK ПРИ СТАРТЕ ======
@app.on_event("startup")
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    print("Webhook set!")
