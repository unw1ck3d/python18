# В приложении к заданию находится рассказ “Кошки Ультара” Говарда Лавкрафта
# Напишите программу, которая:
# - Открывает файл и считывает данные;
# - Подсчитывает сколько раз в файле встречается слово “кошка” и выводит это число на экран;
# - Находит все строки, в которых встречается слово “кошка” и выводит эти строки на экран.

# Открываем файл на чтение
file = open('text_3_H_Lovecraft.txt', 'r')

with file as f:
    # Количество вхождений
    counts_entry = 0
    # В каждой строке файла
    for line in f.readlines():
        # Если в строке счетчик фиксирует вхождение слова
        if line.count('кошка') > 0:
            # Выводим строку
            print('Это строка в которой найдено вхождение:\n', line)
            # Учитываем вхождение в счетчике
            counts_entry = counts_entry + line.count('кошка')

# Выводим результат
print('Всего в рассказе Говарда Лавкрафта слово КОШКА встречается', counts_entry, 'раз.')