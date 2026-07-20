"""
02. Номер студента
Каждому студенту (объекту student) должен автоматически присваиваться уникальный номер - student_id, начиная с 1.

Этот номер должен храниться в каждом объекте класса Student.
И, разумеется, у каждого студента он должен быть свой собственный.
"""



print(Student.student_id == 0)  # True

s1 = Student("name1", "2000-01-01")
s2 = Student("name2", "2000-01-01")

print(Student.student_id == 2)  # True
print(s1.student_id == 1)
print(s2.student_id == 2)

# True
# True
# True
# True
