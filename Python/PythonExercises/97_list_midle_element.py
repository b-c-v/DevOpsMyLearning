amount_numbers = int(input("How many numbers do you want to enter: "))
number_list = []

while amount_numbers % 2 == 0:
    print("The number must be odd")
    amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter {i +1} number: "))
    number_list.append(number)

middle_element_list = len(number_list) // 2
print(len(number_list) // 2)
print(f"The middle element of the list is: {number_list[middle_element_list]}")

# find the middle element using a variable amount_numbers
middle_element_position = amount_numbers // 2
print(amount_numbers // 2)
print(f"The middle element is: {number_list[middle_element_list]}")
print(
    f"Square root of the number {number_list[middle_element_list]} is: {number_list[middle_element_list]**0.5}"
)
