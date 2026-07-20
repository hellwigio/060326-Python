""" 05. Альтернативный конструктор

Реализуйте метод from_string(), позволяющий создавать объект из строки формата:
"Bob, 2001-12-03"

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

    def show_info(self):
        print(f"Student:")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.get_age()}")
        print(f"\tID: {self.student_id}")

    @classmethod
    def from_string(cls, string):
        name, birth_date = string.split(", ")

        return cls(name, birth_date)



s1 = Student.from_string("Bob, 2001-12-03")
print(s1)

# Student: Bob, birth_date: 2001-12-03, ID: 1


