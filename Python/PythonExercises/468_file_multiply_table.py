number = int(input("Enter your number: ").strip())
file_name = input("Enter a name of the file: ").strip()

with open(file_name, "a") as file:
    file.write("Multiplication table of number " + str(number) + "\n")
    for i in range(1, 11):
        line = f"{number} * {i} = {number * i}"
        file.write(line + "\n")
