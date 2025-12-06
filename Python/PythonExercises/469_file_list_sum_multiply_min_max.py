import os

number_count = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(number_count)]

file_name = input("Enter a name of the file: ").strip()


# multiply_numbers
def multiply_numbers(any_list):
    total_product = 1
    for i in any_list:
        total_product *= i
    return total_product


with open(file_name, "a+") as file:
    file.write(f"Your list is: {user_list}\n")
    file.write(f"The sum of all numbers: {sum(user_list)}\n")
    file.write(f"The multiplication of all numbers: {multiply_numbers(user_list)}\n")
    file.write(f"The minimum number: {min(user_list)}\n")
    file.write(f"The maximum number: {max(user_list)}\n")
    file.write(f"The first number: {user_list[0]}\n")
    file.write(f"The last number: {user_list[-1]}\n")
    # Move the cursor to the beginning of the file before reading
    file.seek(0)
    print(f"Data saved in the file {file_name}\n{file.read()}")

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully.")
else:
    print("File does not exist.")
