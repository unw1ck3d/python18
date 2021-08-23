"""
С помощью библиотек requests и bs4 прочитайте содержимое страницы бесплатных игр на сайте Steam
(https://store.steampowered.com/genre/Free%20to%20Play/)
Получите все ссылки (тег <a href = ‘...’>), для каждой ссылки получите текст ссылки и url.
Сформируйте словарь, состоящий только из тех ссылок, у которых в тексте встречается фраза “Free To Play”.
Выведите словарь на экран.
"""


import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests и bs4 прочитайте содержимое страницы бесплатных игр на сайте Steam
site = BeautifulSoup((requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')).text, 'html.parser')

# Пустой словарь
free2play = dict()

# В каждой строке, где есть тег "а"
for string in site.find_all('a'):
    # если есть словосочетание Free To Play
    if 'Free To Play' in string.text:
        # добавляем в словарь
        free2play[string.find(class_='tab_item_name').text] = string.get('href')

# Выведите словарь на экран
for keys,values in free2play.items():
    print(keys)
    print(values)
