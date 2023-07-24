import random

word_list = ['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 'borrow', 'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port', 'pose', 'quit', 'elite', 'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score', 'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 'tail', 'forget', 'form', 'talent', 'formal', 'uncle', 'gear', 'gender', 'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear', 'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 'judge', 'equal', 'lord', 'king', 'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom', 'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count', 'good', 'young', 'youth', 'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty', 'look', 'time', 'long', 'steal', 'talk', 'return', 'hide', 'honour', 'like', 'pride', 'clock', 'true', 'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 'copy', 'follow', 'rich', 'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame', 'lack', 'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend', 'fill', 'know', 'month', 'rest', 'debate', 'stock', 'exchange', 'note', 'sell', 'equity', 'large', 'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different', 'attract', 'cover', 'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree', 'price', 'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world', 'include', 'insurance', 'pension', 'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open', 'offer', 'type', 'network', 'example', 'potential', 'specific', 'accept', 'match', 'sale', 'place', 'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 'flow', 'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage', 'firm', 'investor', 'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar', 'purchase', 'drive', 'late', 'system']

def get_word():
    return(random.choice(word_list).upper())

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print(word)
    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    while tries >= 0:
        l = input('Enter you letter or word: ').upper()
        print(display_hangman(tries))
        if l.isalpha() and len(l) == 1:
            if l in guessed_letters:
                print("You have already entered this letter! Be careful!")
            else:
                if l in word:
                    print("The letter is in the word")
                    for i in range(len(word)):
                        if word[i] == l:
                            word_completion[i] = l
                    print(*word_completion, sep='')
                else:
                    print("Wrong letter. You have", tries, "tries")
                    tries -= 1
                guessed_letters.append(l)
        elif l.isalpha() and len(l) > 1:
            if l in guessed_words:
                print('You have already entered this word! Be careful!')
            elif l.upper() == word:
                print('You won!')
                break
            else:
                print("You entered the wrong word. You have", tries, "tries")
                guessed_words.append(l)
                tries -= 1
        else:
            print("It's not a letter or a word")
        
        if '_' not in word_completion:
            print('You won!')
            break
    if tries < 0:
         print('You lost!')
         print('Hidden word was -', word)


play(get_word())