#1. Написать функцию, которая принимает 2 числа и возвращает их сумму
# def sum(a, b):
#     c = a + b
#     return c
# print('#1 Сумма', sum(15, 5))

#2 Написать функцию, которая принимает 1 число и возвращает его произведение на 4.
# def ex_2(a):
#     c = a * 4
#     return c
# print('#2 Произведение', ex_2(10))

# #3. Написать функцию, которая принимает 3 числа, и их сумму делит на 3.
# def sumdel(a, b, c):
#     d = (a + b + c)/3
#     return d
# print('#3 Сумма/3 =', sumdel(3, 4, 5))

# #4. Написать функцию, которая не принимает аргументов, но возвращает 7.
# def none():
#     c = 7
#     return c
# print('#4 Вернуть 7 =', none())

# #5. Написать функцию, которая принимает 1 число и возвращает его остаток от деления на 5
# def qwer(a):
#     c = a % 5
#     return c
# print('#5 остаток от деления на 5=', qwer(21))

# #6. Написать функцию, которая принимает 2 числа и возвращает словарь который содержит эти 2 числа и их сумму. Ключи для чисел придумать самостоятельно.
# def lis(a, b):
#     c = {'abc': a, 'def': b, 'c': a + b}
#     return c
# print('#6 Словарь и сумма', lis(2, 10))

# #7. Написать функцию, которая принимает список, проверяет есть ли в нём число 8 или число 4. Возвращает истину или ложь.
# def sp(a):
#     c = 4 in a or 8 in a
#     return c
# print('Наличие в списке 4 и 8.... ', sp([1, 4, 66, 7]))

# #8. Написать функцию, которая принимает 2 списка и делит 2-е число первого списка на первое число второго списка. Результат деления возвращает.
# def ex81(a,b):
#     c = b/a
#     return c
# print('Результат ', ex81(12,6))
#исправленное ниже
# def ex81(a,b):
#     c = a[1]/b[0]
#     return c
# print('Результат ', ex81((12, 16),(8, 12)))

# # 9. Написать функцию. Принимает строку и заменяет в ней все пробелы на строку "privet"
# def ex9(a):
#     c = a.replace(' ', 'privet')
#     return c
# print(ex9('Vsem zdraste'))

# # 10. Написать функцию которая принимает строку и возвращает 2-е слово. Предполагается что строка содержит слова разделенные пробелом.
# def ex10(a):
#     c = a.split(' ')
#     c = c[1]
#     return c
# print('Второе слово', ex10('Первое второе третье и четвёртое'))
#
# # 11. Написать функцию принимающую список и меняет первый элемент на 4. Возвращает измененный список.
# def ex11(a):
#     a[0]=4
#     c = a
#     return c
# print('список и меняет первый элемент на 4:', ex11([1,2,3,4,5,6,7,'we']))
#
# #исправленное ниже
# def ex11(a):
#     a[0]=4
#     return a
# print('список и меняет первый элемент на 4:', ex11([1,2,3,4,5,6,7,'we']))


# # 12. Написать функцию принимающую словарь и меняет значение под ключём 'a' на 86. Возвращает измененный словарь.
# def ex12(a):
#     a['a']=86
#     c = a
#     return c
# print('меняет значение под ключём a на 86', ex12({'a':1, 'b':2, 'c':3}))
#
# # 13. Написать функцию принимающую словарь и возвращает этот же словарь но уже без ключа 'b'.
# def ex13(a):
#     del a['b']
#     c = a
#     return c
# print('возвращает этот же словарь но уже без ключа b', ex13({'a':1, 'b':2, 'c':3}))
#
# #14. Написать функцию принимающую список цифр и добавляющую ко второму элементу 33 и возвращает список.
# def ex14(a):
#     a[1] = a[1]+33
#     return a
# print('добавляющую ко второму элементу 33 и возвращает список', ex14([1,2,3,4,5]))
#
# # 15. Написать функцию принимающую список, добавить к этому списку новый элемент который будет равен сумме первого и последнего элемента этого списка.
# Получить последний элемент списка можно так: ls[-1]
# def ex15(a):
#     b = a[0]+a[-1]
#     a.append(b)
#     c = a
#     return c
# print('список 2', ex15([1,2,3,4,5]))
#
# # 16. Написать функцию принимающую словарь и добавляет к словарю ключ 'c' который содержит сумму числа под ключём 'a' и 45.
# def ex16(a):
#     b = a['a']+45
#     a['c']=b
#     c = a
#     return c
# print('добавляет к словарю ключ c который содержит сумму числа под ключём и 45', ex16({'a':1, 'b':2}))
#
# # 17. Написать функцию которая принимает список и делает первые два элемента одинаковыми.
# def ex17(a):
#     a[1] = a[0]
#     c = a
#     return c
# print('список', ex17([1,2,3,4,5]))
#
# # 18. Написать функцию которая принимает словарь и число, удаляет ключ 'a' и добавляет ключ 'c' который должен содержать значение равное этому числу.
# def ex18(a,b):
#     del a['a']
#     a['c'] = b
#     c = a, b
#     return c
# print('словарь и число', ex18({'a':1, 'b':2}, 13))
# #исправленное ниже
# def ex18(a,b):
#     del a['a']
#     a['c'] = b
#     return a
# print('словарь и число', ex18({'a':1, 'b':2}, 13))

# # 19. Написать функцию которая принимает список и возвращает список который содержит только первый и последний элемент списка.
# # Получить последний элемент списка можно так: ls[-1]
# def ex19(a):
#     b = a[0], a[-1]
#     c = b
#     return c
# print('принимает список', ex19([1,2,3,4,5,6,7,8,9]))
# #сейчас у тебя возвращает кортеж, а должен возвращать список
# #исправленное ниже
# def ex19(a):
#     x = a[0]
#     y = a[-1]
#     return [x, y]
# print('принимает список', ex19([1,2,3,4,5,6,7,8,9]))

# # 20. Написать функцию которая принимает словарь и возвращает список содержащий значения по ключам 'b' и 'm'.
# def ex20(a):
#     b = a['b']
#     m = a['m']
#     c = b, m
#     return c
# print('принимает словарь и возвращает список содержащий значения по ключам b и m', ex20({'a':1, 'b':2, 'c':3, 'd':4, 'm':5}))
# #исправленное ниже
# def ex20(a):
#     b = a['b']
#     m = a['m']
#     c = [b, m]
#     return c
# print('принимает словарь и возвращает список содержащий значения по ключам b и m', ex20({'a':1, 'b':2, 'c':3, 'd':4, 'm':5}))

# # 21. Написать функцию которая принимает число и список и добавляет его в начало списка.
# def ex21(a, b):   #проверено
#     x = [a]
#     c = x + b
#     return c
# print('добавляет его в начало списка', ex21(12, [1, 2, 3, 4, 5, 6]))
#
# # 22. Написать функцию принимающую строку, состоящую из слов разделенных пробелами.
# #Функция должна возвращать сколько в строке слов.
# def ex22(a):
#     b = a.split(' ')
#     c = len(b)
#     return c
# print('В строке слов =', ex22('Функция должна возвращать сколько в строке слов'))
#
#
#
# #23. Написать функцию принимающую строку состоящую ровно из двух слов, разделенных пробелом.
# #Функция должна возвращать строку аналогичную входящей, но только слова должны поменяться местами.
# #Пример:
# #>>> fn("республика беларусь")
# #"беларусь республика"
#
# def ex23(a):
#     b = a.split(' ')
#     c = b[1]+' '+b[0]
#     return c
# print('Наоборот=', ex23('Республика Беларусь'))
#
# print('END')
# проверено