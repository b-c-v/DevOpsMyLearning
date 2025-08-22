first_number = int(input("Enter firs number: "))
second_number = int(input("Enter second number: "))
odd_list = []
even_list = []

for i in range(first_number, second_number):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Odd numbers: {odd_list}")
print(f"Even numbers: {even_list}")

odd_sum = sum(odd_list)
even_sum = sum(even_list)

print(f"Sum of all odd numbers {odd_sum}")
print(f"Sum of all even numbers {even_sum}")
print(f"Their sum is {odd_sum + even_sum}")


# Sum of numbers divisible by 3 or 5
divisible_3 = []
divisible_5 = []

for i in range(first_number, second_number):
    if i % 3 == 0:
        divisible_3.append(i)
    if i % 5 == 0:
        divisible_5.append(i)

print(f"Numbers divisible by 3: {divisible_3}")
print(f"Numbers divisible by 5: {divisible_5}")
print(f"Their sum is {sum(divisible_3) + sum(divisible_5)}")

divisible_3_sum = sum(divisible_3)
divisible_5_sum = sum(divisible_5)

print(f"Sum of all numbers divisible by 3 is {divisible_3_sum}")
print(f"Sum of all numbers divisible by 5 is {divisible_5_sum}")
print(f"Their sum is {divisible_3_sum + divisible_5_sum}")
