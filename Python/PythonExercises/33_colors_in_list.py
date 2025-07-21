my_list = []
for i in range(6):
    color = input("Enter any color: red, orange, yellow, green, blue, violet\n")
    my_list.append(color)

select_color = input("Please enter the color that needs to be counted: ")

print(f"Color {select_color} is found in the list {my_list.count(select_color)} times")
