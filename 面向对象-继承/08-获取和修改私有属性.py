"""
在python中，一般定义函数名get_xx用来获取私有属性，定义set_xx用来修改私有属性
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
        super().__init__()
        self.kongfu = '[新方法]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 徒弟类
class Prentice(AnotherMaster):
    def __init__(self):
        super().__init__()
        self.kongfu = '[小明独创方法]'
        # 定义私有属性
        self.__money = 200000

    # 定义函数：获取私有属性值： get_xx
    def get_money(self):
        return self.__money

    # 定义函数：修改私有属性值： set_xx
    def set_money(self):
        self.__money = 234524

    def make_cake(self):
        super().dance()
        print(f'使用{self.kongfu}')

    # 定义私有方法
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

print(xiaoxiaoming.get_money())
