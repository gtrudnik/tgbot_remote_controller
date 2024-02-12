import telebot
from telebot import types
import const
from rw_config import *
from commands import *

token = ''
bot = telebot.TeleBot(token)


def creat_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("⏪️")
    item2 = types.KeyboardButton("⏯️")
    item3 = types.KeyboardButton("⏩️")
    item4 = types.KeyboardButton("🔊")
    item5 = types.KeyboardButton("🔉")
    item6 = types.KeyboardButton("🔇")
    markup.row(item1, item2, item3)
    markup.row(item4, item5, item6)
    return markup


def delete_messages(*messages):
    for msg in messages:
        bot.delete_message(msg.chat.id, msg.message_id)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, const.list_com + const.default_com)  # + get_commands().join("\n"))
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['playpause'])
def play_pause(message):
    do_action("playpause")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['next'])
def play_next(message):
    do_action("nexttrack")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['previous'])
def play_previous(message):
    do_action("prevtrack")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['volumeup'])
def volume_up(message):
    for i in range(5):
        do_action("volumeup")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['volumedown'])
def volume_down(message):
    for i in range(5):
        do_action("volumedown")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(commands=['volumemute'])
def volume_mute(message):
    do_action("volumemute")
    bot.send_message(message.chat.id, const.choose, reply_markup=creat_markup())


@bot.message_handler(content_types=['text'])
def analize_message(message):
    if message.text == "⏪️":
        play_previous(message)
    elif message.text == "⏯️":
        play_pause(message)
    elif message.text == "⏩️":
        play_next(message)
    elif message.text == "🔊":
        volume_up(message)
    elif message.text == "🔉":
        volume_down(message)
    elif message.text == "🔇":
        volume_mute(message)

bot.infinity_polling()
