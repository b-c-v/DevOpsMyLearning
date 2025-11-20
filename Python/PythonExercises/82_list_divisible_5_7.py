first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
divisible_5 = []
divisible_7 = []
divisible_5_7 = []

for i in range(first_number, second_number):
    if i % 5 == 0:
        divisible_5.append(i)
    if i % 7 == 0:
        divisible_7.append(i)
    if i % 5 == 0 and i % 7 == 0:
        divisible_5_7.append(i)


print(f"Numbers divisible by 5 : {divisible_5}")
print(f"Numbers divisible by 7: {divisible_7}")
print(f"Numbers divisible by 5 and 7: {divisible_5_7}")
