"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
import datetime

sample1 = 'Jan 1 2014 2:43PM'
dt1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(dt1)
sample2 = '14:20 10/12/22'  # YY/MM/DD
dt2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(dt2)
sample3 = 'Tuesday, September 24, 2019'
dt3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(dt3)
sample4 = '01.01.1970 - 00:00:01'
dt4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(dt4)




# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
tdelta = datetime.timedelta(days=1)
print('Yesterday:', today - tdelta)
print('Today:', today)
print('Tommorow:', today + tdelta)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
dt = datetime.datetime.fromtimestamp(some_day).strftime('%d.%m.%Y')
print(dt)


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
def two_weeks_ago(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    tdelta = datetime.timedelta(weeks=2)
    return (dt - tdelta).timestamp()

print(two_weeks_ago(1014163200))