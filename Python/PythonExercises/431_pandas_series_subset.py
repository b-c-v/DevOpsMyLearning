import pandas as pd

user_series = pd.Series(dtype=int)


def fill_series(amount_numbers, user_series):
    for i in range(amount_numbers):
        user_number = int(input(f"Enter your {i+1} number: "))
        user_series.loc[len(user_series)] = user_number


amount_numbers = int(
    input("How many numbers do you want to enter in the first series: ")
)
fill_series(amount_numbers, user_series)

print(f"Your series:\n{user_series}")

# creates a filtered version of that series containing only values smaller than a user-specified number.
subset_number = int(input("Enter a number to use as an upper limit: "))
user_changed_series = user_series[user_series < subset_number]
print(f"Updated series:\n{user_changed_series}")
