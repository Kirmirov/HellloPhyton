# -- coding: utf-8
import random

def pass_generator():
    
    def ask_options(option_text):
        while True:
            print(option_text)
            answer = input()
            if answer.isdigit():
                break
            else:
                print('Введите число')
        return int(answer)

    def ask_question(question_text):
        while True:
            print(question_text, 'Y or N?')
            answer = input()
            if answer == 'Y' or answer == 'N':
                break
            else:
                print('Ответ не верный!')
        if answer == 'Y':
            return True
        else:
           return False

    def get_pass(pass_length, enable_chars):
        password = ''
        for i in range(pass_length):
            random_index = random.randint(0, len(enable_chars) - 1)
            password += enable_chars[random_index]
        print('Ваш', 'пароль:', password)


    print('Вас приветсвует генератор паролей!')
    password_count = ask_options('Укажите сколько паролей выхотите сгенерировать:')
    pass_length = ask_options('Введите длинну желаемых паролей:')

    latin_lowercase_enable = ask_question('Пароль должен включать прописные латинские буквы?')
    latin_uppercase_enable = ask_question('Пароль должен включать заглавные латинские буквы?')
    russian_lowercase_enable = ask_question('Пароль должен включать прописные русские буквы?')
    russian_uppercase_enable = ask_question('Пароль должен включать заглавные русские буквы?')
    digits_enable = ask_question('Пароль должен включать цифры?')
    punctuations_enable = ask_question('Пароль должен включать знаки пункуации?')

    enable_chars=''

    latin_lowercase_letters='abcdefghijklmnopqrstuvwxyz'
    latin_uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian_lowercase_letters='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    russian_uppercase_letters='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    digits='0123456789'
    punctuations='.,?!-:;""()[]/\\&#$@%*_=+`'

    if latin_lowercase_enable:
        enable_chars += latin_lowercase_letters

    if latin_uppercase_enable:
        enable_chars += latin_uppercase_letters

    if russian_lowercase_enable:
        enable_chars += russian_lowercase_letters

    if russian_uppercase_enable:
        enable_chars += russian_uppercase_letters

    if digits_enable:
        enable_chars += digits

    if punctuations_enable:
        enable_chars += punctuations
        
    while int(password_count) > 0:
        get_pass(int(pass_length), enable_chars)
        password_count -= 1

    is_resume = ask_question('Желаете продолжить работу?')
    if is_resume:
        pass_generator()
    else:
        return

pass_generator()


