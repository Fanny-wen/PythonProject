"""
语法：while 条件 :
        条件成立重复执行的代码
     else：
        循环正常结束之后要执行的代码
"""

i = 0
while i < 5:
    if i == 3:
        print('你不够真诚')
        break
    print(f'媳妇儿，我错了{i}')
    i += 1
else:
    print('媳妇儿原谅我了')  # break如果执行了 else下方的代码就不执行了
