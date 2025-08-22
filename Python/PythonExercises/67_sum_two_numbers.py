while True:
    number_1 = int(input("Please enter first number (0–50): "))
    if 0 <= number_1 <= 50:
        break
    print("First number should be positive and less than 50!")

while True:
    number_2 = int(input("Please enter second number (0–50): "))
    if 0 <= number_2 <= 50:
        break
    print("Second number should be positive and less than 50!")

print(f"The sum of two numbers is: {number_1+number_2}")