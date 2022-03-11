import telebot
from telebot import types

bot = telebot.TeleBot("5130068690:AAFOtDL61iI6UnUuNYLpF65FBJ7RHfbM5fM")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("fact")
    item2 = types.KeyboardButton("not fact")
    markup.add(item1)
    markup.add(item2)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'fact' :
            answer = "Fact"
    elif message.text.strip() == 'not fact':
            answer = "not fact"
    bot.send_message(message.chat.id, answer)

print(start)
bot.polling(none_stop=True, interval=0)