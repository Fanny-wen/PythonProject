name_list = ['tom', 'lily', 'rose', 'wen', 'zhou', 'fan']

"""
1.修改指定下标
2.逆置:reverse()
3.排序:sort(key = None,reverse=False)
"""

# 1.修改指定下标的数据

name_list[0] = 'aaaa'  # ['aaaa', 'lily', 'rose', 'wen', 'zhou', 'fan']
print(name_list)

print('=======================')

# 2.reverse()

name_list.reverse()
print(name_list)  # ['fan', 'zhou', 'wen', 'rose', 'lily', 'aaaa']

print('=====================')

# 3.sort() 排序：升序(默认) or 降序

name_list.sort()
print(name_list)  # ['aaaa', 'fan', 'lily', 'rose', 'wen', 'zhou']

name_list.sort(reverse=True)  # ['zhou', 'wen', 'rose', 'lily', 'fan', 'aaaa']
print(name_list)
