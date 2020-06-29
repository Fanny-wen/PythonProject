str1 = 'aa'
str2 = 'bb'

list1 = [1, 2]
list2 = [10, 20]

t1 = (1, 2)
t2 = (10, 20)

dict1 = {'name': 'python'}
dict2 = {'age': 20}

# + : 合并 ------ 支持的类型：字符串、列表、元组

print(str1 + str2)  # aabb
print(list1 + list2)  # [1, 2, 10, 20]
print(t1 + t2)  # (1, 2, 10, 20)
# print(dict1 + dict2)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


# * : 复制 ------- 支持的类型：字符串、列表、元组

print(str1 * 2)  # aaaa
print(list1 * 2)  # [1, 2, 1, 2]
print(t1 * 3)  # (1, 2, 1, 2, 1, 2)

# in : 元素是否存在------- 支持的类型：字符串、列表、元组、字典
# not in: 元素是否不在------- 支持的类型：字符串、列表、元组、字典
print('a' in str1)  # True
print('a' not in str1)  # False

print(1 in list1)  # True
print(1 not in list1)  # False

print(1 in t1)  # True
print(1 not in t1)  # False

print('name' in dict1)  # True
print('name' not in dict1)  # False
