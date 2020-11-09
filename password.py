"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

import re

chek = True
par = input('Vvedite parol: ')

while chek:
    if re.search(r'\d', par) and re.search(r'[a-zA-Z]', par) and len(par) >= 8:
        print('Parol is enough difficult')
        chek = False
    else:
        par = input('Parol is too easy, try another one: ')
