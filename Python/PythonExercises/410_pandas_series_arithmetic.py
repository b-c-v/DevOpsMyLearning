import pandas as pd

user_series_1 = pd.Series(dtype=int)
user_series_2 = pd.Series(dtype=int)


amount_numbers = int(input("How many numbers do you want to enter: "))


def fill_series(amount_numbers, user_series):
    for i in range(amount_numbers):
        user_number = int(input(f"Enter your {i+1} number: "))
        user_series.loc[len(user_series)] = user_number


print("First series")
fill_series(amount_numbers, user_series_1)
print("Second series")
fill_series(amount_numbers, user_series_2)
print(f"Your first series is:\n{user_series_1}")
print(f"Your second series is:\n{user_series_2}")

print(f"Addition:\n{user_series_1 + user_series_2}")
print(f"Subtraction:\n{user_series_1 - user_series_2}")
print(f"Multiplication:\n{user_series_1 * user_series_2}")
print(f"Division:\n{user_series_1 / user_series_2}")
print(f"Modulus:\n{user_series_1 % user_series_2}")
