nested_list = [[9, 7, 6, 5], [5, 4, 3], [2, 1, 0], [-1, -2, -3]]
print("Nested list:", nested_list)

item = int(input("Enter nested list index: "))

if not 0 <= item < len(nested_list):
    print("You select wrong index")
else:
    chosen_list = nested_list[item]
    print(
        f"Sum of the numbers in the nested list {chosen_list} with index {item} is {sum(chosen_list)}"
    )

# Find nested list with the smallest sum

tmp = sum(nested_list[0])
smallest_sum_list = []
for i in nested_list:
    if sum(i) < tmp:
        tmp = sum(i)
        smallest_sum_list = i
print(f"The nested list with the smallest sum is {smallest_sum_list}")

# using min() function
# key=sum - Instead of comparing the lists directly, compare their sums
smallest_sum_function = min(nested_list, key=sum)
print(f"Function: The nested list with the smallest sum is {smallest_sum_function}")