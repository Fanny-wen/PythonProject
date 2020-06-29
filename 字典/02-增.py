"""
字典为可变类型
写法：字典序列[key] = 值
注意：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
"""

dict1 = {'name': 'TOM', 'age': 24, 'gender': '男'}

dict1['id'] = 1111

print(dict1)
