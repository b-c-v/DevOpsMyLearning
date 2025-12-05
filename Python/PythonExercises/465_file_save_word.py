has_vowel = False

user_word = input("Enter any word without vowels: ").strip()
file_name = input("Enter a name of the file: ").strip()

vowels = ["a", "e", "i", "o", "u"]

for letter in user_word:
    if letter.lower() in vowels:
        has_vowel = True
        break

if has_vowel:
    print("Word shouldn't contain any vowels!")
else:
    with open(file_name, "a") as file:
        print(f'Saving word "{user_word}" to the file "{file_name}"')
        file.write(user_word + "\n")
