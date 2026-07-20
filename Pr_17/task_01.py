""" 01. Класс Student

Создайте класс Student, представляющий студента.
У каждого объекта должно быть
- имя
- и дата рождения.
Дата передаётся как строка (YYYY-MM-DD) и сохраняется в виде объекта datetime.date.

Добавьте метод определения возраста get_age()
  - студенту должно быть
  - если студенту менее 16 лет, то при попытке создать объект студента с некорректной датой рождения
    должно выбрасываться исключение ValueError с текстом:
        "Student must be at least 16 years old."
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

class Student:
    pass

    def get_age(self):
        pass

# Проверка
try:
    s1 = Student("Alice", "2020-05-10")  # ошибка
except ValueError as e:
    print(e)

s2 = Student("Alice", "2005-05-10")
print("Успешно:", s2.name, s2.birth_date)

# Student must be at least 16 years old.
# Успешно: Alice 2005-05-10
