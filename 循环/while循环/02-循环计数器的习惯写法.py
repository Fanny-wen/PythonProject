"""
while 条件:
    条件成立要重复执行的代码
    ...
"""
time = 0
while time < 100:
    print(f'这是第{time+1}次循环')

    time += 1

print(f'我是什么时候执行的{time}') # 需要等到整个循环体执行完了才执行
