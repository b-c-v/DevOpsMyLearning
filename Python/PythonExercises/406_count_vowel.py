user_string = input("Enter any phrase: ")
found_vowels = []

vowels = ["a", "e", "i", "o", "u"]

for letter in user_string:
    if letter.lower() in vowels:
        found_vowels.append(letter)

if len(found_vowels) > 0:
    print(f"Vowels in your phrase: {found_vowels}")
    print(
        f"There're {len(found_vowels)} vowels and {len(user_string) - len(found_vowels)} non-vowel characters."
    )
else:
    print("Your phrase doesn't contain any vowels!!")
