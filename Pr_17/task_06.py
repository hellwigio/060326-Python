""" 06. Возраст на конкретную дату

Добавьте метод calculate_age_on(target_date: datetime), который позволяет
получить возраст студента на переданную дату.

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



# Перерасчёт даты рождения от сегодняшней даты, чтобы Алисе всегда было 19
alis_birthday = (datetime.today() - relativedelta(years=19)).date()  #2006-12-07"

s1 = Student("Alice", str(alis_birthday))

# День рождения Алисы через 25 лет
alis_birthday_plus_25 = alis_birthday + relativedelta(years=25)

print(s1.calculate_age_on(alis_birthday_plus_25))
# 25
