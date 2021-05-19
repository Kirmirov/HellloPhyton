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
print(a, 'СѓРјРЅРѕР¶РµРЅРЅРѕРµ РЅР°', b, 'СЂР°РІРЅРѕ', a * b)
print(a, 'РґРµР»РµРЅРЅРѕРµ РЅР°', b, 'СЂР°РІРЅРѕ', a / b)
print(a, 'РЅР°С†РµР»Рѕ РґРµР»РµРЅРЅРѕРµ РЅР°', b, 'СЂР°РІРЅРѕ', a // b)
print('РћСЃС‚Р°С‚РѕРє РѕС‚ РґРµР»РµРЅРёСЏ', a, 'РЅР°', b, 'СЂР°РІРµРЅ', a % b)
print(a, 'РІ СЃС‚РµРїРµРЅРё', b, 'СЂР°РІРЅРѕ', a ** b)
print('****************************************')

# Third task
print('Р’РІРµРґРёС‚Рµ С‚СЂРµС…Р·РЅР°С‡РЅРѕРµ С‡РёСЃР»Рѕ: ', end='')
wholeNum = int(input())
firstNum = wholeNum // 100
secondNum = (wholeNum // 10) % 10
thirdNum = wholeNum % 10
numSum = firstNum + secondNum + thirdNum
print('РЎСѓРјРјР° С†РёС„СЂ С‡РёСЃР»Р°', wholeNum, 'СЂР°РІРЅР°', numSum)
print('****************************************')

# Fourth task
print('Р’РІРµРґРёС‚Рµ СЃС‚РѕРёРјРѕСЃС‚СЊ РјСЏС‡Р° РІ СЂСѓР±Р»СЏС…: ', end='')
ruble = int(input())
print('Р� СЃ РєРѕРїРµР№РєР°РјРё: ', end='')
penny = int(input())
print('Р’РІРµРґРёС‚Рµ РєРѕР»Р»РёС‡РµСЃС‚РІРѕ РјСЏС‡РµР№ РґР»СЏ РїСЂРёРѕР±СЂРµС‚РµРЅРёСЏ: ', end='')
ballCount = int(input())
sumInPenny = (penny * ballCount) % 100
sumInRuble = (ruble * ballCount) + penny // 100
print('Р—Р°', ballCount, 'РјСЏС‡РµР№ РЅСѓР¶РЅРѕ Р·Р°РїР»Р°С‚РёС‚СЊ', sumInRuble, 'СЂСѓР±Р»РµР№', sumInPenny, 'РєРѕРїРµРµРє')
print('****************************************')

# Fifth task
print('Р’РІРµРґРёС‚Рµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЃРµРєСѓРЅРґ: ', end='')
time = int(input())
seconds = time % 60
minutes = (time // 60) % 60
hours = (time // 60) // 60
print(time, 'СЃРµРєСѓРЅРґ - СЌС‚Рѕ', hours, 'С‡Р°СЃ', minutes, 'РјРёРЅСѓС‚', seconds, 'СЃРµРє')
print('****************************************')

# Sixth task
print('Р’РІРµРґРёС‚Рµ С‡РµС‚С‹СЂРµС…Р·РЅР°С‡РµРЅРѕРµ С‡РёСЃР»Рѕ: ', end='')
wholeNum = int(input())
firstNum = wholeNum // 1000
secondNum = (wholeNum // 100) % 10
thirdNum = (wholeNum // 10) % 10
fourthNum = wholeNum % 10
maxNum = max(firstNum, secondNum, thirdNum, fourthNum)
print('РЈ С‡РёСЃР»Р°', wholeNum, 'РјР°РєСЃРёРјР°Р»СЊРЅР°СЏ С†РёС„СЂР° СЂР°РІРЅР°', maxNum)
print('****************************************')

# Seventh task
print('Р’РІРµРґРёС‚Рµ РЅР°С‚СѓСЂР°Р»СЊРЅРѕРµ С‡РёСЃР»Рѕ, РЅРµ РїСЂРµРІРѕСЃС…РѕРґСЏС‰РµРµ 1 000 000 000: ', end='')
numberStr = input()
lastNumberGroup = int(numberStr[-3:])
firstNum = lastNumberGroup // 100
secondNum = (lastNumberGroup // 10) % 10
thirdNum = lastNumberGroup % 10
numSum = firstNum + secondNum + thirdNum
print('РЎСѓРјРјР° РїРѕСЃР»РµРґРЅРёС… С‚СЂРµС… С†РёС„СЂ С‡РёСЃР»Р°', numberStr, 'СЂР°РІРЅР°', numSum)
