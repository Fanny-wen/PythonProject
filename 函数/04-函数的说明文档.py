def add_func(num1, num2):
    """我是说明文档"""
    return num1 + num2


help(add_func)  # add_func(num1, num2) 我是说明文档


# 函数说明文档的高级使用
def sum_func(a, b):
    """
    :param a:参数1
    :param b:参数2
    :return: 返回值
    """
    print(a + b)

help(sum_func)
