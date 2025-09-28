# pandas - provides high-level abstractions like DataFrame and Series. Designed for data analysis and manipulation. Optimized for working with large datasets efficiently.

# csv - works with raw text data (lists, dictionaries) instead of structured objects like DataFrames. Lightweight but does not support analysis (only parsing and writing). Memory-efficient since it processes files row by row. Best for simple updates or transformations without complex analysis.

import csv

data_list = []

with open("tmp.csv", "w", newline="") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(["Name", "Age", "Grade"])
    write.writerow(["Alice", 14, "9th"])
    write.writerow(["Bob", 15, "10th"])
    write.writerow(["Charlie", 13, "8th"])

with open("tmp.csv", "r") as csvfile:
    reade = csv.reader(csvfile)
    for row in reade:
        data_list.append(row)

print(f"Data saved in the list: {data_list}")

# using panda module
import pandas as pd

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pandas openpyxl

# Create a DataFrame
df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [14, 15, 13],
        "Grade": ["9th", "10th", "8th"],
    }
)

# Save DataFrame to CSV without including the index
df.to_csv("tmp.csv", index=False)

# Read CSV back into a new DataFrame
df2 = pd.read_csv("tmp.csv")

# Convert DataFrame to a nested list
data_list = df2.values.tolist()

print(f"Data saved in the list: {data_list}")
