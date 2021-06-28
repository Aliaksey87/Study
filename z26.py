# 1. Импортировать 2-мя способами функции стандартной библиотеки:
#    statistics.mean
#    math.factorial
#    json.dumps
#    json.loads
#    Понять что они делают (погуглив), повызывать к какими-нибудь аргументами.

# from functools import reduce
# reduce(lambda x, y: x + y,[2, 3,4, 5], 0)

# from statistics import mean
# print(mean([1,2,3,4,5]))               # считает среднее
# import statistics
# print(statistics.mean([1,2,3,4,5]))    # считает среднее
#
# from math import factorial
# print(factorial(5))                    # 1*2*3*4*5
# import math
# print(factorial(5))                    # 1*2*3*4*5

# from json import dumps
# x = dumps([1, 2, 3, 4, 5])     # выводит всё строкой
# print(x[0])
# import json
# print(json.loads(x)[0])         # выводит всё списком



# from json import loads
# y = loads(x)
# print(y[0])
# from json
# print(json.loads("foo", {"bar": ["baz", null, 1.0, 2]}))

from json import loads
# print(loads(x[0,2]))


# 2. Установить с помощью pip библиотеку Jinja2 версии 2.9.3
# Проверить что библиотека установлена можно импортировав:
#        from jinja2 import Environment


