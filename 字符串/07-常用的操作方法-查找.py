# 查找
# find()    index()     count()
# rfind()   rindex()
mystr = "hello world and itcast and itheima and Python"

# 1.find(字串，开始位置下标，结束位置下标) 检测某个字串是否包含在这个字符串中，如果包含，则返回字串开始位置的下标，否则则返回-1
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1
print('---------------------------')
# 2.index(字串，开始位置下标，结束位置下标)
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
print(mystr.index('andx'))  # 报错
print('---------------------------')
# 3.count(字串，开始位置下标，结束位置下标) 返回子串在字符串中非重叠出现的次数
print(mystr.count('and'))
# 4.rfind() 从右边开始
# 5.rindex()从右边开始
