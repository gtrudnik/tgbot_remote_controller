import telebot
from telebot import types
import const
from rw_config import *
from commands import *
from controller import Controller

token = ''
bot = telebot.TeleBot(token)
password = '12345678'
controller = Controller()


def is_logged(chat_id):
    chat = controller.get_chat(chat_id)
    if len(chat) == 0:
        controller.add_chat(chat_id)
    chat = controller.get_chat(chat_id)[0]
    if not chat.is_login:
        bot_message = bot.send_message(chat_id, "Введите пароль!")  # + get_commands().join("\n"))
        controller.add_message(bot_message.id, bot_message.text, chat_id)
        print("Not login")
    return chat.is_login


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


def delete_messages(msgs):
    # delete previous bot messages
    for msg in msgs:
        try:
            bot.delete_message(msg.chat_id, msg.id)
            controller.delete_message(msg.id)
        except Exception:
            print("delete error")


@bot.message_handler(commands=['start'])
def info_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    if not is_logged(message.chat.id):
        return 0
    messages = controller.get_not_menu_msgs_chat(message.chat.id)
    print(messages)
    delete_messages(messages)
    print(controller.is_exist_menu_message(message.chat.id))
    if not controller.is_exist_menu_message(message.chat.id):
        bot_message = bot.send_message(message.chat.id, const.list_com + const.default_com + const.choose,
                                       reply_markup=creat_markup())  # + get_commands().join("\n"))
        controller.add_message(bot_message.id, bot_message.text, message.chat.id, is_menu=True)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    messages = controller.get_all_msgs_chat(message.chat.id)
    delete_messages(messages)
    controller.delete_all_msg_chat(message.chat.id)
    bot_message = bot.send_message(message.chat.id, const.list_com + const.default_com + const.choose,
                                   reply_markup=creat_markup())
    controller.add_message(bot_message.id, bot_message.text, message.chat.id, is_menu=True)


@bot.message_handler(commands=['playpause'])
def play_pause(message):
    if not is_logged(message.chat.id):
        return 0
    do_action("playpause")
    info_message(message)


@bot.message_handler(commands=['next'])
def play_next(message):
    if not is_logged(message.chat.id):
        return 0
    do_action("nexttrack")
    info_message(message)


@bot.message_handler(commands=['previous'])
def play_previous(message):
    if not is_logged(message.chat.id):
        return 0
    do_action("prevtrack")
    info_message(message)


@bot.message_handler(commands=['volumeup'])
def volume_up(message):
    if not is_logged(message.chat.id):
        return 0
    for i in range(5):
        do_action("volumeup")
    info_message(message)


@bot.message_handler(commands=['volumedown'])
def volume_down(message):
    if not is_logged(message.chat.id):
        return 0
    for i in range(5):
        do_action("volumedown")
    info_message(message)


@bot.message_handler(commands=['volumemute'])
def volume_mute(message):
    if not is_logged(message.chat.id):
        return 0
    do_action("volumemute")
    info_message(message)


@bot.message_handler(commands=['battery'])
def battery_message(message):
    if not is_logged(message.chat.id):
        return 0
    x = battery_info()
    bot_message = bot.send_message(message.chat.id, "Процент заряда: " + str(x[0]) + "%")
    info_message(message)
    controller.add_message(bot_message.id, bot_message.text, message.chat.id)


@bot.message_handler(content_types=['text'])
def analyze_message(message):
    if not is_logged(message.chat.id):
        if message.text == password:
            controller.login_chat(message.chat.id)
    elif message.text == "⏪️":
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
    else:
        bot.delete_message(message.chat.id, message.message_id)


bot.infinity_polling()
