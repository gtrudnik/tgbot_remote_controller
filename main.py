import telebot
from telebot import types
import const
from rw_config import *
from commands import *

token = 'token'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, const.list_com)  #+ get_commands().join("\n"))


@bot.message_handler(commands=['add'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)


@bot.message_handler(commands=['playpause'])
def play_pause(message):
    do_action("playpause")


@bot.message_handler(commands=['next'])
def play_next(message):
    pass


@bot.message_handler(commands=['previous'])
def play_previous(message):
    pass


@bot.message_handler(commands=['volumeup'])
def volume_up(message):
    pass


@bot.message_handler(commands=['volumedown'])
def volume_down(message):
    pass


@bot.message_handler(commands=['volumemute'])
def volume_mute(message):
    do_action("volumemute")


bot.infinity_polling()
