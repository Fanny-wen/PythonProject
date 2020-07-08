"""
filter
map
reduce
lambda
"""
# 1.lambda
numbers = range(10)
lam = lambda x: x + 3
n1 = []
for i in numbers:
    n1.append(lam(i))
print(n1)  # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
lambda使用方法：
    ·在lamnda后面直接跟变量
    ·变量后面是冒号
    ·冒号后面是表达式，表达式计算结果就是本函数的返回值
    注意：lambda函数不能包含命令，包含的表达式不能超过一个。
"""

# 2. map
"""
map(func,seq)   func是一个函数，seq是一个序列对象.在执行的时候，序列对象中的每个元素，按照从左到右的顺序，一次被取出来，并塞入到func那个函数里面，并将func的返回值依次存到一个list中。
"""
l1 = map(lambda x: x + 3, numbers)
print(list(l1))  # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l2 = map(lambda x, y, z: x + y + z, [1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [7, 8, 9, 2, 1])
print(list(l2))  # [14, 17, 20, 15, 6]

# 3.reduce
from functools import reduce

r1 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])
print(r1)  # 21

# 4.filter  filter(func,iterable)

num2 = range(-5, 5)
f1 = filter(lambda x: x > 0, num2)
print(list(f1))  # [1, 2, 3, 4]
