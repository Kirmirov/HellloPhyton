# -*- coding: utf-8 -*-

# First task
print('Введите пароль: ', end='')
password = input()
print('Введите пароль повторно: ', end='')
passwordCheck = input()

if (password == passwordCheck):
    print('Все окей!')
else:
    print('Пароли не совпадают!')
print('****************************************')

# Second task
print('Введите одно вещественное число: ', end='')
numberCheck = float(input())

if numberCheck == 0:
    print('Ноль')
if numberCheck > 0:
    print('Положительное')
if numberCheck < 0:
    print('Отрицательное')
print('****************************************')

# Third task
print('Введите шестизначные номер билета: ', end='')
ticketNumber = int(input())
leftPart = ticketNumber // 1000
rightPart = ticketNumber % 1000

if leftPart == rightPart:
    print('Билет', ticketNumber, 'счастливый')
else:
    print('Билет', ticketNumber, 'НЕсчастливый')

print('****************************************')

# Fourth task
print('Введите вес дыни от 1 кг до 100 кг: ', end='')
melonWeight = int(input())

if melonWeight - 2 == 0 or melonWeight % 2 != 0:
    print('NO')
else:
    print('YES')
print('****************************************')

# Fifth task
print('Введите номер кармана: ', end='')
sectorNumber = int(input())

if sectorNumber >= 1 and sectorNumber <= 10:
    if sectorNumber % 2 == 0:
        print('Красный!')
    else:
        print('Черный!')
if sectorNumber >= 11 and sectorNumber <= 18:
    if sectorNumber % 2 == 0:
        print('Черный!')
    else:
        print('Красный!')
if sectorNumber >= 19 and sectorNumber <= 28:
    if sectorNumber % 2 == 0:
        print('Красный!')
    else:
        print('Черный!')
if sectorNumber >= 29 and sectorNumber <= 36:
    if sectorNumber % 2 == 0:
        print('Черный!')
    else:
        print('Красный!')

if sectorNumber < 0 or sectorNumber > 36:
    print('Ошибка ввода!')

if sectorNumber == 0:
    print('Зеленый!')
