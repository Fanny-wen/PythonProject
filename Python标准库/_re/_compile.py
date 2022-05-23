import re

prog = re.match(r'pattern', 'pattern')
print(prog)

res = re.findall(r'a*', 'aabaabaac', flags=0)
print(res)

res = re.search(r'abc', 'abc')
print(res)
