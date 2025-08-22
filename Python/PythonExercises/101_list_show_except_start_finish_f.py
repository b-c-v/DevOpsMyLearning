name_list = []

amount_names = int(input("How many names do you want to enter: "))

for i in range(amount_names):
    name = input(f"Enter your {i+1} name: ")
    name_list.append(name)


for i in name_list:
    if i[0].lower() != "f" and i[-1].lower() == "n":
        print(f'This name don\'t start with "F" and end with "n": {i}')

# use string methods

for i in name_list:
    if not i.lower().startswith("f") and i.lower().endswith("n"):
        print(f'Method: This name don\'t start with "F" and end with "n": {i}')
