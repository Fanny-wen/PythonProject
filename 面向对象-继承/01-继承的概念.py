"""
继承的概念
单继承
多继承
子类重写父类的同名属性和方法
子类调用父类的同名属性和方法
多层继承
super()
私有属性和私有方法
"""


# 体验继承：python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法。

# 父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):
    pass


result = B()
result.info_print()  # 1

# 注意Python中，所有类默认继承object类，object类时顶级类或基类，其他子类叫做派生类
