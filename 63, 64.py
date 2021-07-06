import time
import random
from datetime import datetime
from functools import partial

# x = 'abc'
# def fn(y):
#     y[0] = 'm'
# fn(x)
# print(x)

# x = 7
# print(x)
# def fn(y):
#     y = 8
# fn(x)
# print(x)


# x = [1,3,4]
# def fn(y):
#     y[0] = 25
# fn(x)
# print(x)

# x = 44
# print(x)
# def fn(y):
#     y = 2*x
#     return y
# fn(x)
# print(x)

# x = [1,2,3,4,5]
# # a = x[0]
# # b = x[1]
# a,b = x
# print(a + b)

# ls = [([4, 2], 5), [[7, 3], 6]]
# for (_, x), y  in ls:
#     print(x + y)

# Написать функцию которая будет распаковывать цифры 7 и 6 в переменные x и y из списка
# ls = [4,[7,8],6]    Использовать unboxing.
# ls = [4,[7,8],6]
# (_,(a,_),b) = ls
# print(a,b)
# print(ls)

# Написать функцию которая будет бежать for-ом по списку  ls = [ (3, [9, 1]), [(23,43), [5, 4]] ]
# и суммировать элементы 9 и 5 используя unboxing.
# ls = [ (3, [9, 1]), [(23,43), [5, 4]]]
# sum = 0
# for (_,(x,_)) in ls:
#     sum+=x
# print(sum)


# Генератор
# def plus5(z):                                   # функция №1, принимает значение переменной z
#     print('Вычисляем: ' + str(z))               # печатает значение у
#     time.sleep(1)                               # задержка во времени
#     return z + 2                                # возвращает из функции
#
# def lazy_map(fn, ls):                           # функция lazy_map, принимает fn - функция plus5 - return z + 2, ls - range(1000000)
#     for x in ls:                                # проходит по значениям из списка ls
#         y = fn(x)                               # записывает в у значение из ls под индексом х
#         yield y                                 # возвращает из функции
#
# start = datetime.now()                          # начало подсчёта времени
# generator = lazy_map(plus5, range(10))           # запускается generator, она же lazy_map c переменными plus5(то что вернёт эта функция return z + 2 ) и range(1000000)(генератор от 1 до 999999)
# print(next(generator))                          # запускаем фунцию generator и печатаем результат
# print(next(generator))                          # запускаем фунцию generator и печатаем результат
# print(next(generator))                          # запускаем фунцию generator и печатаем результат
# print(next(generator))                          # запускаем фунцию generator и печатаем результат
# print(next(generator))                          # запускаем фунцию generator и печатаем результат
# print("Программа выполнилась за " + str((datetime.now() - start). total_seconds()) + " секунд")






# Итератор
# import time
# from datetime import datetime
# def plus5(z):
# print('Heavy computing: 1 + str(z))
# time.sleep(l)
# return z + 5
# class lazyMmap:
# def	(self, fn, Is):
# self.fn = fn self.idx = 0 self.Is = Is
# def	(self):
# return self
# def	(self):
# if self.idx > len(self.Is): raise StopIteration() else:
# val = self.fn(self.ls[self.idx]) self.idx = self.idx + 1 •	return val
# start = datetime.now()
# iterator = lazy map(plus5, [3Л4Х5Х6])
# print(next(iterator))
# print(next(iterator))
# print("Программа выполнилась за " +
# str((datetime.now() - start).total seconds()) + " секунд"!


# 65.Сделать генератор который принимает на вход число x, пусть x = 5, и возвращает 5 разных
# простых чисел.
# Простое число: число которое делится только на себя и на 1.

# Запустить генератор подав на вход 1 000 000, и сгенерировать с его помощью 6 простых чисел.

# Простое число - имеющее ровно два различных натуральных делителя — единицу и самого себя. Другими словами,
# число является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x

def plus5(z):                                   # функция №1, принимает значение переменной z
    print('Вычисляем число №' + str(z))         # печатает значение у
    time.sleep(1)                               # задержка во времени
    return z + 1                                # возвращает из функции

def lazy_map(fn, ls):                           # функция lazy_map, принимает fn - функция plus5 - return z + 2, ls - range(1000000)
    for x in ls:                                # проходит по значениям из списка ls
        y = fn(x)                               # записывает в у значение из ls под индексом х
        yield y                                 # возвращает из функции

start = datetime.now()                          # начало подсчёта времени
generator = lazy_map(plus5, range(10))           # запускается generator, она же lazy_map c переменными plus5(то что вернёт эта функция return z + 2 ) и range(1000000)(генератор от 1 до 999999)
print(next(generator))                          # запускаем фунцию generator и печатаем результат
print(next(generator))                          # запускаем фунцию generator и печатаем результат
print(next(generator))                          # запускаем фунцию generator и печатаем результат
print(next(generator))                          # запускаем фунцию generator и печатаем результат
print(next(generator))                          # запускаем фунцию generator и печатаем результат
print("Программа выполнилась за " + str((datetime.now() - start). total_seconds()) + " секунд")


def ex777():
    random.randint(1, 150)
    x = int(input('Введите число: '))         # вводим число
    w = 0                                     # переменная для подсчёта
    y = x                                     # переменная для деления
    for x in range(1, x+1):                   # перебираем от 1 до х
        q = y % x                             # вычисляем остаток
        if q == 0:                            # сравниваем остаток с 0
            w += 1                            # если делится без остатка, то добавляем 1
    if w == 2:                                # если набралось 2 еденицы, то число натуральное
        return 'True'
    else:
        return 'False'
print(ex777())


# def fn(a):
#     founds_nams = 0
#     last_prime = 1
#     while founds_nams != a:
#         prime = True
#         for y in range(2, last_prime):
#             if last_prime % y != 0:
#                 prime = False
#                 break
#         if prime:
#             founds_nams += 1
#             yield last_prime
#         last_prime+=1
#     print(last_prime)


# Карирование (Сurrying) == Частичное применение (Partial application)
# def fn(a,b):
#     return a + b
# fn2 = partial (fn, 3)
# print(fn2)
# print(fn2(5))

# Z66. 1. Найти функцию которая принимает несколько аргументов.
#    - С помощью partial передать часть (не все) аргументы в найденную функцию создав новую.
#    - Передать остаток аргументов получив результат вычисления
# 11.2 Написать функцию, которая принимает 2 числа а затем умножает их друг на друга. Нельзя пользоваться *.
# Подсказка: в python есть функция list(range(4)) которая вернёт список вида [0, 1, 2, 3]
# def fn(x, y):
#     c = 0
#     a = x
#     b = y
#     for a in range(x):
#         # print(x)
#         for b in range(y):
#             # print(x, y)
#             c = c + 1
#     return c
# fn2 = partial (fn, 3)      # тут принимается x = 3 и не меняется на всём протяжении программы
# print(fn2)
# print(fn2(5))
# print(fn2(7))
# print(fn2(10))
# готово



