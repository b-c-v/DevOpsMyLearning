sentence = input("Enter any sentence: ")
print(f"Number of characters in the sentence: {len(sentence)}")

words = sentence.split()
print(f"Number of words in the sentence: {len(words)}")

find_word = input("Enter a word that should be find: ")
count = sentence.count(find_word)

if count > 0:
    print(
        f'The word "{find_word}" is found in the sentence {sentence.count(find_word)} times'
    )
    want_replace = input("Do you want to replace it Y/n? ").lower()
    if want_replace == "n":
        print("OK, thank you!")
    else:
        replace_word = input("Enter the replacement word: ")
        print(sentence.replace(find_word, replace_word))
else:
    print(f'The word "{find_word}" was not found in the sentence.')
