"""
1.append(数据):列表结尾追加数据
2.extend(数据):列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
3.insert(位置下标,数据):指定位置新增数据
"""
# 列表数据是可以改变的 ---- 列表可变类型
name_list = ['tom', 'lily', 'rose']

# append():改变原列表

name_list.append('terry')
print(name_list)

# 如果追加一个序列，则将整个序列追加进去

name_list.append((['1', '2']))
print(name_list)  # ['tom', 'lily', 'rose', 'terry', ['1', '2']]

print('================================')

# extend():追加数据是一个序列，把数据序列里面的数据拆开然后逐一添加到序列

name_list.extend('hello')
print(name_list)  # ['tom', 'lily', 'rose', 'terry', ['1', '2'], 'h', 'e', 'l', 'l', 'o']
name_list.extend(
    ['wen', 'zhou'])  # ['tom', 'lily', 'rose', 'terry', ['1', '2'], 'h', 'e', 'l', 'l', 'o', 'wen', 'zhou']
print(name_list)

print('=================================')

# insert():

name_list.insert(1,
                 'aaaa')  # ['tom', 'aaaa', 'lily', 'rose', 'terry', ['1', '2'], 'h', 'e', 'l', 'l', 'o', 'wen', 'zhou']L
print(name_list)
