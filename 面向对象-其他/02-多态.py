"""
多态指的是一类事物有多种形态（一个抽象类有多个子类，因而多态的概念依赖于继承）
    定义:多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果。
    好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化。
    实现步骤：
        ·定义父类，并提供公共方法
        ·定义子类，并重写父类方法
        ·传递子类对象给调用者，可以看到不同子类执行效果不同
"""


# 体验多态

class Dog(object):
    # 父类提供统一的方法，哪怕是空方法
    def work(self):
        print('指哪打哪')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DruDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    # 传入不同的对象，执行不同的代码，即不同的work函数
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DruDog()

police = Person()

police.work_with_dog(ad)  # 追击敌人
police.work_with_dog(dd)  # 追查毒品
