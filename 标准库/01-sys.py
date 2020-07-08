import sys

print('The file name :', sys.argv[0])  # The file name : D:/PythonProject/标准库/01-sys.py
print('The number of argument', len(sys.argv))  # The number of argument 1
print('The argument is :', str(sys.argv))  # The argument is : ['D:/PythonProject/标准库/01-sys.py']
print(sys.argv)  # ['D:/PythonProject/标准库/01-sys.py']

for i in range(10):
    if i == 5:
        print(i)
        # sys.exit('I wet out at here')  # 退出当前程序，并发起SystemExit异常
    else:
        print(i)
# sys.path
print(sys.path)  # 查找模块所在目录，以列表的形式显示出来


