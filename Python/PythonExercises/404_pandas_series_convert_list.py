import pandas as pd

user_series = pd.Series(dtype=int)

amount_numbers = int(input("How many numbers do you want to enter: "))
for i in range(amount_numbers):
    user_number = int(input(f"Enter your {i+1} number: "))
    user_series.loc[len(user_series)] = user_number


print(f"Your series is:\n{user_series}")
print(f"Convert series to list: {user_series.tolist()}")
