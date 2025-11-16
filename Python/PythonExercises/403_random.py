import random

random_number = random.randrange(1, 11)

user_number = int(input("Enter any number from 1 to 10: "))

if user_number == random_number:
    print("You win!")
else:
    print("You lost!")
