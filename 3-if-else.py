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

leftSum = 0
while (leftPart != 0):
    leftSum = leftSum + leftPart % 10
    leftPart = leftPart // 10

rightSum = 0
while (rightPart != 0):
    rightSum = rightSum + rightPart % 10
    rightPart = rightPart // 10

if leftSum == rightSum:
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
print('Введите колличество задач для выполнения: ', end='')
taskCount = int(input())
print('Введите колличество задач выполняемых за день: ', end='')
taskCountOnDay = int(input())
if taskCount % taskCountOnDay != 0:
    daysCount = (taskCount // taskCountOnDay) + 1
else:
    daysCount = (taskCount // taskCountOnDay)
print('Колличество дней для выпонения всех задач:', daysCount)
print('****************************************')

# Sixth task
print('Введите номер кармана: ', end='')
sectorNumber = int(input())

if sectorNumber >= 1 and sectorNumber <= 10 or sectorNumber >= 19 and sectorNumber <= 28:
    if sectorNumber % 2 == 0:
        print('Черный!')
    else:
        print('Красный!')
if sectorNumber >= 11 and sectorNumber <= 18 or sectorNumber >= 29 and sectorNumber <= 36:
    if sectorNumber % 2 == 0:
        print('Красный!')
    else:
        print('Черный!')

if sectorNumber < 0 or sectorNumber > 36:
    print('Ошибка ввода!')

if sectorNumber == 0:
    print('Зеленый!')