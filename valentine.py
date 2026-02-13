from telebot import TeleBot, types

bot = TeleBot("8488578422:AAEWZlmb5wmI5xc1QOyMaQeoo2TwUVIk5Gw")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    web_app = types.WebAppInfo("https://valentine-rthw.onrender.com")

    btn = types.KeyboardButton("Open valentine", web_app=web_app)

    markup.add(btn)
    bot.send_message(message.chat.id, "Open", reply_markup=markup)

bot.infinity_polling()

