import time
from datetime import date

birthday = date(year=1998, month=6, day=29)
print(birthday)  # 1998-06-29

today = date.today()  # 等价于 date.fromtimestamp(time.time())
print(today)  # 2021-06-29
print(today)  # 2021-06-29
print(today - birthday)  # 8401 days, 0:00:00

print(date.fromtimestamp(time.time()))  # 返回对应于 POSIX 时间戳的当地时间, time.time() 返回的就是时间戳

print("=" * 100)

print(date.max.toordinal())  # 3652059
print(date.min.toordinal())  # 3652059
print(date.min)  # 0001-01-01
print(date.max)  # 9999-12-31

print(date.fromordinal(1))  # 0001-01-01, 1=<ordinal<=date.max.toordinal()
