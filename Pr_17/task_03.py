""" 03 Добавьте строковое представление объекта.

Пример вывода:
Student: Alice, birth_date: 2005-05-10, ID: 1
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

class Student:
    MIN_AGE = 16

    student_id_seq = 0

    def __init__(self, name, birth_date):
        Student.student_id_seq += 1

        self.student_id = Student.student_id_seq

        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        if self.get_age() < Student.MIN_AGE:
            raise ValueError("Student must be at least 16 years old.")


    def get_age(self):
        return relativedelta(datetime.now(), self.birth_date).years

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

s1 = Student("Alice", "2005-05-10")

print(s1)
print(str(s1) == "Student: Alice, birth_date: 2005-05-10, ID: 1")

# "Student: Alice, birth_date: 2005-05-10, ID: 1")
# True
