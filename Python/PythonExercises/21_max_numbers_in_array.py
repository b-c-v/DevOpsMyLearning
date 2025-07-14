import array as arr

my_array = arr.array("i")
for i in range(5):
    number = int(input("Enter any number: "))
    my_array.append(number)
print("Maximum number:", max(my_array))

m = my_array[0]
for j in range(len(my_array)):
    if my_array[j] > m:
        m = my_array[j]
print("Maximum number:", m)
