"""
包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，那么这个文件夹就称为包
"""
# 导入包 方法一：
import mypackage.my_module1
# 导入包 方法二：需要早__init__.py中添加__all__列表
from mypackage import *

mypackage.my_module1.info_print1()  # 1   \n   my_module1

my_module1.info_print1()
