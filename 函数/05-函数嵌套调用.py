def test_b():
    print('------testB start')
    print('here is function testB\'s code ')
    print('------testB end')


def test_a():
    print('=======testA start')
    test_b()
    print('=======testA end')


test_a()


# 打印一条横线

def print_line():
    print('-' * 50)


def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(4)
