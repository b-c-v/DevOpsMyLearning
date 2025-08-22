# shutil в Python применяется для высокоуровневой работы с файлами, директориями и архивами. Он предоставляет удобные функции для копирования, перемещения, удаления и архивации файлов и папок.
import shutil

# Копирование файла (только содержимое, без метаданных)
shutil.copy("example.txt", "backup.txt")

# Копирование файла с метаданными (например, время изменения)
shutil.copy2("example.txt", "backup.txt")

# Копирование всей папки
shutil.copytree("project", "project_backup")

# Перемещение файла или папки
shutil.move("file.txt", "archive/file.txt")

# Удаление всей директории
shutil.rmtree("temp_folder")

# Создание zip архива из папки
shutil.make_archive("project_backup", "zip", "project")

# Получение информации о диске
total, used, free = shutil.disk_usage("/")
print(f"Свободно: {free // (1024 ** 3)} ГБ")
