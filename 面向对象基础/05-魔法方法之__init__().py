"""
在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
"""

# __init__()
"""
思考：洗衣机的宽度和高度是与生俱来的属性，可不可以在生产过程中就赋予这些属性呢？
答：__init__()方法的作用：初始化对象
"""


class Washer():
    def __init__(self):
        self.width = 100
        self.height = 200

    def print_info(self):
        print(self.width, self.height)


"""
注意：__init__()方法，在创建一个对象时默认被调用，不需要手动调用。
    __init__() 中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去。
"""

haier = Washer()
haier.print_info()  # 100 200
