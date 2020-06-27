"""
语法： for 临时变量 in 序列 :
        重复执行的代码1
        重复执行的代码2
        重复执行的代码3
        重复执行的代码4
"""

str1 = 'hello world'
for i in str1:
    if i == 'o':
        continue
    print(i)

