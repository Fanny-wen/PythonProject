"""
小明是个爱学习的好孩子，像学习更多的技术
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 另一个师傅类
class AnothorMaster(object):

    def __init__(self):
        self.kongfu = '[新方法]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 徒弟类
class Prentice(Master, AnothorMaster):
    pass


xiaoming = Prentice()
print(xiaoming.kongfu)  # [古法煎饼果子配方]
xiaoming.make_cake()  # 运用[古法煎饼果子配方]

"""
结果：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法
"""
