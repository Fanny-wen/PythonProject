# 如果年龄大于等于18，输出：已经成年，可以上网 ---准备年龄的数据 和 18 做比较

def issurf():
    age = input("请输入你的年龄")
    if int(age) >= 18:
        print(f'您的年龄是{age}岁,已经成年，可以上网')
    else:
        print(f'你只有{age}岁，还不可以来网吧上网哦')

issurf()





