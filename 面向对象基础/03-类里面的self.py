"""
self指的是调用该函数的对象
"""


class Washer():
    def wash(self):
        print('洗衣服')
        print(self, '===')  # <__main__.Washer object at 0x00000207C75C36D8>


haier = Washer()
print(haier, '---')  # <__main__.Washer object at 0x00000207C75C36D8>
haier.wash()
# 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象


"""
一个类创建多个对象
多个对象都调用函数的时候，self地址是否相同
答：不同的对象存储的地址不同
"""

haier2 = Washer()
print(haier2)  # <__main__.Washer object at 0x000002023D77B358>
haier2.wash()  # <__main__.Washer object at 0x000002023D77B358>
