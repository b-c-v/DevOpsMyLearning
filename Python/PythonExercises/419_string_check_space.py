filename = input("Enter any filename: ").strip()

space_count = filename.count(" ")

if space_count > 0:
    print("Filenames shouldn't include spaces!")
    print(f'Your filename will be renamed to "{filename.replace(" ", "_")}"')

else:
    print("You entered a valid filename!")
