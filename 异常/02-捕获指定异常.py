"""
语法：
    try:
        可能发生错误的代码
    except 异常类型:
        如果捕获到该异常类类型执行的代码
"""

try:
    print(num)
except NameError:
    print('有错误')

# 捕获多个指定异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后。并使用元组的方式进行书写

try:
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print('有错误')

# 捕获异常描述信息
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)  # name 'num' is not defined

# 捕获所有异常
try:
    print(num)
except Exception as result:
    print(result)  # name 'num' is not defined
