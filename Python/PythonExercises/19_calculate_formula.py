a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = (a + b + c) * (a / b) * (2 * a + 3 * b)
print("Result is: ", result)

d = int(input("Enter forth number: "))
result2 = (d + a + 2 * a * b) / (d * (4 * c + 10))
print(result2)
