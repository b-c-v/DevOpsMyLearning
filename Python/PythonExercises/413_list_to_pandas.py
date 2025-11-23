import pandas as pd

user_series = pd.Series(dtype=int)

number_count = int(input("How many values do you want to enter: "))

user_numbers = [int(input(f"Enter your {i+1} number: ")) for i in range(number_count)]
print(f"Your list is: {user_numbers}")

alphabet = "abcdefghijklmnopqrstuvwxyz"
indexes = [alphabet[i] for i in range(number_count)]

numbers_series = pd.Series(user_numbers, index=indexes)
print(f"Your series: {numbers_series}")
