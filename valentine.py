from threading import Thread
from fastapi import FastAPI
import uvicorn
from telebot import TeleBot

bot = TeleBot("8488578422:AAEWZlmb5wmI5xc1QOyMaQeoo2TwUVIk5Gw")
app = FastAPI()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает")

def run_bot():
    bot.infinity_polling()

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=10000)

Thread(target=run_bot).start()
run_api()
