"""
datetime模块提供了以简单和复杂的方式操作日期和时间的类
"""

from datetime import date

now = date.today()
print(now)  # 2020-07-08

import datetime

print(datetime.datetime(1341, 12, 12))  # 1341-12-12 00:00:00

print(date(1231, 2, 21))  # 1231-02-21

print(datetime.time(12, 4, 1))  # 12:04:01
