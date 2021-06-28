# def print_args_and_result(fn):
#     def wrapper(*args, **kwargs):
#         print("Входящие аргументы:")
#         for arg in args:
#             print(str(arg))
#         result = fn(*args, **kwargs)
#         print("Выходящее значение:")
#         print(str(result))
#         return result
#     return wrapper
# @print_args_and_result
# def test(a, b):
#     return (a + b) / 2
# test(25, 12)



# 1. Оберните функцию
# def swap_words(words):
#     tmp = words.split(' ')
#     return tmp[1] + ' ' + tmp[0]
#
# декоратором который первую букву у выходящего значения делает большой.
# Сделать строке первую букву большой можно так:
# >>> 'коля'.capitalize()
# 'Коля'
#
# @my_decorator
# def swap_words(words):
#     tmp = words.split(' ')
#     return tmp[1] + ' ' + tmp[0]
#
# swap_words(“привет мир”)
# “Мир привет”

# Повызывайте обёрнутую функцию.


def my_decorator(fn):
    def capitalize(a):
        x = fn(a)                      # fn это swap_words
        y = x.capitalize()
        return y
    return capitalize
@my_decorator
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]
# print(swap_words("мир привет"))
# проверено

# “Мир привет”



# 2. Оберните функцию
# def mult_on_2(ls):
#     result = []
#     for x in ls:
#         result.append(x * 2)
#     return result
#
# декоратором который применяет функцию 2 раза к аргументам.
# Повызывайте обёрнутую функцию.

def mult(ls2):
    result_2 = []
    for x in ls2:                 #
        result_2.append(x * 2)
    return result_2
@mult
def mult_on_2(ls):                #
    result = []
    for x in ls:
        result.append(x * 2)
    return result
# print(mult_on_2([2, 4, 6, 22]))
# не работает


# 3. Оберните функцию
# import math
#
# def my_sqrt(x):
#     return math.sqrt(x)
#
# декоратором который проверяет является ли аргумент отрицательным и если это так, печатает "Нельзя передавать отрицательные числа"
# и возвращает -1. Если аргумент позитивный, то просто передаёт его в функцию.
#
# Повызывайте обёрнутую функцию с положительными и отрицательными числами.
