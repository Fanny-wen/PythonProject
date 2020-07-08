import copy

i = copy.__all__
print(i)  # ['Error', 'copy', 'deepcopy']

a = [1, 2, [3, 4]]
b = a

c = copy.copy(a)
d = copy.deepcopy(a)

a[0] = 0
a[2].append(6)
print(a)  # [0, 2, [3, 4, 6]]
print(b)  # [0, 2, [3, 4, 6]]
print(id(a) == id(b))  # True
print(c)  # [1, 2, [3, 4, 6]]
print(d)  # [1, 2, [3, 4]] d 和 a 是两个完全不同的对象，二者不会互相影响
