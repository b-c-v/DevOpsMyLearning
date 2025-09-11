user_word = input("Enter any word: ")

if user_word.isidentifier():
    print(f'You can use the word "{user_word}" as the variable, function or class name')
else:
    print(f'"{user_word}" is not acceptable as a variable, function or class name')

user_number = input("Enter any number: ")

if user_number.isdigit():
    print(f"You entered the number: {user_number}")
else:
    print(f'"{user_number}" is not a number')
