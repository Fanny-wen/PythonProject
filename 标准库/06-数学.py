"""
math模块提供了对浮点数学的底层C库函数的访问
random模块提供了进行随机选择的工具
statistics模块计算数值数据的基本统计属性(均值，中位数，方差等)
"""

import math

print(math.cos(math.pi / 4))  # 0.7071067811865476

print(math.log(1024, 2))  # 10.0

import random

print(random.choice(['apple', 'pear', 'banana']))

print(random.sample(range(100), 10))

print(random.randrange(6))

import statistics

data = [2.123, 13.51, 231, 4.1, 431.1]
print(statistics.mean(data))  # 136.3666
print(statistics.median(data))
print(statistics.variance(data))