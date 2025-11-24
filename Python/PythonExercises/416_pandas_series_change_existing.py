import pandas as pd

user_series_1 = pd.Series(dtype=int)
user_series_2 = pd.Series(dtype=int)


def fill_series(amount_numbers, user_series):
    for i in range(amount_numbers):
        user_number = int(input(f"Enter your {i+1} number: "))
        user_series.loc[len(user_series)] = user_number


amount_numbers = int(
    input("How many numbers do you want to enter in the first series: ")
)
fill_series(amount_numbers, user_series_1)


amount_numbers_2 = int(
    input("How many numbers do you want to add to the first series: ")
)
fill_series(amount_numbers_2, user_series_2)

user_changed_series = pd.concat([user_series_1, user_series_2], ignore_index=True)
print(f"Updated series: {user_changed_series}")
