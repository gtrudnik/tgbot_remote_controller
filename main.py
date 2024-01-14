import telebot
from telebot import types
import const
from rw_config import *

token = 'token'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, const.list_com + get_commands().join("\n"))


@bot.message_handler(commands=['add'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)


bot.infinity_polling()
