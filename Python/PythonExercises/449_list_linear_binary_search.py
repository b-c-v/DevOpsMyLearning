number_count = int(input("How many numbers do you want to enter: "))

user_numbers = [int(input(f"Enter your {i+1} number: ")) for i in range(number_count)]

print(f"Your list is: {user_numbers}")

search_number = int(input("Enter a number to search: "))

index_list = []

for i in range(len(user_numbers)):
    if user_numbers[i] == search_number:
        index_list.append(i)

if len(index_list) > 0:
    print(f"Number {search_number} was found at indices {index_list}")
else:
    print(f"The number was not found in the list.")


def binary_search(sorted_list, target):
    # Set the starting index of the search range
    left_index = 0

    # Set the ending index of the search range
    right_index = len(sorted_list) - 1

    # Continue searching while the range is valid
    while left_index <= right_index:
        # Find the middle index of the current search range
        middle_index = (left_index + right_index) // 2

        # Get the value at the middle index
        middle_value = sorted_list[middle_index]

        # Check if the middle value is the target
        if middle_value == target:
            # Target found — return its index
            return middle_index

        # If the target is greater, ignore the left half
        elif middle_value < target:
            left_index = middle_index + 1

        # If the target is smaller, ignore the right half
        else:
            right_index = middle_index - 1

    # If the loop ends, the target is not in the list
    return -1


result = binary_search(user_numbers, search_number)

# Print the result in a readable way
if result != -1:
    print(f"Binary search: Number found at index {result}")
else:
    print("Binary search: Number not found in the list")
