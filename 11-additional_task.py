# -- coding: utf-8 
import random

def auto_game():
    print('Приветствуем Вас в игре "Машина угадывает число"!')
    print('Укажите максимальную границу для поиска случайного числа:', end=' ')
    search_start = 1
    search_end = int(input())
    print('Загадайте число! И запишите на бумаге!')  

    while True:
        comp_number = random.randint(search_start, search_end)
        print('Вы загадали число', comp_number, '? ДА, БОЛЬШЕ, МЕНЬШЕ ?')
        player_input = input()
        if player_input == 'ДА':
            print('Слава роботам! Это было легко!')
            break
        elif search_start == search_end:
            print('Врать не хорошо!')
            break
        elif player_input == 'БОЛЬШЕ':
            print('Продолжаю поиск!')
            search_start = comp_number + 1
            continue
        elif player_input == 'МЕНЬШЕ':
            print('Продолжаю поиск!')
            search_end = comp_number - 1
            continue
auto_game()