"""
元组数据不支持修改，只支持查找
1.index():查找某个数据，如果数据存在返回对应下标，否则报错，语法和列表、字符串的index方法相同
2.count():统计某个数据在当前元组出现的次数
3.len():
"""

t1 = (1, 2, 3, 4, 5, 6)

# 1.下标
print(t1[1])  # 2

# 2.index()
print(t1.index(2))  # 1

# 3.count()
print(t1.count(1))  # 1
print(t1.count(11))  # 0 不存在

# 4.len()
print(len(t1))  # 6
