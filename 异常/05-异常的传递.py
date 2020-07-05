"""
尝试制度打开test.txt 文件存在读取内容，不存在提示用户
读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经意外终止
"""
import time

try:
    f = open('test.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取问价的过程中，产生了异变，那么就会捕获到
        # 比如 按下了 ctrl + c
        print('意外中止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('文件不存在')
