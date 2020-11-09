"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

import random
import re

secret_numb = random.randint(1, 1_000_000)

inp_numb = input('Try to guess secret number, enter number from 1 to 1 000 000:  ')
while secret_numb != 'exit':
    if inp_numb.isdigit():
        if int(inp_numb) < 1 or int(inp_numb) > 1000000:
            print('Over range limit, enter number from 1 to 1000000')
        else:
            if int(inp_numb) < secret_numb:
                print('Secret number is more then your')
            elif int(inp_numb) > secret_numb:
                print('Secret number is less then your')
            elif int(inp_numb) == secret_numb:
                print('you win')
        inp_numb = input('Try again:  ')
    else:
        inp_numb = input('Not a number! Enter a number!:  ')
        

