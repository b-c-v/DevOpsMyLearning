# tarfile применяется для создания, чтения и распаковки TAR-архивов (.tar, .tar.gz, .tgz, .tar.bz2, .tar.xz)
import tarfile

"""
Поддерживаемые режимы открытия:
"r"         Только чтение .tar
"r:gz"      Чтение .tar.gz / .tgz
"r:bz2"     Чтение .tar.bz2
"r:xz"      Чтение .tar.xz
"w"         Запись .tar
"w:gz"      Запись с gzip-сжатием
"w:bz2"     Запись с bzip2-сжатием
"w:xz"      Запись с xz-сжатием
"""

# Создание архива с gzip-сжатием
with tarfile.open("backup.tar.gz", "w:gz") as archive:
    archive.add("folder_to_backup")  # Добавляет папку (рекурсивно)

# Распаковка архива:
with tarfile.open("backup.tar.gz", "r:gz") as archive:
    archive.extractall("output_folder")  # Распаковывает всё содержимое

#  Получение списка файлов:
with tarfile.open("backup.tar.gz", "r:gz") as archive:
    print(archive.getnames())  # Список путей файлов в архиве

# Извлечение одного файла:
with tarfile.open("backup.tar.gz", "r:gz") as archive:
    archive.extract("folder_to_backup/file.txt", path="output_dir")
