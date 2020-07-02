# 1.声明全局变量 2.定义两个函数 3.函数一修改全局变量；函数二访问全局变量

glo_num = 0


def test1():
    global glo_num  # 申明全局变量 glo_num
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)
test1()
test2()
print(glo_num)
