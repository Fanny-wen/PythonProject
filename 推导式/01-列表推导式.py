"""
作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表
需求：0，1 ，2，4 ...
"""
# 1.创建一个空列表
list1 = []

# 2.书写循环，一次追加数字到空列表list1中

# while 循环实现
i = 0
while i < 10:
    list1.append(i)
    i += 1

print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for 循环实现
list2 = []

for i in range(10):
    list2.append(i)

print(list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式实现

list3 = [i for i in range(10)]
print(list3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
