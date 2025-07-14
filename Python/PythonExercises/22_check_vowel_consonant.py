vowels = ["a", "e", "i", "o", "u"]
letter = input("Enter any letter: ")
for i in range(len(vowels)):
    if letter.lower() == vowels[i]:
        print("You entered a vowel letter")
        break
    else:
        print("You entered a consonant letter")
        break

# using set
vowels_set = {"a", "e", "i", "o", "u"}
if letter.lower() in vowels_set:
    print("Set: you entered a vowel letter")
else:
    print("Set: you entered a consonant letter")
