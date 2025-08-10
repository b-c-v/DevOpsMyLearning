name_list = ["ser", "Nick", "12345", "1234", "54321"]

amount_names = int(input("How many names do you want to enter: "))

for i in range(amount_names):
    name = input(f"Enter any name: ")
    name_list.append(name)

name_list.sort(reverse=False)
print("List of names in ascending order", name_list)
for i in name_list:
    if len(i) == 5:
        print(f"This name contains only 5 characters: {i}")

name_list.sort(reverse=True)
print(f"List of names in descending order", name_list)
descending_list = []
for i in name_list:
    descending_list.append(i + ".")
print(descending_list)

# the same as code before, but in a shorter way
students_final = [name + "." for name in name_list]
print(students_final)
