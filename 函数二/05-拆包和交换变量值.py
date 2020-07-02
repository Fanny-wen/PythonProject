"""
拆包：元组
拆包：字典
"""


# 拆包元组数据
def return_num():
    return 10, 200


num1, num2 = return_num()
print(num1, num2)  # 10 200

# 拆包字典数据

dict1 = {'name': 'tom', 'age': 24}
a, b = dict1
print(a, b)  # name age
