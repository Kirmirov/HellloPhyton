# -*- coding: utf-8 -*-
import math

# First task
while True:
    print('Введите число: ', end='')
    num = int(input())
    if num < 10:
        continue
    if num > 100:
        break
    else:
        print('Вывод числа: ', num)

print('****************************************')
    
# Second task
while True:
    print('Введите число от 1 до оо: ', end='')
    num = int(input())
    if num == 0:  # Escape from cycle
        break
    if num == 1:
        print('NO')
        continue
    div = 2
    while num % div != 0:
        div += 1
    print('YES' if div == num else 'NO')
print('****************************************')

# Third task
while True:
    print('Введите число: ', end='')
    num = int(input())
    is_contains = False
    if num == 0:  # Escape from cycle
        break
    while num != 0:
        if num % 10 == 1:
            is_contains = True
            break
        num = num // 10
    print('Введенное число содержит цифру 1' if is_contains else 'Введенное число НЕ содержит цифру 1')
print('****************************************')

# Fourth task
print('Введите число: ', end='')
num = int(input())

for n in range(1, num + 1):
    if n >= 2 and n <= 8:
        continue
    if n >= 128 and n <= 256:
        continue
    if n >= 1024 and n <= 2048:
        continue
    print(n)
print('****************************************')

# Fifth task
for n in range(7):
    for j in range(6):
        print('2', end=' ')
    print()
print('****************************************')

# Sixth task
sp = 2
for n in range(10):
    for j in range(10):
        j += 1
        if j == sp:
            sp += 1
            break
        print(j, end=' ')
    print()
print('****************************************')

# Seventh task
hours = 0
minutes = 0
seconds = 0
# Консоль имеет ограничение на установленный буфер так что данные на 24 часа выводятся не корректно
while hours != 24:
    print(hours, ':', minutes, ':', seconds)
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes >= 60:
        minutes = 0
        hours += 1
print('****************************************')

# Eighth task
print('Введите число: ', end='')
num = int(input())
total = 0
for n in range(1, num + 1):
    while n != 0:
        if n % 10 == 5:
            total += 1
        n = n // 10
print('От 1 до', num, 'число 5 встречается', total, 'раз')
print('****************************************')

# Nineth task
print('Введите число: ', end='')
num = int(input())
while num > 9:
    i = int(num % 10)
    num = num // 10
    num = num + i
print('Цифровой корень числа равен: ', num)
