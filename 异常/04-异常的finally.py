"""
finally表示的是无论是否异常都要执行的代码，例如关闭文件。
"""

try:
    f = open('test1.txt', 'r')
except Exception as result:
    f = open('test1.txt', 'w')
else:
    print('没问题')
finally:
    f.close()
