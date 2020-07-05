"""
类方法：
    ·特点：需要用装饰器 @classmethod 来标记其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数。
    ·类方法使用场景：
        ·当方法中 需要使用类对象（如访问私有类属性等）时，定义类方法
        ·类方法一般和类属性配合使用
"""


# 1.定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


# 2.创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)  # 10

"""
静态方法：
    ·特点：
        ·需要通过装饰器 @staticmethod 来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象(形参没有self/cls)
        ·静态方法 也能够通过实例对象和类对象 去访问
    ·静态方法使用场景
        ·当方法中 既不需要使用实例对象（如实例对象，实例属性）,也不需要使用类对象(如类属性、类方法、创建是实例等)时，定义静态方法
        ·取消不需要的参数传递，有利于 减少不必要的内存占用和性能消耗
"""


# 1.定义类，定义静态方法
class Bird(object):
    @staticmethod
    def info_print():
        print('这是一个鸟类，用于创建鸟实例....')


# 2.创建对象
huamei = Bird()
# 3.调用静态方法
huamei.info_print()  # 这是一个鸟类，用于创建鸟实例....
'''通过类调用'''
Bird.info_print()  # 这是一个鸟类，用于创建鸟实例....
