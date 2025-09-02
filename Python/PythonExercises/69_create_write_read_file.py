with open("myfile.txt", "w") as file:
  file.write(input("Enter your name: ") + "\n")
  file.write(input("Enter your age: " + "\n"))

with open("myfile.txt") as f:
  print(f.read())

number1 = int(input("Enter any number: "))
number2 = int(input("Enter any number: "))
total_sum = number1 + number2

with open("myfile.txt", "a") as file:
  file.write(str(total_sum))

with open("myfile.txt") as f:
  print(f.read())