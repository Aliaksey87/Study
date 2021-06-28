import requests
import json
from datetime import datetime, date, time, timedelta

s1 = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate='
s2 = str(date.today() - timedelta(days=6))           # начальная дата (7 дней назад)
s3 = '&endDate='
s4 = str(date.today())                               # конечная дата (сегодня)
s = (s1 + s2 + s3 + s4)                              # url в сборе
print(s)
respons = requests.get (
    s
)
data = json.loads(respons.text)
a = []
for x in data:
    a.append(x['Cur_OfficialRate'])
x = round(sum(a)/len(a), 4)
print(x)


# s = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=', d1,'&endDate=date2'



# s = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=date1&endDate=date2'
# print(s)
# s1 = s.replace('date1', d1)
# s1 = s1.replace('date2', в2)
# print(s1)

# respons = requests.get (
#     s
#     # 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2021-6-22&endDate=2021-6-28'
#     # 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2021-6-22&endDate=2021-6-28'
# )
# data = json.loads(respons.text)
# print(data)
# a = []
# for x in data:
#     # print(x['Cur_OfficialRate'])
#     a.append(x['Cur_OfficialRate'])
# # print(a)
# x = sum(a)/len(a)
# print(x)

# print(datetime.now())
# print(datetime.now(tz=None))
#

