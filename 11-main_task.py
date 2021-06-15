# -- coding: utf-8 
import random

def start_game():
    print('Приветствуем Вас в игре "Угадай Число"!')
    print('Укажите границу для выбора случайного числа:', end=' ')
    search_boundary = int(input())
    secret_number = random.randint(1, search_boundary)
    print(secret_number)  # For test
    attepts_count = 10

    def is_valid(player_input):
        if player_input.isdigit():
            player_number = int(player_input)
            if 1 <= player_number <= search_boundary:
                return True
            else:
                return False
        else:
            return False         

    def get_min_count(max_number):
        count = 0
        while max_number != 0:
            max_number //= 2
            count += 1
        return count

    while True:
        if attepts_count == 0:
            print('Попытки закончились! Вы проиграли!')
            break
        print('Введите число от 1 до', search_boundary, ': ', end=' ')
        player_input = input()
        if not is_valid(player_input):
            print('Введено не верное значение!')
            continue
        else:
            player_number = int(player_input)
            attepts_count -= 1
            if player_number == secret_number:
                print('Поздравляю! Вы угадали! Вам понадобилось', 10 - attepts_count, 'попыток! Минимальное количество попыток за которое можно было угадать число равно', get_min_count(search_boundary))
                break
            elif player_number < secret_number:
                print('Загаданное число больше!')
                continue
            elif player_number > secret_number:
                print('Загаданное число меньше!')
                continue
    start_game()

start_game()