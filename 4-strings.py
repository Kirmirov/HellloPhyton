# -*- coding: utf-8 -*-

# First task
print('Введите число: ', end='')
number = input()
print('В введенном числе', len(number), 'цифр')

print('****************************************')

# Second task
print('Введите текст: ', end='')
text = input()

if text in 'Glo Academy':
    print('YES')
else:
    print('NO')
    
print('****************************************')

# Third task
print('Введите название статьи: ', end='')
articleOne = input()
print('Введите название статьи: ', end='')
articleTwo = input()
print('Введите название статьи: ', end='')
articleThree = input()

if len(articleOne) > len(articleTwo) and len(articleOne) > len(articleThree):
    print(articleOne)
if len(articleTwo) > len(articleOne) and len(articleTwo) > len(articleThree):
    print(articleTwo)
if len(articleThree) > len(articleOne) and len(articleThree) > len(articleTwo):
    print(articleThree)

print('****************************************')

# Fourth task
print('Введите название команды: ', end='')
teamName = input()
print(teamName * 5)

print('****************************************')

# Fifth task
print('Введите email: ', end='')
email = input()

if email in '@':
    print('Корректный')
else:
    print('Некорректный')