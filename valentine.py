from threading import Thread
from fastapi import FastAPI
import uvicorn
from telebot import TeleBot, types
import threading

bot = TeleBot("8488578422:AAEWZlmb5wmI5xc1QOyMaQeoo2TwUVIk5Gw")
app = FastAPI()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo("https://valentine-rthw.onrender.com")
    btn = types.KeyboardButton("Открыть", web_app=web_app)
    markup.add(btn)

    bot.send_message(message.chat.id, "Нажми кнопку", reply_markup=markup)


def run_bot():
    print("Bot started")
    bot.infinity_polling()


threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
