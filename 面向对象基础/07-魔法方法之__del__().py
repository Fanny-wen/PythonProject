"""
当输出对象是，python解释器也会默认调用__del__()方法
"""


class Washer():
    def __init__(self):
        self.width = 199

    def __del__(self):
        print('对象已删除')


haier = Washer()  # 对象已删除  最后输出
print(haier)
