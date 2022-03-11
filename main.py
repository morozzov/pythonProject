import telebot
from telebot import types

bot = telebot.TeleBot("5130068690:AAFOtDL61iI6UnUuNYLpF65FBJ7RHfbM5fM")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Number")
    item2 = types.KeyboardButton("Text")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, "Click: \nNumber \nText", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Number":
        answer = 123
    elif message.text.strip() == "Text":
        answer = "qwer"
    bot.send_message(message.chat.id, answer)


print("start")
bot.polling(none_stop=True, interval=0)