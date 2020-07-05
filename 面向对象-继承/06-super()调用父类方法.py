"""
super()调用父类方法
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 另一个师傅类
class AnothorMaster(Master):

    def __init__(self):
        self.kongfu = '[新方法]'

    def make_cake(self):
        print(f'运用{self.kongfu}')
        # 方法一：super()带参数写法
        # super(AnothorMaster, self).__init__()
        # super(AnothorMaster, self).make_cake()

        # 方法二：无参数super()
        super().__init__()
        super().make_cake()


# 徒弟类
class Prentice(AnothorMaster):
    def __init__(self):
        self.kongfu = '[小明独创配方]'

    def make_cake(self):
        self.__init__()
        print(f'小明使用的是{self.kongfu}')

    def make_old_cake(self):
        # 方法一：super(当前类名,self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法二：super().函数()  super()自动按照__mor__顺序查找
        super().__init__()
        super().make_cake()




xiaoming = Prentice()
xiaoming.make_old_cake()
