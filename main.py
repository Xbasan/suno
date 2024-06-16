import telebot
from telebot import types
from telebot.types import InputFile



bot = telebot.TeleBot('5473853379:AAGy2mEkaKNlLmOS2r4kIZxbVVxhC-LxnQQ')

   

if __name__ == '__main__':
    bot.polling(non_stop=True, interval=0)
