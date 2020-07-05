"""
属性即是特征，比如：洗衣机的宽度、高度、重量...
对象属性既可以在类外面添加和获取，也能在类里面添加和获取
"""


class Washer():
    def wash(self):
        print('洗衣服')

    def print_info(self):
        print(f'宽度：{self.width},高度：{self.height}')


haier = Washer()

# 类外面添加对象属性
haier.width = 499
haier.height = 1234

# 类外面获取对象属性
print(haier.width)  # 499

# 类里面获取对象属性
haier.print_info()  # 宽度：499,高度：1234
