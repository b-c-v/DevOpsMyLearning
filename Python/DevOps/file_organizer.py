#!/bin/env python
import os  # модуль для работы с файловой системой
import shutil  # модуль для операций копирования и перемещения файлов


def organize_files(source_directory):
    # Словарь с типами файлов и соответствующими им расширениями
    file_types = {
        "python": [".py"],
        "text": [".txt"],
        "json": [".json"],
        "yaml": [".yaml", ".yml"],
    }
    # Создание папок для каждого типа файлов, если они ещё не существуют
    for directory in file_types.keys():
        os.makedirs(os.path.join(source_directory, directory), exist_ok=True)

    # Перебор всех файлов в указанной директории
    for filename in os.listdir(source_directory):
        file_path = os.path.join(
            source_directory, filename
        )  # Получаем полный путь к файлу

        if os.path.isfile(file_path):  # Проверяем, что это файл, а не папка
            # Получаем расширение файла в нижнем регистре
            file_extension = os.path.splitext(filename)[1].lower()
            # Сравниваем расширение с известными типами
            for file_type, extensions in file_types.items():
                # Если расширение соответствует одному из известных
                if file_extension in extensions:
                    # Путь до папки назначения
                    destination_directory = os.path.join(source_directory, file_type)
                    # Перемещаем файл
                    shutil.move(
                        file_path, os.path.join(destination_directory, filename)
                    )
                    # Прерываем цикл, как только нашли подходящий тип
                    break


if __name__ == "__main__":
    # Задаём директорию текущей папки
    source_dir = "."
    organize_files(source_dir)
