import arithmetic  # Импортируем модуль, в котором должны быть реализованы арифметические функции
import unittest  # Импортируем встроенный модуль для тестирования


# Класс с тестами должен наследовать unittest.TestCase
# Название класса желательно писать с заглавной буквы
class TestArithmetic(unittest.TestCase):

    # Тест на функцию сложения
    def test_add_numbers(self):
        result = arithmetic.add_number(10, 15)  # вызываем функцию из arithmetic
        self.assertEqual(result, 25)  # проверяем, равен ли результат 25

    # Тест на функцию вычитания
    def test_sub_number(self):
        result = arithmetic.sub_number(15, 10)
        self.assertEqual(result, 5)

    # Тест на функцию умножения
    def test_mul_number(self):
        result = arithmetic.mul_number(15, 10)
        self.assertEqual(result, 150)

    # Тест на функцию деления
    def test_div_number(self):  # исправлено: теперь имя начинается с test_
        result = arithmetic.div_number(15, 10)
        self.assertEqual(result, 1.5)


# Это стандартная конструкция, чтобы запускать тесты, только если файл запускается напрямую.
if __name__ == "__main__":
    # Запуск всех методов test_* из класса test (через unittest)
    unittest.main()
