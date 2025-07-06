# csv модуль для чтения и записи данных в формате CSV
import csv

# Запись данных в CSV-файл
with open("example.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)  # Создаём объект для записи
    writer.writerow(["Имя", "Возраст"])  # Записываем заголовок
    writer.writerow(["Анна", 30])  # Записываем строку с данными
    writer.writerow(["Борис", 25])

# Чтение данных из CSV-файла
with open("example.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)  # Создаём объект для чтения
    for row in reader:
        print(row)  # Выводим каждую строку как список
