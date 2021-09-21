# Import libraries
import requests  # Библиотека HTTP для людей
import telebot  # Библиотеки для телеграм бота
import config  # Конфиг бота
import random  # Модуль случайной генерации

from bs4 import BeautifulSoup
from telebot import types

# Create bot
bot = telebot.TeleBot(config.TOKEN)

# Welcome message
@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("🎲 Случайная Free To Play игра в Steam")

    markup.add(item)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>!\n"
                     "Нажми на кнопку ниже, и получишь ссылку на случайную бесплатную игру в Steam.\n"
                     "Давай, попробуй!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_random_f2p_game(message):
    if message.chat.type == 'private':
        if message.text == "🎲 Случайная Free To Play игра в Steam":

            # С помощью библиотек requests и bs4 прочитайте содержимое страницы бесплатных игр на сайте Steam
            site = BeautifulSoup((requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')).text,
                                 'html.parser')

            # Пустой словарь
            free2play = dict()

            # В каждой строке, где есть тег "а"
            for string in site.find_all('a'):
                # если есть словосочетание Free To Play
                if 'Free To Play' in string.text:
                    # добавляем в словарь
                    free2play[string.find(class_='tab_item_name').text] = string.get('href')

            info = random.choice(list(free2play.values()))

            bot.send_message(message.chat.id, info)


# RUN
bot.polling(none_stop=True)
