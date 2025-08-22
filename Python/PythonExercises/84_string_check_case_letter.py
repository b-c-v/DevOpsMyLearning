def check_uppercase(word):
    if word[0].upper() != word[0]:
        return False
    else:
        return True


first_name = input("Enter your firstname: ")
while True:
    if check_uppercase(first_name):
        break
    else:
        print("The first name should start with a capital letter. Please try again!")
        first_name = input("Enter your firstname: ")
        check_uppercase(first_name)

lastname = input("Enter your lastname: ")
while True:
    if check_uppercase(lastname):
        break
    else:
        print("The lastname should start with a capital letter. Please try again!")
        lastname = input("Enter your lastname: ")
        check_uppercase(first_name)

print(f"Your full name is: {first_name} {lastname}")
