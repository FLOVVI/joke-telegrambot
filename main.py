import sqlite3

import telebot

from config import token
from database import Database
from joke import Joke

bot = telebot.TeleBot(token)
print("Active")


class Value:
    joke = Joke()
    database = Database()
p = Value


@bot.message_handler(commands=["start"])
def start(message):
    p.database.search(message.from_user.id)
    bot.send_message(message.chat.id, "Пришел вас веселить, встречайте Анекдот бота\n"
                                      "Напиши /give")


@bot.message_handler(commands=["newday"])
def newday(message):
    p.joke = Joke()
    bot.send_message(message.chat.id, f"Обновился\n"
                                      f"Найдено анекдотов: {p.joke.number_of_jokes}")
    p.database.all_reset()


@bot.message_handler(commands=["give"])
def give(message):
    data = p.database.get_user_page(message.from_user.id)
    if not data['newday']:
        bot.send_message(message.chat.id, "Новый день - Новые шутки!")
    try:
        bot.send_message(message.chat.id, f"Анекдот №{data['page']}\n\n{p.joke.jokes[data['page']].strip()} Классов")
    except IndexError:
        bot.send_message(message.from_user.id, "Шутки закончились!\nНачинаем заново!")
        p.database.user_reset(message.from_user.id)

bot.polling(none_stop=True, interval=0)