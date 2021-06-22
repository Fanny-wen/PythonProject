import math
from sys import float_info

num1, num2, num3 = 1, False, True
int_num = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def return_bool1(x, y):
    return x and y


def return_bool2(x, y):
    return x or y


if __name__ == "__main__":
    result1 = return_bool1(num1, num2)
    result2 = return_bool1(num1, num3)
    result3 = return_bool2(num1, num3)
    result4 = return_bool2(num1, num3)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(float_info)
    print(callable(int_num))
    print(return_bool1)
    print(callable(return_bool1))
    print(dir(math))
    for item in enumerate(my_list):
        print(item)
    print("=" * 100)
    my_list.extend(['x', 'y'])
