"""
1.del 目标:可以删除指定下标的数据
2.pop():删除指定下标的数据，如果不指定下标，默认删除最后一个数据，无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
3.remove():移除列表中某个数据的第一个匹配项
4.clear():清空列表
"""

name_list = ['tom', 'lily', 'rose', 'wen', 'zhou', 'fan']

# del
"""
del name_list
print(name_list)   
NameError: name 'name_list' is not defined
"""
del name_list[0]
print(name_list)  # ['lily', 'rose']

print('======================')

# pop():

del_name = name_list.pop(0)
print(del_name)  # lily
print(name_list)  # ['rose']

print('======================')

# remove():

name_list.remove('rose')

print(name_list)  # ['wen', 'zhou', 'fan']

print('===============')

# clear():

name_list.clear()
print(name_list)
