"""
需求：1.被烤的时间和对应的地瓜状态：
    0-3：生的
    3-5：半生不熟
    5-8：熟的
    >8：糊了
"""


class SweetPotato():

    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def __str__(self):
        return f'烤了:{self.cook_time}分钟 \n状态：{self.cook_static} \n加了：{self.condiments}'

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 < self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '糊了'

    def add_condiments(self, *args):
        self.condiments.extend(args)


potato = SweetPotato()
potato.cook(4)
potato.add_condiments('盐', '辣椒')
print(potato)
potato.cook(2)
print(potato)
