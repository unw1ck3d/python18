# В приложении заданы словари с названиями, рейтингами и жанрами сериалов shows и ratings. Напишите
# программу, которая состоит из двух функций:

# - Первая функция получает на вход словарь shows и название жанра. Функция должна вернуть все названия сериалов для заданного жанра;
# - Вторая функция получает на вход словарь ratings и список названий сериалов. Функция должна вернуть средний рейтинг для сериалов из входного списка.

# Создайте модуль, содержащий эти функции. Импортируйте модуль в свою программу и с помощью этих двух
# функций исследуйте средний рейтинг для жанров “драма” и “криминал”.

# импортируем функции из модуля
from module_2_program import get_show_as, get_average_rating

# Функция исследованя среднего рейтинга для жанра
def explore(genre):
    result = get_average_rating(get_show_as(genre))
    return ('{}{}{}{}'.format('Ретинг фильмов жанра ', genre.upper(), ' - ', result))

# Cредний рейтинг для жанров “драма”
print(explore('драма'))

# Cредний рейтинг для жанров “криминал”
print(explore('криминал'))
