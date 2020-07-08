"""
glob模块提供了一个在目录中使用通配符搜索创建文件列表的函数
"""

import glob

g = glob.glob('*.py')
print(list(g))  # ['01-sys.py', '02-copy.py', '03-os.py', '04-文件通配符.py']
