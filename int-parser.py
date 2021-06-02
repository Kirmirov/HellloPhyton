# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
# адрес сайта, предназначение (r -reading), кодировка
file = open('for_parsing.html', 'r', encoding='utf-8')
# метод куфв считывает содержимое
data = file.read()
# закрываем соединение с файлом
file.close()
# Передаем в библиотеку файл и название разборщика файла
soup = BeautifulSoup(data, 'lxml')

a_tags_list = soup.findAll('a')
for a_tag in a_tags_list:
    print(a_tag.text)

li_tags_list = soup.findAll('li')
for li_tag in li_tags_list:
    print(li_tag.text)