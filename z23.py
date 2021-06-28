
# 1. Создайте класс "здание". Придумайте для его 1 свойство и 1 метод.
#    Отнаследуйте от его классы "торговый центр" и "школа".
#    Для классов "торговый центр" и "школа" придумайте 1 дополнительное свойство
#    и 1 дополнительный метод.
#    Создайте объекты всех 3-х классов. Посмотрите их свойства, повызывайте
#    их методы.
class zd:
    def __init__(self, floor):
        self.floor = floor
    def zd1(self, anyfloor):
        self.floor = self.floor + anyfloor


class tc(zd):
    def __init__(self, floor, color):
        self.color = color
        super().__init__(floor)
    def tc1(self, anycolor):
        self.color = anycolor


class sc(zd):
    def __init__(self, floor, kol):
        self.kol = kol
        super().__init__(floor)
    def sc1(self, anykol):
        self.kol = anykol

#
# zd11 = zd(4)
# print(zd11.floor)
# tc11 = tc(7, 'red')
# print(tc11.color, tc11.floor)
# sc11 = sc(10, 500)
# print(sc11.floor, sc11.kol)
# zd11.zd1(5)
# print(zd11.floor)
# tc11.tc1('white')
# print(tc11.color)
# sc11.sc1('511')
# print(sc11.kol)
# sc11.zd1(2)
# print(sc11.floor)
# проверено


# 2. Создайте класс Factorial у которого должен быть метод calculate,
# принимающий число и считающий факториал для числа.
#    Например факториал для числа 5 = 1 * 2 * 3 * 4 * 5 = 120.
#    Всю логику расчёта поместите в инкапсулированный метод который
#    будет вызываться внутри метода calculate.
#    Создайте объект класса Factorial и поробуйте вызвать
#    инкапсулированный метод и метод calculate.
class Factorial():
    def __factorial(self, a):              # тут решает
        x = 1
        self.y = 1
        for a in range(a):
            self.y = self.y * x
            x = x + 1
        return self.y
    def calculate(self, a):
        y = self.__factorial(a)
        return y                          # тут выводит
# c1 = Factorial()
# print(c1.calculate(5))
# проверено

# 3. Создайте класс "банк". У банка должно быть свойство - депозиты (список чисел отражающий депозиты людей
#    в банке). Создайте метод + для класса, который должен суммировать банки и как результат создавать новый банк
#    с депозитами исходных банков.
#    Создайте 2 объекта класса "банк". Сложите их. Посмотрите депозиты нового банка.
#
# class Bank:
#    def __init__(self, deposits):
#       ...
#
# alfabank = Bank([32,4,54,65])
# bsb_bank = Bank([56,23,11])
#
# new_bank = alfabank + bsb_bank
# print(new_bank.deposits)
#
# должно напечатать [32,4,54,65, 56,23,11]

# class bank():
#     def __init__(self, deposits):
#






