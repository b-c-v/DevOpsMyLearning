import random


def check_answer(answer):
    if answer == 'yes':
        return answer
    elif answer == 'no':
        return False
    else:
        print('Your answer is not correct')


def generate_password(pas_number, chars):
    for _ in range(pas_number):
        print(*random.sample(chars, pas_length), sep='')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'il1Lo0O'

chars = ''

print('How many passwords do you want to generate')
pas_number = int(input())
print('Enter length of password')
pas_length = int(input())
print('Do you want to use Numbers: yes or no?')
pas_with_digits = check_answer(input())
print('Do you want to use Uppercase Letters: yes or no?')
pas_with_uppercase_letters = check_answer(input())
print('Do you want to use Lowercase Letters: yes or no?')
pas_with_lowercase_letters = check_answer(input())
print('Do you want to use Symbols: yes or no?')
pas_with_symbols = check_answer(input())
print('Do you want to exclude Ambiguous characters: yes or no?')
pas_with_ambiguous = check_answer(input())

if pas_with_digits:
    chars += digits
if pas_with_uppercase_letters:
    chars += uppercase_letters
if pas_with_lowercase_letters:
    chars += lowercase_letters
if pas_with_symbols:
    chars += punctuation
if pas_with_ambiguous:
    for i in ambiguous:
        chars = chars.replace(i, '')


generate_password(pas_number, chars)
