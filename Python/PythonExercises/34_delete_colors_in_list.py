my_list = []
for i in range(5):
    color = input("Enter any color: red, orange, yellow, green, blue, violet\n")
    my_list.append(color)

print(f"List with all items: {my_list}")

my_list.pop(len(my_list) - 1)
print(f"Deleted last item in the list {my_list}")

my_list.pop(0)
print(f"Deleted first item in the list {my_list}")
