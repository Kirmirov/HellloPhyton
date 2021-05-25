# -*- coding: utf-8 -*-
import math

# First task
b_words = 65
l_words = 97
while b_words < 91:
    print(chr(b_words), chr(l_words))
    b_words += 1
    l_words += 1
print('****************************************')

# Second task
while True:
    print('Введите символ: ', end='')
    ch = input()
    if ch == 'e':  # Escape from cycle
        break
    print('Цифра' if ord(ch) >= 48 and ord(ch) <= 57 else 'НЕ цифра')
print('****************************************')

# Third task
while True:
    print('Введите символ: ', end='')
    ch = input()
    if ch == '0':  # Escape from cycle
        break
    print('Заглавная. Кириллица' if ord(ch) >= 1040 and ord(ch) <= 1071 else 'НЕ загалавная')
print('****************************************')

# Fourth task
while True:
    print('Введите символ: ', end='')
    ch = input()
    if ch == '0':  # Escape from cycle
        break
    if ord(ch) >= 65 and ord(ch) <= 90:
        print(ch.lower())
    if ord(ch) >= 97 and ord(ch) <= 122:
        print(ch.upper())
print('****************************************')

# Fifth task
print('Введите первый символ: ', end='')
f_ch = input()
print('Введите второй символ: ', end='')
s_ch = input()

for n in range(min(ord(f_ch), ord(s_ch)), max(ord(f_ch), ord(s_ch)) + 1):
    print(chr(n))
print('****************************************')

# Sixth task
print('Введите строку: ', end='')
string = input()

for ch in range(len(string)):
    if ord(string[ch]) >= 48 and ord(string[ch]) <= 57:
        print(string[ch], end='')
    else:
        continue
print('****************************************')

# Seventh task
print('Введите с заглавной буквы фамилию: ', end='')
s_name = input()
print('Введите имя: ', end='')
f_name = input()
print('Введите отчество: ', end='')
th_name = input()

print(s_name, ' ', f_name[0], '.', th_name[0], '.', sep='')
print('****************************************')

# Eighth task
print('Введите строку: ', end='')
string = input()
total = 0
for ch in range(len(string) - 1):
    f_ch = string[ch]
    s_ch = string[ch + 1]
    if f_ch == s_ch:
        total += 1

print('Колличество ппарных символов в строке: ', total)
print('****************************************')

# Nineth task
print('Введите строку: ', end='')
string = input()

print('Длинна строки: ', len(string))
print('Последний символ строки: ', string[::-1][0])
print('Первые два символа строки: ', string[:2])
print('Последние два символа строки: ', string[len(string) - 2:len(string)])
print('Строка в обратном порядке: ', string[::-1])
print('Строка в с удаленными первым и последним символом: ', string[1:len(string) - 1])
print('****************************************')

# Tenth task
print('Введите строку: ', end='')
string = input()
total = 1
for ch in range(len(string)):
    if string[ch] == ' ':
        total += 1

print('Колличество слов в строке:', total)