"""
02. Номер студента
Каждому студенту (объекту student) должен автоматически присваиваться уникальный номер - student_id, начиная с 1.

Этот номер должен храниться в каждом объекте класса Student.
И, разумеется, у каждого студента он должен быть свой собственный.
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
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

        if self.get_age() < Student.MIN_AGE:
            raise ValueError("Student must be at least 16 years old.")


    def get_age(self):
        return relativedelta(datetime.now(), self.birth_date).years

print(Student.student_id_seq == 0)  # True

s1 = Student("name1", "2000-01-01")
s2 = Student("name2", "2000-01-01")

print(Student.student_id_seq == 2)  # True
print(s1.student_id == 1)
print(s2.student_id == 2)

# True
# True
# True
# True
