import keyboard
import pyautogui
import psutil
import os


def cmd_command(command):
    os.system(command)


def click_key(btn):
    keyboard.send(btn)


def do_action(action):
    pyautogui.press(action)


def battery_info():
    return psutil.sensors_battery()

# 'volumedown', 'volumemute', 'volumeup', "playpause", 'prevtrack', 'nexttrack'
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
