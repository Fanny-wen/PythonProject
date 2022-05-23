import datetime

"""
子类关系
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""
print(datetime.MAXYEAR)  # 常量: 9999
print(datetime.MINYEAR)  # 常量: 1

print("=" * 100)

print(datetime.date)  # <class 'datetime.date'>
print(datetime.date.year)  # <attribute 'year' of 'datetime.date' objects>
print(datetime.date.month)  # <attribute 'month' of 'datetime.date' objects>
print(datetime.date.day)  # <attribute 'day' of 'datetime.date' objects>

print("=" * 100)

print(datetime.time)  # <class 'datetime.time'>
print(datetime.time.hour)  # <attribute 'hour' of 'datetime.time' objects>
print(datetime.time.minute)  # <attribute 'minute' of 'datetime.time' objects>
print(datetime.time.second)  # <attribute 'second' of 'datetime.time' objects>
print(datetime.time.microsecond)  # attribute 'microsecond' of 'datetime.time' objects>
print(datetime.time.tzinfo)  # <attribute 'tzinfo' of 'datetime.time' objects>

print("=" * 100)

print(datetime.timedelta)

print("=" * 100)

print(datetime.tzinfo)

print("=" * 100)

print(datetime.timezone)
