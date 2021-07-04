import datetime

a = datetime.datetime.today() + datetime.timedelta(days = 7)
print(a)
b = '2021-06-23 00:00:00+00:00'
c = datetime.datetime.strptime(b[0:-6], '%Y-%m-%d %H:%M:%S')
# c = datetime.datetime.s
print(c)