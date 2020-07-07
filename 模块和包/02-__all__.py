"""
如果一个模块文件中有__all__变量，当使用 from xxx import * 导入时，只能导入这个列表中的元素
"""

from my_module import *

testA(1, 6)  # 7

testB(1, 2)  # NameError: name 'testB' is not defined
