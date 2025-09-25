import pandas as pd


# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas openpyxl

# Загружаем Excel-файл в DataFrame (таблицу pandas)
df = pd.read_excel("tmp.xlsx")

sum_column = df.iloc[:, 1].sum()
print(f"The sum of numbers in the second column: {sum}")

product_column = df.iloc[:, 1].product()
print(f"The product of numbers in the second column: {product_column}")

count_column = df.iloc[:, 1].count()
print(f"Count numbers in the second column: {count_column}")

mean_column = df.iloc[:, 1].mean()
print(f"Average value in the second column: {mean_column}")
