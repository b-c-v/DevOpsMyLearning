number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))
greater_5_less_10 = 0
even_sum = 0

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

for i in number_list:
    if i >= 5 and i <= 10:
        greater_5_less_10 += i
    if i % 2 == 0:
        even_sum += i

print(f"Sum of the numbers greater then 5 and less then 10 is: {greater_5_less_10}")
print(f"Sum of the even numbers is: {even_sum}")
