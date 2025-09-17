import array as ar

amount_numbers = int(input("How many numbers do you want to enter: "))
number_array = ar.array("i", [])

for i in range(amount_numbers):
    number = int(input(f"Enter {i +1} number: "))
    number_array.append(number)

print(number_array)

append_number = int(input("Enter any number to append to array: "))

number_array.append(append_number)
print(f"Print your array: {number_array}")
