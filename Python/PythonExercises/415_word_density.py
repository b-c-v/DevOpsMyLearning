user_text = input("Enter any text: ")
user_word = input("Enter a word that should be counted: ")

total_word_count = len(user_text.split())
print(f"There are {total_word_count} words in the sentence.")

user_word_count = user_text.lower().count(user_word.lower())
word_density = (user_word_count / total_word_count) * 100


if word_density > 3:
    print(f'The density of the word "{user_word}" is more than 3% and is {word_density:.2f}%')
else:
    print(f'The density of the word "{user_word}" is {word_density:.2f}%')
