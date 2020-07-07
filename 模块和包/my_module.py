def testA(a, b):
    print(a + b)


def testB(a, b):
    print(a + b)


# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行testA函数调用

print(__name__, '==========')  # __main__
# __name__是系统变量，是模块的标识符，值是：如果是自身模块值是__mail__，否则是当前模块的名字
if __name__ == '__main__':
    testA(1, 2)

__all__ = ['testA']