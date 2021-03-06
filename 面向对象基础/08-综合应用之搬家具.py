class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 12)


class Home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子地址在：{self.address},面积为：{self.area},剩余面积：{self.free_area},家具有：{self.furniture}'

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家里已经装不下了，不能再买了！！')


home1 = Home('北京', 100)
print(home1)

home1.add_furniture(bed)
print(home1)
