nested_list = [[9, 7, 6, 5], [5, 4, 3], [2, 1, 0], [-1, -2, -3], 2, "test"]
print("Nested list:", nested_list)


nested_count = 0

for i in nested_list:
    if isinstance(i, list):
        nested_count += 1

print(f"The total number of lists in a nested list {nested_count}")
