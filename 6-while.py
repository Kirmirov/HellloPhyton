# -*- coding: utf-8 -*-
import math

# First task
print('Введите число: ', end='')
num = int(input())
total = 0

while num % 2 == 0:
    total += 1
    num /= 2

print('Введенное число делится на 2 без остатка', total, 'раз')
print('****************************************')
    
# Second task
print('Введите число: ', end='')
num = int(input())
five_count = 0

while num != 0:
    check_num = num % 10
    if check_num == 5:
        five_count += 1
    num = num // 10

print('В введеном числе содержится', five_count, 'цифр пять')
print('****************************************')

# Third task
print('Введите число: ', end='')
num_main = int(input())
num_change = num_main
num_sum = 0

while num_change != 0:
    num_sum += num_change % 10
    num_change = num_change // 10

print('YES' if num_main % num_sum == 0 else 'NO')

# Fourth task
print('Введите число: ', end='')
num_main = int(input())
num_max = 0
num_min = math.inf

while num_main != 0:
    num = num_main % 10
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num
    num_main = num_main // 10

print('Максимальное число:', num_max)
print('Минимальное число:', num_min)
print('****************************************')

# Fifth task
print('Введите число: ', end='')
num_main = int(input())
count_pos = 0
count_neg = 0

while num_main != 0:
    if num_main > 0:
        count_pos += 1
    else:
        count_neg += 1
    print('Введите число: ', end='')
    num_main = int(input())
print('Произведение количества положительных и отрицательных чисел последовательности равно: ', count_neg * count_pos)
print('****************************************')

# Sixth task
print('Введите число: ', end='')
num = int(input())
num_sum = 0
num_count = 0

while num != 0:
    num_count += 1
    num_sum += num
    print('Введите число: ', end='')
    num = int(input())
    
print('Cреднее арифметическое элементов последовательности равно: ', int(num_sum / num_count))