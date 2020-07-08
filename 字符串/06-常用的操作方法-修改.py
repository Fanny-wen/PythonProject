# 修改

# 1.replace(久串，新串，替换次数) 替换  返回一个新的字符串,不会改变原有字符串---说明字符串是不可变数据类型

mystr = "hello world and itcast and itheima and Python"

newstr = mystr.replace('and', 'or', 10)  # 替换次数如果超过出现的次数，表示替换所有这个字串

print(newstr)
print('---------------------------')
# 2.split(分割字符，num) --分割，返回一个列表,会丢失分割字符
# 注意：num表示的是分割字符出现的次数，即将来返回数据个数为num+1

mylist = mystr.split('and', 3)
print(mylist)
print('---------------------------')
# 3-- 字符或子串.join(多字符串组成的序列)--合并列表里面的字符串数据为一个大字符串

new_str = '...'.join(mylist)
print(new_str)
