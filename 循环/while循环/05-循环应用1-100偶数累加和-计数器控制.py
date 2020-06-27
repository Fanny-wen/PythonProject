# 计数器控制增量为2

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
        i += 2
    else:
        i += 1

print(result)
