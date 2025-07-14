# my_array = []
# for i in range(5):
#     number = float(input("Enter any number: "))
#     my_array.append(number)
# print(sum(my_array))

import array as arr

my_array = arr.array("i")
for i in range(5):
    number = int(input("Enter any number: "))
    my_array.append(number)
print("Summary of numbers: ", sum(my_array))
