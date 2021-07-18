# Виртуальное казино
import random  # Добавляем модуль random

# Статичные данные
balance = 10000  # Задаём размер депозита
quote_credit = 1000  # Задаём значение шага в 1000 кредитов
request_text = 'Пожалуйста, выбирете любое ЦЕЛОЕ число от 2 до 12: '  # Текст запроса
log = []  # Пустой спсок/массив

# Запрос на ввод имени игрока
username = input("Привет, игрок!\nПожалуйста, сообщи своё имя: ")

# Приветствие
print('Добро пожаловать в наше Казино,', username, end='!\n')
print('')

# Выводим сообщение
print('Вам предоставлен депозит на', balance, 'кредитов', end='!\n')
print('')

# Ввыполняем до тех пор, пока баланс игрока больше 0
while balance > 0:
    # Выводим сообщение о начале игры
    print('Баланс вашего счёт', username, 'составляет =', balance)
    print('')
    print('Бросаем кубики!')
    print('')

    # Получаем случайное число в промежутке 12
    value = random.randint(2, 12)

    # Запрос нв ввод значения от игрока
    while True:
        try:
            user_value = int(input(request_text))
            if user_value < 2 or user_value > 12:
                raise ValueError
            break
        # Если полученный ввод не число, будет вызвано исключение
        except ValueError:
            print("Ошибка! Вы ввели недопустимое значение! Внимательно прочтите условие приглашения а ввод данных.")
        else:
            print('Значение принято.')
            break

    # Если предположение игрока верно и укладывается в диапозон значений
    if (2 <= user_value <= 12) and (user_value == value):
        balance = balance + quote_credit
        print('Бинго,', username, 'Вы угадали!\nВам начислено ', quote_credit, end='кредитов!\n')
        print('Ваше значение = ', user_value, '\nВыпавшее значение =', value)
        print('Баланс Вашего счёта', balance)

    # Если предположение игрока неверно
    else:
        balance = balance - quote_credit
        print('Вы не угадали,', username, '\n', 'С Вашего счёта списано ', quote_credit, '.\n')
        print('Ваше значение = ', user_value, '\nВыпавшее значение =', value)
        print('Баланс Вашего счёта', balance)

    print('')  # Пустая строка

    # Вносим запись в массив/спмсок
    log.append(['Игра загадала: ' + str(value) + ';' +'Моя попытка: ' + str(user_value) + ';' +'На счету: '+ str(balance)])
    # log.append(['Игра загадала: ', str(value), 'Моя попытка: ', str(user_value), 'На счету: ', str(balance)])

if balance == 0:
    print('Ваш баланс равен 0. Продолжение возможно после пополнения баланса.')
    log.append(['Ваш баланс равен 0. Продолжение возможно после пополнения баланса.'])
    for item in log:
        print(item)
