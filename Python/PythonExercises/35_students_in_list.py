my_list = []
for i in range(10):
    student = input("Enter any name of the student: ")
    my_list.append(student)

print(f"List of the students: {my_list}")

my_list.reverse()
print(f"List of the students in reverse mode: {my_list}")

my_list.pop(0)
my_list.pop(len(my_list) - 1)
print(f"List of the students with deleted first and last student's name: {my_list}")

# another way to remove first and last items
if len(my_list) >= 2:
    my_list = my_list[1:-1]
else:
    my_list = []

print(f"Deleted with if statement: {my_list}")
