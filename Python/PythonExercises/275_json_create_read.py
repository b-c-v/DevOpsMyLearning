# json module when working with general Python objects and simple JSON data. For encoding (writing) and decoding (reading) JSON data.

# pandas when dealing with structured, tabular data for analysis. Provides high-level methods for reading/writing JSON files directly into DataFrames, which are useful for data analysis and manipulation.

import json

# List of user dictionaries
users = [
    {"name": "Alice", "age": 25, "skills": ["Python", "Data Analysis"]},
    {"name": "Bob", "age": 30, "skills": ["Java", "Machine Learning"]},
]

# Write to JSON file
with open("tmp.json", "w") as file:
    json.dump(users, file, indent=4)

# Read JSON file
with open("tmp.json", "r") as file:
    users = json.load(file)

print(f"Print whole file as {type(users)}:\n{users}")
print("Print only name and age:")
for user in users:
    print(user["name"], user["age"])


# Convert list to dict using "name" as key
users_dict = {user["name"]: user for user in users}
print(f"Print whole file as {type(users_dict)}:\n{users_dict}")


# Using Pandas module
import pandas as pd

# Create DataFrame
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob"],
        "age": [25, 30],
        "skills": [["Python", "Data Analysis"], ["Java", "Machine Learning"]],
    }
)

# Write DataFrame to JSON
df.to_json("tmp.json", orient="records", indent=4)

# Read JSON into a DataFrame
df = pd.read_json("tmp.json")

# DataFrame behaves like a dictionary of columns (df["name"], df["age"]) internally. It's not actually a Python dict, but a DataFrame that mimics dict-like access for columns.
print(f"Print whole file as {type(users_dict)}:\n{df}")
print("Print only name and age:")
print(df[["name", "age"]])  # Access column
