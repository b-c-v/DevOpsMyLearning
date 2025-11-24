import pandas as pd

user_dict = {}

num_colors = int(input("How many colors do you want to enter in this dictionary: "))

for i in range(num_colors):
    color_code = int(input(f"Enter color code: "))
    color_name = input(f"Enter color name: ")
    user_dict[color_code] = color_name

print(f"Your dictionary is: {user_dict}")

user_series = pd.Series(user_dict)
print(f"Your series is: {user_series}")
