number = int(input(f"Enter your any number: "))

previous_number = number - 1
next_number = number + 1

print(f"Previous number is {previous_number}")
print(f"Next number is {next_number}")

additional_number = int(input(f"Enter any number that you want to add: "))
print(f"Summary with previous number {previous_number + additional_number}")
print(f"Summary with next number is {next_number + additional_number}")
