import telebot
from telebot import types
import const
from rw_config import *
from commands import *

token = ''
bot = telebot.TeleBot(token)
messages = dict()


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


def delete_messages(msg, msgs):
    # delete user message
    bot.delete_message(msg.chat.id, msg.message_id)
    # delete previous bot messages
    if msg.chat.id in msgs.keys():
        for msg in msgs[msg.chat.id]:
            try:
                bot.delete_message(msg.chat.id, msg.message_id)
            except:
                print("delete error")
        msgs[msg.chat.id] = []


@bot.message_handler(commands=['start', 'help'])
def info_message(message):
    bot_message = bot.send_message(message.chat.id, const.list_com + const.default_com + const.choose,
                                   reply_markup=creat_markup())  # + get_commands().join("\n"))
    delete_messages(message, messages)
    if bot_message.chat.id in messages.keys():
        messages[bot_message.chat.id].append(bot_message)
    else:
        messages[bot_message.chat.id] = [bot_message]


@bot.message_handler(commands=['playpause'])
def play_pause(message):
    do_action("playpause")
    info_message(message)


@bot.message_handler(commands=['next'])
def play_next(message):
    do_action("nexttrack")
    info_message(message)


@bot.message_handler(commands=['previous'])
def play_previous(message):
    do_action("prevtrack")
    info_message(message)


@bot.message_handler(commands=['volumeup'])
def volume_up(message):
    for i in range(5):
        do_action("volumeup")
    info_message(message)


@bot.message_handler(commands=['volumedown'])
def volume_down(message):
    for i in range(5):
        do_action("volumedown")
    info_message(message)


@bot.message_handler(commands=['volumemute'])
def volume_mute(message):
    do_action("volumemute")
    info_message(message)


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
