"""
pprint模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取。
"""

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)
