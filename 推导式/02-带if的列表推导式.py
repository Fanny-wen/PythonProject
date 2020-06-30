"""
需求：创建0-10的偶数列表
"""
# 方法一：range()步长实现

list1 = [i for i in range(0, 10, 2)]
print(list1)  # [0, 2, 4, 6, 8]


# 方法二：if 实现

list2 = [i for i in range(10) if i % 2 == 0]
print(list2)  # [0, 2, 4, 6, 8]
