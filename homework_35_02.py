""" 02. Проверка данных пользователя

Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.
"""


class User:
    pass


try:
    user1 = User("alice", "pass123")
    print(user1)  # User(username='alice')
except ValueError as e:
    print("Error:", e)

try:
    user2 = User("", "12345")  # Некорректное имя
except ValueError as e:
    print("Error:", e)

try:
    user3 = User("bob", "123")  # Слишком короткий пароль
except ValueError as e:
    print("Error:", e)

print(f"Total users: {User.get_total()}")
# Должно быть 1, только валидные пользователи считаются


# User(username='alice')
# Error: Username must be a non-empty string.
# Error: Password must be a string with at least 5 characters.
# Total users: 1