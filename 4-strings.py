# -*- coding: utf-8 -*-

# First task
print('Введите число: ', end='')
number = input()
print('В введенном числе', len(number), 'цифр')

print('****************************************')

# Second task
print('Введите текст: ', end='')
text = input()

if 'Glo Academy' in text:
    print('YES')
else:
    print('NO')
    
print('****************************************')

# Third task
print('Введите название первой статьи: ', end='')
artOne = input()
print('Введите название второй статьи: ', end='')
artTwo = input()
print('Введите название третьей статьи: ', end='')
artThree = input()

lenArtOne = len(artOne)
lenArtTwo = len(artTwo)
lenArtThree = len(artThree)

maxArt = max(lenArtOne, lenArtTwo, lenArtThree)

if maxArt == lenArtOne:
    print(artOne)
elif maxArt == lenArtTwo:
    print(artTwo)
else:
    print(artThree)    

print('****************************************')

# Fourth task
print('Введите название команды: ', end='')
teamName = input()
print(teamName * 5)

print('****************************************')

# Fifth task
print('Введите email: ', end='')
email = input()

if '@' in email:
    print('Корректный')
else:
    print('Некорректный')