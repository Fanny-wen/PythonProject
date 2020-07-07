"""
了解模块
导入模块
制作模块
__all__
包的使用方法
"""
# 1.导入模块

'''
导入模块的方式
    ·import 模块名
    ·from 模块名 import 功能名
    ·from 模块名 import *
    ·import 模块名 as 别名
    ·from 模块名 import 功能名 as 别名
'''

# 2.制作模块
"""
在python中，每个python文件都可以作为一个模块，模块的名字就是文件的名字。也就是说自定义模块名必须要符合标识符命名规则。
"""
# 2.1定义模块
'''新建一个文件，命名为my_module.py'''
# 2.2测试模块
'''运行一下模块'''
# 2.3调用模块
'''
导入模块
调用功能
'''
import my_module

print(__name__, '-----')  # my_module
my_module.testA(2, 2)

# 模块定位顺序

"""
当导入一个模块，Python解析器对模块位置的搜素顺序是：
    1.当前目录
    2.如果不在当目录，python则搜索在shell变量PYTHONPATH下的每个目录
    3.如果都找不到，python会查看默认路径，UNIX下，默认路径一般为/usr/local/lib/python/模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
    注意：
        ·自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
        ·使用from 模块名 import 功能 的时候，如果功能名字重复，调用的是最后定义或导入的功能
"""
