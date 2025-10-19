from random import *
def is_valid(num): # Функция проверки корректности введенных данных
    if  num.isdigit(): 
        if 1 <= int(num) <= 100:
            return True 
        else:
            return False
    else:
        return False
#основная программа
random_number = randint(1,101)
print(random_number)
def is_main():
    print('Добро пожаловать в числовую угадайку')
    attempts = 0 # количество попыток 
    while True:
        n = input('Введите число от 1 до 100')
    
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            n = int(n)
        if n < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            #тратит одну попытку
            attempts += 1
        elif n > random_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            #тратит одну попытку
            attempts += 1
        else: 
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print( 'Количество попыток=',attempts)
            break
is_main()

