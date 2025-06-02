# os модуль используется для взаимодействия с операционной системой. Он предоставляет функции для работы с файловой системой, путями, переменными окружения, процессами и другими системными возможностями.
# модуль pathlib — более современный и объектно-ориентированный способ работы с путями.
import os

current_dir = os.getcwd()
print(f"current directory: {current_dir}")

# Show files in directory
entries = os.listdir(current_dir)
print("directory contents: ", entries)

# Delete a File
os.remove("demofile.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Rename file
os.rename("myfile.txt", "renamed_file.txt")

# Create folder
os.mkdir("any_name_dir")


# Delete Folder
# Note: You can only remove empty folders.
# To delete an entire folder, use the os.rmdir() method:
os.rmdir("any_name_dir")

# Объединение путей (кроссплатформенно)
full_path = os.path.join("/home/user", "docs", "file.txt")
print(f"Full path is: {full_path}")

# Получение информации (метаданных) о файле или директории
# Получение информации о файле "21-1_os-module.py"
file_info = os.stat("21-1_os-module.py")

# Печать полной информации о файле (включая время последнего изменения, доступа, права и т.д.)
print("All info: ", file_info)

# Вывод размера файла в байтах
print("File size: ", file_info.st_size, "bytes")
