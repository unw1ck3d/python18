# -*- coding: cp1251 -*-
'''
В предыдущий пример добавьте любой другой алгоритм сортировки.
Сравните время его работы с selection_sort. Напишите выводы.
'''

# Импортируем модули
import random
import time


# Функция для генерации массива случайных целых чисел длины n
def generated_array(n):
    # Получаем массив из диапазона чисел n
    gen_array = [i for i in range(n)]
    # Перемешиваем полученный массив
    random.shuffle(gen_array)
    # Возвращаем перемешанный массив из функции
    return gen_array


# функция из приложения
def selection_sort(input_list):
    start_time = time.time()  # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time  # время выполнения в секундах


def bubble_sort(nums):
    start_time = time.time()  # время старта функции
    # Устанавливаем значение True для нашей переменной-переключателю
    swapped = True
    # Пока переключатель в значении True цикл while активен
    while swapped:
        # Сразу после начала цикла while меняем значение переключателя на False
        swapped = False
        # Для каждого элемента массива в длине диапазона представленного массива минус один элемент из диапозона массива
        for i in range(len(nums) - 1):
            # Если полученный в цикле элемент массива больше чем соседний элемент в этом же массиве
            if nums[i] > nums[i + 1]:
                # Меняем их местами в массиве
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Возвращаем переключатель в значение True для того, чтобы цикл while оставался активен
                swapped = True
        return time.time() - start_time


def default_sort(array):
    start_time = time.time()
    sorted(array)
    return time.time() - start_time

# - Печатается размер списка и время сортировки.
# Для каждого диапазона из доступных в массиве [внутри квадратных скобок]
print('Выборочная сортировка:')
for scope in [1000, 2000, 5000, 10000]:
    # Вывести на экран количество элементов обрабатываемого в цикле диапазона
    # Вывести затраченное время на сортировку выборов, округленное до двух знаком после запятой
    print(f'Сортировка {scope} элементов')
    print(f'Выборочная сортировка: {round((selection_sort(generated_array(scope))), 6)} сек.')
    print(f'Пузырьковая сортировка: {round((bubble_sort(generated_array(scope))), 6)} сек.')
    print(f'Стандартная сортировка: {round((default_sort(generated_array(scope))), 6)} сек.')
    print('')

'''
Выводы:
Выборочная сортировка занимает много времени. Время увеличивается при увеличении количества элементов массива.
Пузырькова сортировка - использование приемлемо при обработке небольшого массива
Стандартная сортировка - наименее затратна по времени, а так же более понятна по синтаксису.
'''