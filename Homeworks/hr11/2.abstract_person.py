"""
Создайте класс-наследник Person, который будет хранить данные абстрактного студента.
Назовите его Student.
У класса Student должны быть все параметры класса Person, плюс два дополнительных параметра:
- Номер группы
- Список оценок по тестам
Также у класса Student должен быть дополнительный метод set_test_score,
получающий на вход оценку по тесту и добавляющий ее в список оценок студента.
Переопределите метод __str__ таким образом, чтобы информация о студенте выводилась в формате
“Студент: Иван Иванов, группа ГР-01, оценки [5, 0]”
Создайте несколько объектов класса Student, распечатайте их параметры с помощью print.
"""

# Импортируем модуль
import random

# Базовый класс Person, хранящий данные о каком-нибудь человеке.
class Person:
    """Класс содержит базовые данные о каком-нибудь человеке."""

    # Метод инициализации (__init__)
    def __init__(self, surname, name):
        # У класса должно быть два параметра
        self.surname = surname  # параметр Фамилия
        self.name = name  # параметр Имя

    # Специальный метод (__str__) отвечает за строковое представления объекта (__init__)
    def __str__(self):
        # Определите метод __str__ таким образом, чтобы при печати объекта выводились имя и фамилия.
        # Т.е. возвращаем сначала значение объекта Имя, затем объекта Фамилия
        return self.name, self.surname


# Создаем класс-наследник Person, который будет хранить данные абстрактного студента.
class Student(Person):
    """Класс содержит базовые данные о каком-нибудь человеке-студенте."""

    # Метод инициализации (__init__). Определяем для класса Student все параметры класса
    def __init__(self, surname, name, group_no):
        # Указываем подклассу Student часть параметров со ссылкой на на параметры базового класса Person
        super().__init__(surname, name)

        # Плюс два дополнительных параметра:
        # 1. Параметр номер группы
        self.group_no = group_no

        # 2. Параметр список оценок
        self.score = []

    # Также, у класса Student должен быть дополнительный метод set_test_score,
    # получающий на вход оценку по тесту и добавляющий ее в список оценок студента.
    def set_test_score(self, score):
        self.score.append(score)

    # Переопределите метод __str__ таким образом, чтобы информация о студенте выводилась в формате
    # “Студент: Иван Иванов, группа ГР-01, оценки [5, 0]”
    def __str__(self):
        # Определите метод __str__ таким образом, чтобы при печати объекта выводились имя и фамилия.
        # Т.е. возвращаем значения в нужном нам порядке
        return f"Студент: {self.name} {self.surname}, группа ГР-{self.group_no}, оценки {self.score}"


#  Создайте два объекта класса Student + генерируемый номер группы
student1 = Student('Пирожков', 'Толя', random.randint(1, 10))
student2 = Student('Рыжиков', 'Володя', random.randint(1, 10))

# Генерируем список оценок
for i in range(10):
    student1.set_test_score(random.randint(3, 5))
    student2.set_test_score(random.randint(3, 5))

# Выводим результат
print(student1.__str__())
print(student2.__str__())

