import pandas
df = pandas.read_csv('C:/Users/alexey/PycharmProjects/titanic.csv')
# 1. Распечатайте колонки которые есть датафрейме.
# print(df.columns)

# 2. Узнайте сколько людей было на борту
# print(df.shape[0])                              # 891

# 3. Узнайте сколько на борту было мужчин.
# print(df[(df['Sex'] == 'male')].shape[0])

# 4. Посчитайте процент выживших на борту.
# (количество выживших / общее количество)*100
# print(df[(df['Survived'] == 1)].shape[0])
# a = df[(df['Survived'] == 1)].shape[0]            # количество выживших
# b = df.shape[0]                                   # сколько людей было на борту
# print('процент выживших на борту', ((a/b)*100), '%')

# shape[0]   количество строк
# shape[1]   количество колонок

# 5. Кого было больше на борту, мужчин или женщин ?
print(df[(df['Sex'] == 'male')].shape[0])             # кол муж
print(df[(df['Sex'] == 'female')].shape[0])             # кол жен
a = df[(df['Sex'] == 'male')].shape[0]             # кол муж
b = df[(df['Sex'] == 'female')].shape[0]             # кол жен
if

# 6. Посчитайте сколько процентов из выживших были мужчинами?

# 7. Человек какого класса вероятнее всего не выжил ?
#