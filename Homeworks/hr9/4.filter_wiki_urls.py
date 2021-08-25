'''
С помощью re и BeautifulSoup исследуйте страницу Википедии, посвященную премии “Небьюла”
(https://ru.wikipedia.org/wiki/Небьюла).
Соберите все ссылки на этой странице.
Отфильтруйте только те, что не ведут на страницы Википедии.
'''

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

# Открываем ссылку
page = urlopen('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0')

# Создается объект BeautifulSoup. Данные передаются конструктору.
bs = BeautifulSoup(page, 'html.parser')

# Находим и фиксируем в переменной контент div
content = bs.find('div', id='content')

# Находим все url'ы
links = content.find_all('a', href=re.compile(r'^http'))

# Находим wiki url'ы
wiki_links = content.find_all('a', href=re.compile(r'^https.*wiki'))

# Пересечением множеств удаляем все url на wiki
non_wiki_links = set(links).difference(set(wiki_links))

# Для каждого элемента списка
for item in non_wiki_links:
    # Получаем текст ссылки и url
    print(item.text, '\n', item.get('href'))
