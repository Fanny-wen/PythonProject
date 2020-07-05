"""
思考：一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性呢?
答：传参数
"""


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(self.width, self.height)


haier = Washer(200, 300)
haier.print_info()  # 200 300
