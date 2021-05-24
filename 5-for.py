# -*- coding: utf-8 -*-
import math

# First task
for prog in range(25):
    print('Hello, GloAcademy!')
    
print('****************************************')
    
# Second task
print('Введите число: ', end='')
numb = int(input())

for n in range(numb + 1):
    print('Квадрат числа', n, 'равен', n * n)

print('****************************************')

# Third task
print('Введите первое число: ', end='')
num_one = int(input())
print('Введите второе число: ', end='')
num_two = int(input())

if num_one == num_two:
    print('Ошибка! Числа должны быть разными!')

min_num = min(num_one, num_two)
max_num = max(num_one, num_two)

for n in range(min_num, max_num + 1):
    print(n)

print('****************************************')

# Fourth task
print('Введите первое число: ', end='')
num_one = int(input())
print('Введите второе число: ', end='')
num_two = int(input())

if num_one == num_two:
    print('Ошибка! Числа должны быть разными!')

min_num = min(num_one, num_two)
max_num = max(num_one, num_two)

for n in range(min_num, max_num + 1):
    if n % 2 == 0:
        print(n)

print('****************************************')

# Fifth task
print('Введите число: ', end='')
numb = int(input())

for n in range(1, 11):
    print(numb, '*', n, '=', numb * n)

print('****************************************')

# Sixth task
print('Введите число: ', end='')
numb = int(input())
total = 0
for n in range(1, numb):
    if n % 10 == 1 or n % 10 == 3 or n % 10 == 7:
        total += n
print('Сумма чисел от 1 до', numb, 'равна:', total)
print('****************************************')

# Seventh task
print('Введите число: ', end='')
numb = int(input())

is_entry = False
total = 1
for n in range(1, numb):
    if n % 10 == 2 or n % 10 == 9:
        total *= n
        is_entry = True
        
print('Произведение чисел от 1 до', numb, 'равна:', total if is_entry else 0)
print('****************************************')

# Eighth task
print('Введите кол-личество чисел: ', end='')
num_count = int(input())
max_num = 0
min_num = math.inf

for n in range(num_count):
    print('Введите число: ', end='')
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print('Максимальное число:', max_num)
print('Минимальное число:', min_num)
print('****************************************')

# Nineth task

print('Введите кол-личество чисел: ', end='')
num_count = int(input())
is_num_even = True

for n in range(num_count):
    print('Введите число: ', end='')
    num = int(input())
    if num % 2 != 0:
        is_num_even = False
        
print('NO' if is_num_even else 'YES')
print('****************************************')

# Tenth task

print('Введите кол-личество чисел: ', end='')
num_count = int(input())
is_num_even = True

for n in range(num_count):
    print('Введите число: ', end='')
    num = int(input())
    if num % 2 == 0:
        is_num_even = False
        
print('YES' if is_num_even else 'NO')
print('****************************************')