# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.Гарантируется, что между различными словами присутствует один пробел.

en_alphabet = [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
ru_alphabet = [chr(i) for i in range(1040,1104)]

def caesar(text, k):
    if txt[0] in en_alphabet:
        alphabet = en_alphabet
        n = 26
    else:
        alphabet = ru_alphabet
        n = 32
    for i in range(len(text)):
        if text[i].isalpha():
            x = alphabet.index(text[i])
            if text[i].isupper():
                print(alphabet[(x + k) % n], end = '')
            else:
                print(alphabet[(x + k) % n + n], end='')
        else:
            print(text[i], end = '')
    print(end = ' ')
txt = input('Введите текст: ')
l = txt.split()
for word in l:
    counter = 0
    for letter in range(len(word)):
        if word[letter].isalpha():
            counter += 1
    caesar(word, counter)