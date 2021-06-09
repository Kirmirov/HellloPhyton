# First Task
import math

def get_digital_product(numberOne, numberTwo):

    def get_count_rank (number):
        count = 0
        while number > 0:
            number //= 10
            count += 1
        return count

    return get_count_rank(numberOne) * get_count_rank(numberTwo)

print(get_digital_product(1995, 243))

# Second Task

def get_product_two_numb(listOne, listTwo):

    def get_max_numb(list):
        neg_infinity = -math.inf
        max_numb = neg_infinity
        for numb in list:
            if numb > max_numb:
                max_numb = numb
        return max_numb
    
    return get_max_numb(listOne) * get_max_numb(listTwo)

first_list = [1, 3, 22, 13]
second_list = [2, 5, 4, 9]

print(get_product_two_numb(first_list, second_list))

# Third Task

def get_days_in_month(number_of_month):
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month_list[number_of_month - 1]

print(get_days_in_month(2))
print(get_days_in_month(6))
print(get_days_in_month(12))

# Fourth Task
def get_price_of_dellivery(goods_count):
    return goods_count * 50 + 50

print(get_price_of_dellivery(2))
print(get_price_of_dellivery(1))

# Fifth Task

def is_star_date(date):
    split_date = date.split('.')
    day = int(split_date[0])
    month = int(split_date[1])
    last_numb_of_year = int(split_date[2]) % 100
    if day * month == last_numb_of_year:
        return True
    else:
        return False

print(is_star_date("10.06.1960"))
print(is_star_date("20.07.1960"))


