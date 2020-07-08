import os

print(dir(os))

# os.rename('os.txt', 'osrename.txt') 成功修改os.txt为osrename.txt

# os.remove() 用来删除文件

# os.listdir() 显示目录中的文件
i = os.listdir()
print(list(i))  # ['01-sys.py', '02-copy.py', '03-os.py', 'osrename.txt']

# os.getcwd() 当前工作目录
# os.chdir() 改变当前工作目录
# os.pardir() 获取父级目录
print(os.getcwd())  # D:\PythonProject\标准库

# os.makedirs() 创建目录
# os.removedirs() 删除目录
