# 10. Написать функцию, которая принимает 2 списка чисел и возвращает их общие элементы.
# Пример вызова:
#  fn([1,2,3,4], [5,7, 2, 88, 3])
# [2, 3]
def ex_10(a,b):
    c = []
    for x in a:
        for y in b:
            if x == y:
                c.append(y)
    return c
print(ex_10([1,2,3,4], [5,7, 2, 88, 3]))

