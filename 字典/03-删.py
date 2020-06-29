"""
del()/del:删除字典或者删除字典中指定键值对
clear():清空字典
"""

dict1 = {'name': 'TOM', 'age': 24, 'gender': '男'}

# del 删除字典或指定键值对

# del dict1
# print(dict1) NameError: name 'dict1' is not defined

del dict1['name']
print(dict1)  # {'age': 24, 'gender': '男'}

# del dict1['name']  # KeyError: 'name'

# clear()

dict1.clear()
print(dict1)
