user_string = input("Enter any sentence: ")
delete_string = input("Please enter the characters you want to find and delete: ")

if delete_string in user_string:
    print("The characters were found")
    print(f"The sentence with specified characters deleted: {user_string.replace(delete_string, '')}")
else:
    print("Nothing to delete!")
