"""
1.准备数据
2.格式化符号输出数据
"""

age = 18
name = 'TOM'
weight = 39.3
stu_id = 1

# 1.今年我的年龄是x岁  --整数 %d
print('今年我的年龄是%d岁' % age)

# 2.我的名字是x  --字符串 %s
print('我的名字是%s' % name)

# 3.我的体重是x公斤  --浮点数 %f  %.数字f--保留几位小数
print('我的体重是%.2f公斤' % weight)

# 4.我的学号是x
print('我的学号是%03d' % stu_id)

# 5.我的名字是x，今年x岁了
print('我的名字是%s,今年%d岁了' % (name, age))
print('我的名字是%s,明年%d岁了' % (name, age + 1))
# 6.我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s,今年%d岁了，体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))
