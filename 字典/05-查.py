"""
1.key值查找
2.get(key,默认值): 如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None
3.keys():查找字典中所有的key，返回可迭代对象
4.values():查找字典中所有的value，返回可迭代对象
5.items():查找字典中所有的键值对，返回可迭代对象
"""
# 1. [key]
dict1 = {'name': 'TOM', 'age': 24, 'gender': '男'}
print(dict1['name'])  # TOM

# 2. get()

print(dict1.get('name'))  # TOM
print(dict1.get('id', 112))  # 112
print(dict1.get('id'))  # None

# 3. keys()
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])

# 4. values()
print(dict1.values())  # dict_values(['TOM', 24, '男'])

# 5. items()
print(dict1.items())  # dict_items([('name', 'TOM'), ('age', 24), ('gender', '男')])
