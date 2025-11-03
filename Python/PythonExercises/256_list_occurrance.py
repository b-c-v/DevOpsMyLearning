from collections import Counter

amount_numbers = int(input("How many numbers do you want to enter: "))

number_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]

occurrence_list = [
    f"The number {str(i)} is found {number_list.count(i)} times" for i in number_list
]
print(occurrence_list)

# Better, because it counts occurrences of each number in the list. And print number and its occurrence only once
counts = Counter(number_list)
# variable counts is a dictionary-like object (specifically, a Counter object from the collections module).
# Keys - the unique elements from number_list
# Values - the count of how many times each element appears
for k, v in counts.items():
    print(f"The number {k} is found {v} times")
