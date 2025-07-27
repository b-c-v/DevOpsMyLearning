sentence = input("Enter any sentence: ")
# number of characters
# number of words
# number of specific word
print(f"Number of characters in the sentence: {len(sentence)}")
words = sentence.split()
print(f"Number of words in the sentence: {len(words)}")

find_word = input("Enter a word that should be find: ")
print(f"The word \"{find_word}\" is found in the sentence {sentence.count(find_word)} times")
