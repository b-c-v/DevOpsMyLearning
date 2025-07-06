# assert проверяет булевое условие. Если условие истинно (True) — программа продолжает работу.
# Если ложно (False) — выбрасывается AssertionError, и можно указать сообщение об ошибке.
"""
assert условие, "Сообщение об ошибке (необязательно)"
"""


# Проверка входных данных
def set_age(age):
    assert age >= 0, "Возраст не может быть отрицательным"
    print(f"Возраст установлен: {age}")


# set_age(-5)  # AssertionError: Возраст не может быть отрицательным


# Проверка длины списка
def check_length(any_list):
    assert len(any_list) == 3, "Данные должны содержать ровно 3 элемента"


sequence = [1, 2, 3, 4]
# check_length(sequence)  # AssertionError: Данные должны содержать ровно 3 элемента


# Проверка типа данных
def check_type(data):
    assert isinstance(name, str), "Ожидалась строка"


name = 123
# check_type(name) # AssertionError: Ожидалась строка


# Использование внутри функций
def divide(a, b):
    assert b != 0, "Деление на ноль невозможно"
    return a / b


print(divide(10, 2))  # OK
# print(divide(5, 0))  # AssertionError: Деление на ноль невозможно


# Проверка на непустой список
def check_items(items):
    assert items, "Список не должен быть пустым"


my_items = []
check_items(my_items)  # AssertionError: Список не должен быть пустым
