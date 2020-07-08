"""
1.update():追加序列
2.add():追加单一数据
"""
# add() :集合有去重功能，如果追加的数据是集合已有的数据，则什么事情都不做

s1 = {10, 20}

s1.add(100)

print(s1)  # {100, 10, 20}

s1.add(10)

print(s1)  # {100, 10, 20}

# s1.add([1, 2, 3, 4])  # TypeError: unhashable type: 'list'

# update()

s1.update([1, 2, 3, 4, 5])

print(s1)  # {1, 2, 3, 100, 4, 5, 10, 20}
