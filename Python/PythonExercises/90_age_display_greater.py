amount_numbers = int(input("How many ages do you want to enter: "))
ages_list = []
ages_14_20_list = []

for i in range(amount_numbers):
    age = int(input(f"Enter {i +1} age: "))
    ages_list.append(age)
    if age > 10 and age < 20:
        ages_14_20_list.append(age)
print(f"Full list of ages: {ages_list}")
print(f"List of ages between 14 and 20:  {ages_14_20_list}")
