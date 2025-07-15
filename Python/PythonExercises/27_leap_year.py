year = int(input("Enter any year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This is a leap year!")
else:
    print("This is NOT a leap year!")

# Store 5 years in array and then print only leap years
my_list = []
for i in range(5):
    number = int(input("Enter any year: "))
    my_list.append(number)

for i in range(len(my_list)):
    if (my_list[i] % 4 == 0 and my_list[i] % 100 != 0) or my_list[i] % 400 == 0:
        print("This is a leap year:", my_list[i])
