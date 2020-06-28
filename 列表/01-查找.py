# 下标
name_list = ['tom', 'lily', 'rose']
print(name_list)
print(name_list[0])  # 'tom'

print('=============================')
# 函数
"""
1.index(数据,开始位置下标,结束位置下标)   返回指定数据所在位置的下标
2.count(数据,开始位置下标,结束位置下标)   统计指定数据在当前列表中出现的次数
3.len()  访问列表长度，即列表中数据的个数
"""

print(name_list.index('tom'))  # 0

print(name_list.count('tom'))
print(name_list.count('toms'))  # 0 数据不存在，所以出现次数为0

print(len(name_list))  # 3
