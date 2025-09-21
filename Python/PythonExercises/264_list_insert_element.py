amount_numbers = int(input("How many numbers do you want to enter: "))

number_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]

print(f"Your list is: {number_list}")

insert_number_before = int(input(f"Enter any number to insert before each element: "))

insert_before_list = [str(insert_number_before) + str(i) for i in number_list]
print(insert_before_list)

insert_number_after = int(input(f"Enter any number to insert after each element: "))
insert_after_list = [str(i) + str(insert_number_after) for i in insert_before_list]
print(insert_after_list)
