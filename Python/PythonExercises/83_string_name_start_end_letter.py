name_list = []

amount_numbers = int(input("How many names do you want to enter: "))

for i in range(amount_numbers):
    name = input(f"Enter your {i+1} name: ")
    name_list.append(name)


for i in name_list:
    if i[0].lower() == "f":
        print(f'This name starts with "F": {i}')
    if i[-1].lower() == "f":
        print(f'This name ends with "f": {i}')

# use string methods

for i in name_list:
    if i.lower().startswith("f"):
        print(f'Method: this name starts with "F": {i}')
    if i.lower().endswith("f"):
        print(f'Method: this name ends with "f": {i}')
