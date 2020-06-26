def isChildLabor():
    age = int(input('请输入你的年龄'))
    if age <= 18:
        print(f'你只有{age}岁，属于童工，不能雇佣你')
    elif 18<= age <= 60:
        print(f'你的年龄是{age}岁，正好合适')
    else:
        print(f'你的年龄是{age}，年龄太高了')

isChildLabor()