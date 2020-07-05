"""
一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼果子的技术，师傅要把这套技术传授给徒弟
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}')


# 徒弟类
class Prentice(Master):
    pass


xiaoming = Prentice()

print(xiaoming.kongfu)
xiaoming.make_cake()
