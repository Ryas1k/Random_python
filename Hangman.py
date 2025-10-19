from random import *
word_list = ["погода", "дождь", "лето", "хлеб"]
# функция get_word() которая возвращает случайное слово
#  из списка word_list в верхнем регистре.
def get_word():
    word = choice(word_list).upper()
    return word

#Функция display_hangman() принимает один аргумент tries –
#количество попыток угадывания слова – и возвращает текущее состояние игры в графическом виде:
def display_hangman(tries):

    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]

def play(word):
    
    #тело
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print()
    print(display_hangman(tries))
    print(word_completion)
    while tries != 0 and not guessed:
        print('Введите букву или слово')
        letter = input().upper()
        if letter.isalpha() and len(letter) == 1:
            if letter in guessed_letters:
                print('Данную букву вы уже называли!!!')
            elif not letter in word:
                tries -= 1
                guessed_letters.append(letter)
                print('Данной буквы нет в загаданном слове') 
            else:
                print('Данная буква',letter, 'есть в загаданном слове')
                guessed_letters.append(letter)
                word_list_completion = list(word_completion) #['_', '_', '_', '_', '_']
            
                indeks = [i for i in range(len(word)) if word[i] == letter]
            
                for index in indeks:
                    word_list_completion[index] = letter
                word_completion = ''.join(word_list_completion)
            
                if not '_' in word_completion:
                    guessed = True    
                    word_completion = word
            
        if letter.isalpha() and len(letter) == len(word):

            if letter in guessed_words:
                print('Данное слово вы уже вводили!')
            elif letter != word:
                tries -= 1
                guessed_words.append(letter)
                print('Вы не угадали со словом!', letter)  
            else:
                guessed = True
                word_completion = word
            
        else:
            print('Введите букву или слово!')
        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print('Поздравляю, Вы победили!')    
    else:
        print('Вы проиграли!',word,'Было загаданным словом! В следующий раз повезет)') 

again = 'да'
while again == 'да': 
    word = get_word()
    print(word)
    play(word)    
    again = input('Играть еще хочешь? Да или нет?').lower()    
    while again not in ('да' ,'нет'):
        print('Давай заканчивай этот цирк!','Напиши Да(да) или Нет(нет)',sep='\n')
        again = input()
     
