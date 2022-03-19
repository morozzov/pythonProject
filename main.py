import datetime
import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests as req

access_key = "AsccesKey"
bot = telebot.TeleBot(access_key)

def parse_quote():
    resp = req.get("http://bashorg.org/random")
    soup = BeautifulSoup(resp.text, 'lxml')
    soup = soup.find("div", class_="quote").getText(separator="\n")
    return soup

def parse_joke():
    resp = req.get("https://baneks.ru/random")
    soup = BeautifulSoup(resp.text, 'lxml')
    soup = soup.find("p").getText(separator="\n")
    return soup

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Quote")
    markup.add(item1)
    item2 = types.KeyboardButton("Joke")
    markup.add(item2)
    bot.send_message(m.chat.id, "Click: \nQuote to show random quote\nJoke to show random joke", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Quote":
        answer = parse_quote()
    elif message.text.strip() == "Joke":
        answer = parse_joke()
    elif message.text.strip() == "Log":
        if(message.from_user.username == "moroz_zov"):
            answer = "Log file"
            doc = open('log.txt', 'rb')
            bot.send_document(message.chat.id, doc)
        else:
            answer = "Access is denied"
    else:
        answer = "ERROR"
    f = open('log.txt', 'a')
    msg = str(message.text.strip())
    user_name = str(message.from_user.username)
    if (user_name == "None"):
        user_name = "user(" + str(message.chat.id) + ")"
    log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ' -- ', user_name, ': \"', msg, '\"\n'
    # print(datetime.datetime.now(), end=": ")
    # print(message.text.strip())
    print(log)
    f.writelines(log)
    bot.send_message(message.chat.id, answer)

print("start")
bot.polling(none_stop=True, interval=0)