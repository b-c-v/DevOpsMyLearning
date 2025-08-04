list_color = []

amount_numbers = int(input("How many color codes do you want to enter: "))

for i in range(amount_numbers):
    color = input(f"Enter any color: red, orange, yellow, green, blue, violet etc.\n")
    list_color.append(color)


new_list_color = list_color.copy()

print(f"Color list {list_color}")
print(f"Copy of color list {new_list_color}")
