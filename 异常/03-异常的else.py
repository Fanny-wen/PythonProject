"""
else表示的时如果没有异常要执行的代码。
"""

try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有问题啊')
