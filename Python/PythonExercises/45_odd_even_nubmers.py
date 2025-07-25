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
