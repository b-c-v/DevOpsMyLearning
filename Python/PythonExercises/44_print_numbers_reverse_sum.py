first_number = int(input("Enter firs number: "))
second_number = int(input("Enter second number: "))
step = -1
total_sum = 0

if second_number > first_number:
    start = second_number
    end = first_number
else:
    start = first_number
    end = second_number

for i in range(start, end, step):
    total_sum += i
    print(i)

print("The sum of all numbers is: ", total_sum)
