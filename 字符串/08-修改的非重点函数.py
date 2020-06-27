mystr = "hello world and itcast and itheima and Python"

# capitalize():将字符串第一个字符转换成大写

str1 = mystr.capitalize()
print(str1)

# title():将字符串每个单词首字母转换成大写

str2 = mystr.title()
print(str2)

# lower():将字符串中大写转小写

str3 = mystr.lower()
print(str3)

# upper():将字符串小写转大写

str4 = mystr.upper()
print(str4)
print('-------------------------')

mystr2 = "   hello world and itcast and itheima and Python   "
# lstrip() # 删除左侧空白字符

print(mystr2.lstrip())
# rstrip() # 删除右侧空白字符

print(mystr2.rstrip())

# strip() # 删除两侧空白字符

print(mystr2.strip())

print('====================')

mystr3 = 'hello'
# 字符串序列.ljust(长度,填充字符)  返回一个元字符串左对齐，并使用指定字符串（默认空格）填充至对应长度的新字符串

print(mystr3.ljust(10, '.'))

# 字符串序列.rjust(长度,填充字符)  返回一个元字符串左对齐，并使用指定字符串（默认空格）填充至对应长度的新字符串

print(mystr3.rjust(10, '.'))

# 字符串序列.center(长度,填充字符)  返回一个元字符串居中对齐，并使用指定字符串（默认空格）填充至对应长度的新字符串

print(mystr3.center(10, '.'))













