import pandas as pd

# openpyxl - если нужно работать именно с Excel-файлом как документом (формулы, стили, редактирование)
# pandas - лучше использовать если нужно анализировать данные.
# pandas.read_excel по умолчанию использует движок openpyxl

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas openpyxl


# Читаем весь Excel-файл (по умолчанию первый лист)
df = pd.read_excel("tmp.xlsx")

print(df)

print("Use openpyxl")
import openpyxl
# Загружаем созданный файл
wb = openpyxl.load_workbook("tmp.xlsx")
ws = wb.active

# Читаем все строки и печатаем
for row in ws.iter_rows(values_only=True):
    print(row)