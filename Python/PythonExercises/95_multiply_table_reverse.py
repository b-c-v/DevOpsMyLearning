number = int(input("Enter your number: "))
for i in range(10, 0, -1):
    print(f"{number} * {i} = {number * i}")

for i in range(10, 0, -2):
    print(f"Odd numbers only: {number} * {i} = {number * i}")