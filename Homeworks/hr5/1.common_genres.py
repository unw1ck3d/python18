# В приложении заданы 4 словаря с названиями и жанрами сериалов, которые нравятся Ане, Оле, Насте и Свете.
# Напишите функцию, которая получает на вход два словаря и возвращает пересечение жанров.
# Например, Ане и Свете обеим нравятся фантастика и драма.
# С помощью функции найдите общие жанры для:
# - Ани и Насти
# - Оли и Светы
# - Светы и Ани
anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

# Определяем функцию для словаря1 и словаря2
def cross(slv1, slv2):
    # Создаем пустой список
    cross_list = []
    # Если значение словаря1 совпадает со значением словаря2, записываем значение словаря1 в список
    for k1, v1 in slv1.items():
        for k2, v2 in slv2.items():
            if v1 == v2:
               cross_list.append(v1)
    # Преобразуем список в множетсво - чтобы убрать повторяющиеся значения
    # Если длина множества меньше равна нулю, значит пересечений нет
    if len(set(cross_list)) == 0:
        result = 'нет общих любимых жанров'
    # Если длина множества равна 1, выводим текст в единственно числе
    elif len(set(cross_list)) == 1:
        # Использовал replace чтобы убрать символы {} и '
        # Уверен есть более изящный способ, пока не удалось найти
        result = 'любимый жанр: '+((str(set(cross_list))).replace('{','').replace('}','')).replace("'","")
    # Если длина множества больше 1, выводим текст во множественном числе
    elif len(set(cross_list)) > 1:
        # Использовал replace чтобы убрать символы {} и '
        # Уверен есть более изящный способ, пока не удалось найти
        result = 'любимые жанры: '+((str(set(cross_list))).replace('{','').replace('}','')).replace("'","")
    # Возвращаем результат работы функции
    return result

# Выводим результаты
print('У Ани и Насти', cross(anya, nastya))
print('У Оли и Светы', cross(olya, sveta))
print('У Светы и Аня', cross(sveta, anya))
