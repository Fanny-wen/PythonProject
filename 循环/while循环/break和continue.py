# break:当某些条件成立，退出整个循环
i = 1
while i <= 5:

    # 条件：如果大于3，就结束
    if i > 3:
        break
    else:
        print(f'{i}')

    i += 1
print(f'{i}')

# continue:当某些条件成立，退出本次循环，继而执行下一次循环
print('------------------------')
j = 1
while j <= 5:
    # 条件
    if j == 3:
        j += 1
        continue
    print(f'{j}')
    j += 1
