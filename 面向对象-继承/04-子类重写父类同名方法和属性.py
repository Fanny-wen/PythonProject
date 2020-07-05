"""
小明掌握了师傅和另一个师傅的技术后，自己研究了一套新的方法
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 另一个师傅类
class AnotherMaster(object):

    def __init__(self):
        self.kongfu = '[新方法]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 徒弟类
class Prentice(Master, AnotherMaster):
    def __init__(self):
        self.kongfu = '[小明独创配方]'

    def make_cake(self):
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()
        print(f'小明使用的是{self.kongfu}')

    """子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装"""

    # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
        # 父类类名：函数()
        Master.make_cake(self)

    def make_anothermaster_cake(self):
        AnotherMaster.__init__(self)
        AnotherMaster.make_cake(self)


xiaoming = Prentice()
print(xiaoming.kongfu)  # [小明独创配方]
xiaoming.make_cake()  # 小明使用的是[小明独创配方]

# 查看某个类的父类继承关系
print(Prentice.__mro__)

# 子类如何调用父类的同名方法和属性

xiaoming.make_master_cake()  # 运用[古法煎饼果子配方]
xiaoming.make_anothermaster_cake()  # 运用[新方法]
