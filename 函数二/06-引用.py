"""
了解引用：在python中，值是靠引用来传递的
我们可以使用id()来判断两个变量是否为同一个值的引用。我们可以将id值理解为那块内存的地址标识
"""
# 1.int整型
a = 1
b = a

print(b)

print(id(a))  # 140732715414352
print(id(b))  # 140732715414352

a = 2
print(id(b))  # 说明int类型为不可变类型

# 2.list列表

list_a = [1, 2, 3, 4]
list_b = list_a
print(id(list_a))  # 3025885094472
print(id(list_b))  # 3025885094472

list_a.append(5)
print(id(list_b))  # 列表是可变类型
