"""
有三个办公室，8位老师，将8位老师随机分配到办公室
"""
import random

teachers = ['老一', '老二', '老三', '老四', '老五', '老六', '老七', '老八']
offices = [[], [], []]

for teacher in teachers:
    num = random.randint(0, 2)
    offices[num].append(teacher)
# print(offices)


for office in offices:
    i = 1
    print(f'办公室{i}的人数是{len(office)},老师分别是：')
    for name in office:
        print(name)
    i += 1
