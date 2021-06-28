# 1. Создайте класс выражающий существительное "человек".
# Создайте 2 объекта этого класса, посмотрите их свойства.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
class human:
    def __init__(self, height, color, age):
        self.height = height
        self.color = color
        self.age = age
human1 = human('190', 'black', '22')
human2 = human('200', 'white', '43')
# print('human2', human1.height)
# print('human2', human2.color)
# print('human2', human2.age)
# print('human1', human1.__dict__)
# print('human2', human2.__dict__)


# 2. Создайте класс выражающий существительное "дерево"
# Создайте 2 объекта этого класса, посмотрите их свойства.
class wood:
    def __init__(self, color, height, halfheight):
        self.color = color
        self.height = height
        self.halfheight = height*2
wood1 = wood('white', '100', '101')
wood2 = wood('black', '200', '201')
wood3 = wood('silver', '300', '301')
# print('wood1', wood1.color, wood1.height)
# print('wood2', wood2.color, wood2.halfheight)
# print('wood3', wood3.color)


# 3. Создайте класс выражающий существительное "дом"
# Создайте 2 объекта этого класса, посмотрите их свойства.
class house:
    def __init__(self, color, m2, floor):
        self.color = color
        self.m2 = m2
        self.floor = floor
house1 = house('white', '75', '1')
house2 = house('black', '100', '2')
house3 = house('silver', '125', '3')
# print('house1', house1.color, house1.m2, house1.floor)
# print('house3', house3.color, house3.m2, house2.floor)


# 4. Создайте класс выражающий существительное "книга"
# Создайте 2 объекта этого класса, посмотрите их свойства.
class book:
    def __init__(self, color, lists, year):
        self.color = color
        self.lists = lists
        self.year = year
book1 = book('white', '75', '2001')
book2 = book('black', '100', '2002')
book3 = book('silver', '125', '2003')
# print('book1', book1.color, book1.lists, book1.year)
# print('book3', book3.color, book3.lists, book2.year)


# 5. Создайте класс выражающий существительное "дата"
# Создайте 2 объекта этого класса, посмотрите их свойства.
class date:
    def __init__(self, day, mes, year):
        self.day = day
        self.mes = mes
        self.year = year
date1 = date(13, 5, 2001)
date2 = date(7, 6, 2002)
print('date1', date1.day, date1.mes, date1.year)


# 6.  Создайте класс выражающий словосочетание "конверт с письмом"
# Создайте 2 объекта этого класса, посмотрите их свойства.
