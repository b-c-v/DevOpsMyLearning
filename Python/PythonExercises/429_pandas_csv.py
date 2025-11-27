import pandas as pd

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas
file_path = "tmp.csv"

try:
    file = pd.read_csv("tmp.csv")

except FileNotFoundError:
    print("Image file not found. Please check the path.")

else:
    print(file.shape)
    print(file.to_string)
