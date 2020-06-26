"""
1.出拳
    玩家：手动输入
    电脑：随机
2.判单输赢
    玩家赢
    电脑赢
    平局
"""
import random


def mora():
    player = int(input('你准备出什么：0--拳头,1--剪刀,2--布；'))
    computer = random.randint(0, 2)
    if ((player == 2) and (computer == 0)) or ((player == 2) and (computer == 0)) or ((player == 0) and (computer == 1)):
        print('玩家获胜')
    elif player == computer:
        print('平局')
    else:
        print('电脑获胜')
mora()