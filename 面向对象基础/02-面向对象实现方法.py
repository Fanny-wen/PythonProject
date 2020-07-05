"""
定义类:
    python2中类分为：经典类 和 新式类
    语法：
        class 类名():
            代码
            ....
    注意：类名要满足标识符命名规则，同时遵循大驼峰命名习惯

定义对象:
    语法：
        对象名 = 类名()
"""


# 1.定义洗衣机类
class Washer(object):
    def wash(self):
        print('能洗衣服')


# 2.创建对象
haier = Washer()

# 3.验证成果   ---打印haier对象  ---使用wash功能--实例方法/对象方法
print(haier)
haier.wash()
