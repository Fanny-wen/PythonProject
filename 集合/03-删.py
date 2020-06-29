"""
1.pop():随机删除集合中的某个数据，并返回这个数据
2.discard():是删除指定数据，如果数据不存在也不会报错
3.remove():删除指定数据，如果数据不存在则报错
"""

s1 = {1, 2, 3, 4, 5, 6, 7}

# remove()

s1.remove(1)
print(s1)  # {2, 3, 4, 5, 6, 7}

# s1.remove(1) # KeyError: 1

# discard()
s1.discard(2)  # {3, 4, 5, 6, 7}
print(s1)
s1.discard(2)  # 不报错

# pop()
del_s = s1.pop()
del_s2 = s1.pop()
print(s1)
print(del_s)
