# Создать файл с следующим содержимым
import random
#
def some_fn(a, b):
    c = a + b
    x = random.randint(1, 100)
    return c / x

def some_fn2(a):
    c = a ** 3
    z = c / random.randint(1, 100)
    return z

m = random.randint(1, 100)
k = random.randint(1, 100)
y = some_fn(m, k)
d = some_fn2(y)
y = y + 1
print("y ravno " + str(y))
#
# С помощью дебагера затйти в функции (нажав F7) some_fn и some_fn2 просмотрев как в них изменяются переменные.
#
# 2. Создать файл с следующим содержимым
# def fucktorial(x):
#     if x == 0:
#         return 1
#     else:
#         y = fucktorial(x - 1)
#         z = x * y
#         return z
#
# print(fucktorial(3))
#
# С помощью дебагера затйти рекурсивную в функцию  (нажав F7) просмотрев как в ней изменяются переменные.
#
# 3. Создать файл с следующим содержимым
# def reduce(fn, ls, acc):
#     if len(ls) == 0:
#         return acc
#     else:
#         new_acc = fn(ls[0], acc)
#         ls_without_first_element = ls[1:]
#         result = reduce(fn, ls_without_first_element, new_acc)
#         return result
# reduce((2,3),(4, 3), 3)
# Вызвать функцию reduce на каких-нибудь аргументах.
# С помощью дебагера зайти рекурсивную в функцию (нажав F7) просмотрев как в ней изменяются переменные.
