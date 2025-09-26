import pandas as pd


# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas openpyxl

# Загружаем Excel-файл в DataFrame (таблицу pandas)
df = pd.read_excel("tmp.xlsx")

max_number = df.iloc[:, 1].max()
print(f"The max number is: {max_number}")

min_number = df.iloc[:, 1].min()
print(f"The min number is: {min_number}")


# copy data to another list
with pd.ExcelWriter(
    "tmp.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace"
) as writer:
    df.to_excel(writer, sheet_name="CopiedData", index=False)
