"""
На этой же странице, с помощью requests и bs4 найдите и обработайте раздел тегов:
https://store.steampowered.com/genre/Free%20to%20Play/
Сформируйте словарь, в котором ключами будут имена тегов,
а значениями - количество игр, относящихся к этим тегам.
Например: {‘Indie’: 2355, ... }
Обратите внимание, что теги можно найти вот по такому bs-запросу: .find_all('div', class_ = 'tag_count_button')
"""
import requests
from bs4 import BeautifulSoup

# С помощью библиотек requests и bs4 прочитайте содержимое страницы
site = BeautifulSoup((requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')).text, 'html.parser')

# Пустой словарь
narrow_by = dict()

#  В каждой строке, где есть тег "tag_count_button"
for string in site.find_all('div', class_='tag_count_button'):
    # добавляем в словарь ключ tag_name и значение tag_count tab_filter_control_count
    narrow_by[string.find(class_='tag_name').text] = string.find(class_='tag_count tab_filter_control_count').text

# Выведим словарь на экран
for item in narrow_by:
    print(item, ":", (narrow_by[item]).replace(',', ' '), 'игр(ы)')
