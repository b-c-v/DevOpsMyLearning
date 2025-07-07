username = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
    difference = 18 - age
    print(
        f"{username}, sorry! You cannot participate in voting, you will be able to participate after {difference} year"
    )
else:
    print(f"{username}, you're welcome!")
