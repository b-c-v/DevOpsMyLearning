#! /bin/env python
# выполняет поиск заданного ключевого слова в файлах с указанным расширением внутри заданной папки с помощью команды grep, и выводит найденные совпадения в консоль.

import os  # Импорт модуля для работы с файловой системой
import subprocess  # Импорт модуля для запуска внешних команд, таких как grep


# Функция для поиска ключевого слова в файлах с указанным разрешением внутри указанной папки
def search_keyword(keyword, folder_path, extension):
    try:
        # Создаём список файлов с нужным расширением в указанной папке
        files = [f for f in os.listdir(folder_path) if f.endswith(extension)]

        # Если список пуст, выводим сообщение и завершаем функцию
        if not files:
            print(f"NO {extension} files found in the specified folder.")
            return

        # Перебираем каждый найденный файл
        for file in files:
            # Получаем полный путь к файлу
            file_path = os.path.join(folder_path, file)

            # Запускаем команду grep для поиска ключевого слова в файле (регистронезависимо)
            result = subprocess.run(
                ["grep", "-i", keyword, file_path], capture_output=True, text=True
            )

            # Получаем список строк, где встречается ключевое слово
            occurrences = result.stdout.strip().split("\n")

            # Выводим заголовок для каждого файла
            print(f"Occurrences of '{keyword}' in {file}:")

            # Выводим каждое совпадение
            for occurrence in occurrences:
                print(f"- {occurrence}")
    except FileNotFoundError:
        # Обрабатываем ситуацию, если указанной папки не существует
        print("Folder not found, please provide a valid folder path.")


def main():
    # Запрашиваем у пользователя ключевое слово для поиска
    keyword = input("Enter the keyword to search: ")

    # Запрашиваем путь к папке, в которой нужно искать
    folder_path = input("Enter the folder path to search in: ")

    # Запрашиваем расширение файлов, в которых будет производиться поиск
    extension = input("Enter extension of the file: ")

    # Вызываем функцию поиска
    search_keyword(keyword, folder_path, extension)


# Проверка, что скрипт запущен напрямую, а не импортирован как модуль
if __name__ == "__main__":
    main()
