import pandas
info = pandas.read_csv("C:/Users/alexey/PycharmProjects/info.csv")
marks = pandas.read_csv("C:/Users/alexey/PycharmProjects/marks.csv")

# 1. Узнайте для скольких людей из датафрейма info неизвестны оценки.
# Подсказка: нужно использовать 1 merge некоторого типа и .shape

x = marks.merge(info, left_on='id2', right_on='id')
print(x.shape[0])   # сколько с оценками
print(info.shape[0] - x.shape[0])

