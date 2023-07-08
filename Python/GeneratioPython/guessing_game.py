
import random              # Подключите модуль random;
# Функция is_valid() возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае


def is_valid(number):
    return 1 <= number <= 100


def guessing_game(r):
    print('delete_random', r)
    print('Введите число от 1 до 100')

    counter = 0
    while True:
        s = int(input())
        if is_valid(s):
            n = s
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue

        counter += 1  # подсчет попыток, сделанных пользователем

        # сравнение введенного числа с загаданным числом
        if n < r:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > r:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        else:
            print('Вы угадали, поздравляем!')
            print('Вы сделали', counter, 'попыток')
            greetings()
        break


def greetings():
    print('Хотите сыграть: да или нет?')
    if input() == 'да':
        guessing_game(random.randrange(1, 101))
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return False


# Выведите текст приветствия пользователю: 'Добро пожаловать в числовую угадайку'.
print('Добро пожаловать в числовую угадайку')
greetings()
