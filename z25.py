print(list(map(lambda x: x * x, [4,5,6])))


# 1. Напишите функцию которая принимает список чисел и прибавляет к каждому 100. Нужно использовать map и lambda.
print(list(map(lambda x: x+100, [1, 2, 3, 4])))

# 2. Написать функцию, которая принимает список чисел и возвращает список только нечётных чисел. Использовать filter и lambda.
print(list(filter(lambda x: x%2 ==0, [1, 2, 3, 4, 5, 6, 7])))

