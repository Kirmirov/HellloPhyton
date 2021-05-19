# -*- coding: utf-8 -*-

# First task
print('Введите первое число: ', end='')
a = int(input())
print('Введите второе число: ', end='')
b = int(input())
print('Сумма квадратов чисел равна: ', (a * a) + (b * b))
print('****************************************')

# Second task
print('Введите первое число: ', end='')
a = int(input())
print('Введите второе число: ', end='')
b = int(input())
print(a, 'умноженное на', b, 'равно', a * b)
print(a, 'деленное на', b, 'равно', a / b)
print(a, 'нацело деленное на', b, 'равно', a // b)
print('Остаток от деления', a, 'на', b, 'равен', a % b)
print(a, 'в степени', b, 'равно', a ** b)
print('****************************************')

# Third task
print('Введите целое трехзначное положительное число: ', end='')
wholeNum = int(input())
firstNum = wholeNum // 100
secondNum = (wholeNum // 10) % 10
thirdNum = wholeNum % 10
numSum = firstNum + secondNum + thirdNum
print('Сумма цифр числа', wholeNum, 'равна', numSum)
print('****************************************')

# Fourth task
print('Введите цену мяча в рублях: ', end='')
ruble = int(input())
print('в копейках: ', end='')
penny = int(input())
print('Введите количество приобретаемых мячей: ', end='')
ballCount = int(input())
sumInPenny = (penny * ballCount) % 100
sumInRuble = (ruble * ballCount) + penny // 100
print('За', ballCount, 'мяча нужно заплатить', sumInRuble, 'рублей и', sumInPenny, 'копеек')
print('****************************************')

# Fifth task
print('Введите количество секунд: ', end='')
time = int(input())
seconds = time % 60
minutes = (time // 60) % 60
hours = (time // 60) // 60
print(time, 'секунд - это', hours, 'часов', minutes, 'минут', seconds, 'секунд')
print('****************************************')

# Sixth task
print('Введите целое четырехзначное число: ', end='')
wholeNum = int(input())
firstNum = wholeNum // 1000
secondNum = (wholeNum // 100) % 10
thirdNum = (wholeNum // 10) % 10
fourthNum = wholeNum % 10
maxNum = max(firstNum, secondNum, thirdNum, fourthNum)
print('У числа', wholeNum, 'максимальная цифра равна', maxNum)
print('****************************************')

# Seventh task
print('Введите натуральное число, не превосходящее 1 000 000 000: ', end='')
numberStr = input()
lastNumberGroup = int(numberStr[-3:])
firstNum = lastNumberGroup // 100
secondNum = (lastNumberGroup // 10) % 10
thirdNum = lastNumberGroup % 10
numSum = firstNum + secondNum + thirdNum
print('У числа', numberStr, 'сумма последних трех цифр равна', numSum)
