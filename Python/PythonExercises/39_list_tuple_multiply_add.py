my_list = []
for i in range(5):
    number = int(input("Enter any number\n"))
    my_list.append(number)


def additional(any_list):
    total_sum = 0
    for i in any_list:
        total_sum += i
    return total_sum


def multiply(any_list):
    total_product = 1
    for i in any_list:
        total_product *= i
    return total_product


print(f"The sum of the numbers in the list is: {additional(my_list)}")
print(f"The multiplication of the numbers in the list is: {multiply(my_list)}")

# Convert list to tuple and then use the same functions
my_tuple = tuple(my_list)
print(f"The sum of the numbers in the tuple is: {additional(my_tuple)}")
print(f"The multiplication of the numbers in the list is: {multiply(my_tuple)}")
