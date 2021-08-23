"""
На этой же странице найдите и обработайте таблицу игр:
Используйте функцию Inspect Element в вашем браузере, чтобы понять, какие теги и классы вам нужно обрабатывать.
Составьте и распечатайте словарь игр и их тегов.
Например, {'Incremental Epic Breakers': ['2D Platformer', ', Puzzle Platformer', ', Idler', ', Destruction'], ... }
"""

import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests и bs4 прочитайте содержимое страницы
site = BeautifulSoup((requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')).text, 'html.parser')

# Пустой словарь
games_table = dict()

#  В каждой секции тега "tab_item"
for section in site.find_all(class_='tab_item'):
    # Пустой список
    tag_list = list()
    #  В каждой секции тега "top_tag"
    for string in section.find_all(class_='top_tag'):
        # Добавляем текст из тега top_tag в список
        tag_list.append(string.text)
    # Формируем словарь: Имя игры (ключ) - список тэгов для игры (значения)
    games_table[section.find(class_='tab_item_name').text] = tag_list

# Выводим словарь на экран
for item in games_table:
    print(item, ':', games_table[item])
