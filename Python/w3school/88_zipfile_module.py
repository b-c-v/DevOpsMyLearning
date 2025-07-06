# zipfile модуль применяется для работы с ZIP-архивами — создания, чтения, распаковки и изменения .zip файлов
import zipfile

# Создание нового ZIP-архива и добавление в него файла
with zipfile.ZipFile("archive.zip", mode="w") as archive:
    archive.write("example.txt")  # Добавляет файл в архив

# Добавление нескольких файлов:
files = ["file1.txt", "file2.txt", "data.csv"]

with zipfile.ZipFile("backup.zip", "w") as zipf:
    for file in files:
        zipf.write(file)

# Распаковка архива:
with zipfile.ZipFile("archive.zip", "r") as archive:
    archive.extractall("output_folder")  # Извлекает все файлы в папку

# Чтение содержимого архива:
with zipfile.ZipFile("archive.zip", "r") as archive:
    print("Содержимое архива:", archive.namelist())

# Проверка файла:
if zipfile.is_zipfile("archive.zip"):
    print("Это zip-архив")
else:
    print("Это НЕ zip-архив")
