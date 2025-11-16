user_string = input("Enter any sentence: ")

vowels = ["a", "e", "i", "o", "u"]
spaces_count = 0
vowels_count = 0


for letter in user_string:
    if letter == " ":
        spaces_count += 1
    if letter.lower() in vowels:
        vowels_count += 1


total_length = len(user_string)
print(f"Total chars: {total_length}")
print(f"Total chars without spaces: { total_length - spaces_count}")
print(f"Total words: {spaces_count + 1}")
print(f"Total vowels: {vowels_count}")

