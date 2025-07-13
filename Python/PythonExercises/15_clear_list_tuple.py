my_list = []
for i in range(6):
    number = int(input("Enter any number: "))
    my_list.append(number)

print("List items: ", my_list)
my_list.clear()
print("Cleared list: ", my_list)

# tuple is immutable, which is why you need to create a list, add items to the list, and then convert it into a tuple.
my_tuple_list = []
for i in range(6):
    number = int(input("Enter any number: "))
    my_tuple_list.append(number)

my_tuple = tuple(my_tuple_list)
print("Tuple items: ", my_tuple)
# clear tuple
my_tuple = ()
print("Cleared tuple: ", my_tuple)
