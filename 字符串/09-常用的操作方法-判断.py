# 所谓判断即是判断真假，返回的结果是布尔数据类型：True或False
mystr = "hello world and itcast and itheima and Python"

# startwith(字串,开始位置下标,结束位置下标):检查字符串是否是以指定字串开头
print(mystr.startswith('hello'))

# endswith(字串,开始位置下标,结束位置下标):检查字符串是否是以指定字串结尾
print(mystr.endswith('h'))

print('============================')



# isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False

print(mystr.isalpha())

# isdigit():如果字符串只包含数字则返回True 否则返回False

print(mystr.isdigit())

# isalnum():如果字符串至少有一个字符并且所有字符都是字母或者数字或组合则返回True，否则返回False

print(mystr.isalnum())

# isspace():如果字符串只包含空白，则返回True，否则返回False

print(mystr.isspace())
