"""
g = ( i for i in range(10))
一边循环一边计算的机制，称为生成器：generator。
"""

g = (i for i in range(19))
print(g)  # <generator object <genexpr> at 0x0000019CE79B2390>
"""
如果需要一个一个打印出来，可以通过next()函数获取generator的下一个返回值
"""
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('--------')
for i in g:
    print(i)
