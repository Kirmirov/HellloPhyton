# -*- coding: utf-8 -*-
import math

# First task
print('Введите колличество слов в списке: ', end='')
words_list = []

for w in range(int(input())):
    print('Введите слово: ', end='')
    words_list.append(input())

print('Введите слово для поиска: ', end='')
search_word = input()

for word in words_list:
    if search_word.upper() in word.upper():
        print(word)
print('****************************************')

# Second task
path = 'D:\MyDocuments\Python\Courses\план обучения.txt'
elem_list = path.split('\\')

for elem in elem_list:
    print(elem)
print('****************************************')

# Third task
print('Введите IP адрес: ', end='')
split_ip = input().split('.')
isIP = True

for num in split_ip:
    check_num = int(num)
    if check_num > 255:
        isIP = False

print('Корректный IP' if isIP else 'НЕ корректный IP')
print('****************************************')

# Fourth task
# First decision
print('Введите последовательность чисел через пробел: ', end='')
num_list = input().split()
couple_count = 0

for index in range(len(num_list) - 1):
    check_list = num_list[index + 1::]
    check_num = num_list[index]
    for num in check_list:
        if check_num in num:
            couple_count += 1

print('Колличество цифр имеющих пару: ', couple_count)
# Second decision
from math import ceil
print('Введите последовательность чисел через пробел: ', end='')
num_list = input().split()
couple_count = 0

for num in num_list:
    if num_list.count(num) > 1:
        couple_count += num_list.count(num) - 1
        
print('Колличество цифр имеющих пару: ', ceil(couple_count / 2))
print('****************************************')

# Fifth task
print('Введите последовательность чисел через пробел: ', end='')
num_list = input().split()

for num in num_list:
    if num_list.count(num) == 1:
        print(num, end=' ')

