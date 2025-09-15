amount_numbers = int(input("How many numbers do you want to enter: "))

user_set = {
    int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)
}
print(f"Your set: {user_set}")

even_set = {i for i in user_set if i % 2 == 0}
print(f"Set with even numbers: {even_set}")

odd_set = {i for i in user_set if i % 2 != 0}
print(f"Set with odd numbers: {odd_set}")
