import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("tmp.csv")

file_col = df.columns.tolist()

# Get the column names
print("Column names:", file_col)
