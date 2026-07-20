""" 07. Фильтрация студентов по возрасту

Реализуйте метод
filter_by_min_age(students: list[Student], min_age: int),
как способ отобрать из списка студентов только тех, кто старше определённого возраста.

"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pprint import pprint

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

    def calculate_age_on(self, target_date):
        return relativedelta(target_date, self.birth_date).years

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def __repr__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, age: {self.get_age()}, ID: {self.student_id}"

    def show_info(self):
        print(f"Student:")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.get_age()}")
        print(f"\tID: {self.student_id}")

    @classmethod
    def from_string(cls, string):
        name, birth_date = string.split(", ")

        return cls(name, birth_date)

    @classmethod
    def filter_by_min_age(cls, students, min_age):
        return [student for student in students if student.get_age() >= min_age]


s1 = Student("Alice", "2005-05-10")
s2 = Student.from_string("Bob, 2001-12-03")
s3 = Student.from_string("Bill, 2009-05-15")
students = [s1, s2, s3]

pprint(Student.filter_by_min_age(students, 20))
#
# [Student: Alice, birth_date: 2005-05-10, ID: 1,
#  Student: Bob, birth_date: 2001-12-03, ID: 2]
