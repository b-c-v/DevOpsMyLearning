#!/bin/python3
# считает количество строк, переданных через STDIN стандартный ввод (например, при перенаправлении файла или вводе в консоли).

# python3 count_lines_stdin.py < count_lines.py - посчитает количество строк в файле count_lines_stdin.py
# echo -e "Line1\nLine2\nLine3" | python3 count_lines_stdin.py 

import sys  # Импортируем модуль sys для работы с системными потоками, такими как stdin (ввод)


def count_stdin_lines():
    total_lines = 0  # Инициализируем счётчик строк
    for (
        line
    ) in sys.stdin:  # Проходим по каждой строке, полученной из стандартного ввода
        total_lines += 1  # Увеличиваем счётчик на 1 для каждой строки
    return total_lines  # Возвращаем общее количество строк


if (
    __name__ == "__main__"
):  # Проверяем, что скрипт запущен как основная программа (а не импортирован как модуль)
    result = count_stdin_lines()  # Вызываем функцию подсчёта строк и сохраняем результат
    print(
        f"Total lines: {result}"
    )  # Выводим общее количество строк в формате "Total lines: <число>"
