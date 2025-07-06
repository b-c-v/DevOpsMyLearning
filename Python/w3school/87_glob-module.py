# glob модуль применяется для поиска файлов и директорий по шаблону с подстановочными символами (wildcards)

import glob

# Найти все .txt файлы в текущей папке
txt_files = glob.glob("*.txt")
print(txt_files)

# Найти все .py файлы в папке scripts/
py_files = glob.glob("scripts/*.py")
print(py_files)

# Рекурсивный поиск всех .log файлов во всех подпапках
log_files = glob.glob("**/*.log", recursive=True)
print(log_files)

# Использование шаблонов с символами подстановки
image_files = glob.glob("images/img_??.jpg")  # img_01.jpg, img_22.jpg и т.п.
print(image_files)
