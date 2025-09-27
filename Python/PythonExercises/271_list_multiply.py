amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")

multiply_number = int(input("Enter a number to multiply the list: "))

multiply_list = [i * multiply_number for i in user_list]
print(f"List after multiplying: {multiply_list}")

multiply_even_list = [i * multiply_number for i in user_list if i % 2 == 0]
print(f"List with multiplied even numbers: {multiply_even_list}")
