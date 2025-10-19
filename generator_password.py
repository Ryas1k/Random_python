from random import *

def is_kol_password():
  kol_password = input('Количество паролей для генерации?')
  while kol_password.isdigit() == False:
    print('Хватит тупить! Введи количество паролей для генерации')
    kol_password = input('Количество паролей для генерации?')  
  return int(kol_password)
def is_len_password():
  len_password = input('Длина одного пароля')
  while len_password.isdigit() == False:
    print('Хватит тупить! Введи длину одного пароля')  
    len_password = input('Длина одного пароля')  
  return int(len_password)


def is_includ_digits():
  includ_digits = input('Включать ли цифры 0123456789? [д/н]')
  while includ_digits.lower() not in ('да' ,'нет'):
    print('Хватит тупить! Включать ли цифры 0123456789?','Напиши Да(да) или Нет(нет)',sep='\n')
    includ_digits = input()
  return includ_digits


def is_includ_uppercase_letters():
  includ_uppercase_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? [д/н]')
  while includ_uppercase_letters.lower() not in ('да' ,'нет'):
    print('Ну ты тупой !!!','Напиши Да(да) или Нет(нет)',sep='\n')  
    includ_uppercase_letters = input()
  return includ_uppercase_letters

def is_includ_lowercase_letters():
  includ_lowercase_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? [д/н]')  
  while includ_lowercase_letters.lower() not in ('да' ,'нет'):
    print('Ну ты тупой !!!','Напиши Да(да) или Нет(нет)',sep='\n')
    includ_lowercase_letters = input() 
  return includ_lowercase_letters 

def is_includ_punctuation():
  includ_punctuation = input('Включать ли символы !#$%&*+-=?@^_? [д/н]')  
  while includ_punctuation.lower() not in ('да' ,'нет'):
    print('Давай заканчивай этот цирк!','Напиши Да(да) или Нет(нет)',sep='\n')
    includ_punctuation = input()
  return includ_punctuation

def is_not_includ_simvols():
  not_includ_simvols = input('Исключать ли неоднозначные символы il1Io0O? [д/н]')  
  while not_includ_simvols.lower() not in ('да' ,'нет'):
    print('Давай заканчивай этот цирк!','Напиши Да(да) или Нет(нет)',sep='\n')
    not_includ_simvols = input()
  return not_includ_simvols

      # Функция генерация одного пароля
def get_chars():
  # исходные данные локальные переменные 
  digits = '0123456789'                             #цифры
  lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'  #нижний регист
  uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #верхний регист
  punctuation = '!#$%&*+-=?@^_'                     #знаки 
  chars = ''  # пустая строка 
  if includ_digits.lower() in ('да', 'Да','д', 'Yes', 'Y','y'):
    chars += digits 
  if includ_uppercase_letters.lower() in ('да', 'Да','д', 'Yes', 'Y','y'):
    chars += uppercase_letters
  if includ_lowercase_letters.lower() in ('да', 'Да','д', 'Yes', 'Y','y'):
    chars += lowercase_letters
  if includ_punctuation.lower() in ('да', 'Да','д', 'Yes', 'Y','y'):
    chars += punctuation
  if not_includ_simvols.lower() in ('да', 'Да','д', 'Yes', 'Y','y'):
    for i in 'il1Lo0O':
        chars.replace(i, '')
  return chars
# Функции
kol_password = is_kol_password()                          # Количество паролей для генерации
len_password = is_len_password()                          # Длина одного пароля
includ_digits = is_includ_digits()                        # Включать ли цифры 0123456789
includ_uppercase_letters = is_includ_uppercase_letters()  # Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ
includ_lowercase_letters = is_includ_lowercase_letters()  # Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz
includ_punctuation = is_includ_punctuation()              # Включать ли символы !#$%&*+-=?@^_
not_includ_simvols = is_not_includ_simvols()              # Исключать ли неоднозначные символы il1Lo0O
chars = get_chars()                                       

def generate_password(length,chars): #length: длина пароля и chars: алфавит из символов которого состоит пароль
  test_password = sample(chars, length)
  password = ''.join(test_password) # генерация одного пароля с учетом длины и количества символов
  return  password

# Генерация нужного количества паролей
for _ in range(kol_password):
   print(generate_password(len_password,chars))






