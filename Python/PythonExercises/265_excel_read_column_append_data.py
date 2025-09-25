import pandas as pd


# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas openpyxl

column_number = int(input("Please enter a column number: "))

# Загружаем Excel-файл в DataFrame (таблицу pandas)
df = pd.read_excel("tmp.xlsx")


column_data = df.iloc[:, column_number]

print(column_data)

# usecols работает только при чтении файлов
usecols_data = pd.read_excel("tmp.xlsx", usecols="A:B")
print(f"Read few columns:\n{usecols_data}")


# append data to excel file
from openpyxl import load_workbook
workbook = load_workbook("tmp.xlsx")
sheet = workbook.active # Выбираем активный лист (обычно первый по умолчанию)
sheet.append(["Roberto", 2000]) # Добавляем новую строку данных в конец таблицы
workbook.save("tmp.xlsx")
usecols_data = pd.read_excel("tmp.xlsx", usecols=[0,1])
print(f"After adding a new line:\n{usecols_data}")