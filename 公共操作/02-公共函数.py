"""
len():计算容器中元素个数
del或del():删除
max():返回容器中元素最大值
min():返回容器中元素最小值
range(start,end,step):生成从start到end的数字，步长为step，共for循环使用
enumerate(可遍历对象,start = 0):函数用于将一个可便利的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
"""
str = 'abcdefg'
list = [10, 20, 30, 40]
# max()和min(）
print(max(str))  # g
print(max(list))  # 40

print(min(str))  # a
print(min(list))  # 10

# enumerate():返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
for i in enumerate(list):
    print(i)
for index, value in enumerate(list):
    print(index, value)
"""
(0, 10)
(1, 20)
(2, 30) 
(3, 40)
"""
