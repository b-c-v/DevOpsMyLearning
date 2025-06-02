#!/bin/python3
# подсчитывает количество строк в указанном текстовом файле, имя которого передаётся как аргумент командной строки.

# python3 count_lines_file.py count_lines_stdin.py # подсчитать количество строк в файле count_lines_stdin.py

import sys


def count_file_lines(file_name):
    total_lines = 0
    with open(file_name, "r") as file:  # Открываем файл в режиме чтения  Без with файл нужно закрывать вручную (file.close()), иначе возможны утечки ресурсов.
        for line in file:  # Проходим по каждой строке в файле
            total_lines += 1  # Увеличиваем счётчик на 1 для каждой строки
    return total_lines


if __name__ == "__main__":
    if (
        len(sys.argv) != 2
    ):  # Проверяем, передан ли ровно один аргумент командной строки
        print(
            "Usage: count_lines_file.py <filename>"
        )  # Выводим инструкцию по использованию скрипта
        sys.exit(1)  # Завершаем выполнение программы с кодом ошибки

    input_file = sys.argv[1]  # Получаем имя файла из аргументов командной строки
    result = count_file_lines(input_file)  # Вызываем функцию подсчёта строк
    print(f"Total lines: {result}")
