from collections import Counter

number_list = []
amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

# Count occurrences of each number in the list
counts = Counter(number_list)
# variable counts is a dictionary-like object (specifically, a Counter object from the collections module).
# Keys - the unique elements from number_list
# Values - the count of how many times each element appears
print(counts)

# Find the maximum count value (how many times the most frequent number appears)
max_count = max(counts.values())

# ***Find the most occurring numbers:***

# 1. Using list comprehension
# counts.items() gives (key, value) pairs - (num, cnt)
# num = the key (the number from the list)
# cnt = the value (its count)
# If cnt == max_count, the num is added to the new list most_occurring
most_occurring = [num for num, cnt in counts.items() if cnt == max_count]

"""
# 2. Using a for loop
most_occurring = []
for num, cnt in counts.items():
    if cnt == max_count:
        most_occurring.append(num)
"""

if len(most_occurring) == 1:
    print(f"The most occurring element in the list is: {most_occurring[0]}")
else:
    print(f"There are multiple most occurring elements: {most_occurring}")


# ***Find the less occurring numbers:***

min_count = min(counts.values())
less_occurring = [num for num, cnt in counts.items() if cnt == min_count]
if len(less_occurring) == 1:
    print(f"The less occurring element in the list is: {less_occurring[0]}")
else:
    print(f"There are multiple less occurring elements: {less_occurring}")
