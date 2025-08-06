# The := operator is called the walrus operator or the assignment expression operator.
# It allows to assign a value to a variable as part of an expression. This can make certain constructs more concise.
"""
variable := expression
"""
# Traditional way:

value = input("Traditional: Enter something: ")
while value != "quit":
    print(f"Traditional: You entered: {value}")
    value = input("Traditional: Enter something: ")

# With := operator:

while (value := input("Walrus: Enter something: ")) != "quit":
    print(f"Walrus: You entered: {value}")


# Traditional way:
results = []
for x in range(10):
    y = x**2
    if y > 10:
        results.append(y)
print("Traditional:", results)

# With := operator:
results = [y for x in range(10) if (y := x**2) > 10]
print("Walrus:", results)
