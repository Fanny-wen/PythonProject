"""
思考：如果有如下两个列表：
list1 = ['name','age','gender']
list2 = ['tom',25,'mam']
如何快速合并为一个字典？
答：字典推导式
字典推导式作用：快速合并列表为字典或提取字典中目标数据
"""

# 创建一个字典：字典key是1-5数字，value是这个数字的2次方。
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}

# 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['tom', 25, 'mam']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)  # {'name': 'tom', 'age': 25, 'gender': 'mam'}

# 提取字典中目标数据
counts = {'MBP': 234, 'HP': 168, 'DELL': 153, 'Lenovo': 77, 'acer': 99}

# 需求：提取上述电脑数量大于等于200的字典数据

count = {key: value for key, value in counts.items() if value >= 200}
print(count)  # {'MBP': 234}
