import random


# random.sample, 返回一个列表
def get_random_str(length=16):
    str_list = random.sample("1234567890_*&@", length)  # 例:['2', '_', '6', '@', '*']
    str = "".join(str_list)
    return str


if __name__ == "__main__":
    _str = get_random_str(5)
    print(_str)
