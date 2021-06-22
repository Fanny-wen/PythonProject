import random

# random.seed, 初始化随机数生成器


"""
seed( ) 用于指定随机数生成时所用算法开始的整数值。
1.如果使用相同的seed( )值，则每次生成的随即数都相同；
2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
3.设置的seed()值仅一次有效
"""


def get_random1():
    random.seed(1)
    for i in range(5):
        random_num = random.random()
        print(random_num)


def get_random2():
    """设置 seed 相当于选择一条世界线!!!"""
    for i in range(5):
        random.seed(1)
        random_num1 = random.random()
        random_num2 = random.random()
        random_num3 = random.random()
        print(random_num1, random_num2, random_num3)


if __name__ == "__main__":
    get_random1()
    print("=" * 100)
    get_random2()
