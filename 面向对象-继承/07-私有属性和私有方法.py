"""
定义私有属性和方法：在python中，可以为实例属性和方法设置私有权限，即设置某个属性或实例方法不继承给子类
设置私有权限的方法：在属性名和方法名 前面 加上两个下划线 __
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}')

    def dance(self):
        print('dance')


# 另一个师傅类
class AnotherMaster(Master):

    def __init__(self):
        self.kongfu = '[新方法]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 徒弟类
class Prentice(AnotherMaster):
    def __init__(self):
        self.kongfu = '[小明独创方法]'
        self.__money = 200000

    def make_cake(self):
        super().dance()
        print(f'使用{self.kongfu}')

    def __info_print(self):
        print(f'{self.__money}')

    def make_Master_cake(self):
        super().__init__()
        super().make_cake()

    def make_Another_cake(self):
        super().__init__()
        super().make_cake()


class Tusun(Prentice):
    pass


xiaoming = Prentice()
xiaoming.make_cake()

xiaoxiaoming = Tusun()

"""
获取和修改私有属性
"""
