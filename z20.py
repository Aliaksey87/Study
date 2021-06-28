# 1. Написать функцию которая принимает нефиксированное количество обязательных аргументов и суммирует их.
# def ex_1(*a):
#     c = 0
#     for x in a:
#         c = c + x
#     return c
# print(ex_1(1, 2, 3, 4, 5))


def ex_1(*a):
    x = sum(a)
    return x
z = (1,2,3,4,5)
# print(ex_1(*z))

def ex_11(a, b):
    # x = sum(a)
    return a + b
z = (1,2)
# print(ex_11(*z))
# проверено

# 2. Пробежать по значениям словаря можно так:
#    d = {'a': 1, 'b': 22}
#    for x in d.values():
#        print(x)
#    --------------------
#    1
#    22
#    Написать функцию которая принимает нефиксированное количество необязательных аргументов и перемножает их.

def ex_2(**a):
    for x in a.values():
        print(x)
    return
ex_2({'a': 1, 'b': 22, 'c': 33})



# def ex_2():
#     d = {'a': 1, 'b': 22}
#        for x in d.values():
#              print(x)
# print(ex_2({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
# print(ex_2(1, 2, 3, 4))
# ex_2()

# def fn(a, b, c=2, d=3):               # это пример
#     return a + b + c + d
# required_args = (1, 7)
# default_args = {'c': 5, 'd': 2}
# print(fn(*required_args, **default_args))



