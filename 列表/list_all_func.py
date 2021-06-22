my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
my_list7 = []

if __name__ == "__main__":
    print(my_list1.append(10))  # append 没有返回值
    print(my_list1)
    print("=" * 100)
    print(my_list2.extend(list('x')))  # extend 没有返回值
    print(my_list2)
    print("=" * 100)
    print(my_list3.insert(0, 'y'))  # insert 没有返回值
    print(my_list3)
    print("=" * 100)
    print(my_list4.remove(0))  # remove 没有返回值
    print(my_list4)
    print("=" * 100)
    print(my_list5.pop())  # pop 有返回值
    print(my_list5)
    print("=" * 100)
    print(my_list6.clear())  # clear 没有返回值
    print(my_list6)
    for i in range(10):
        my_list7.append(i ** 2)
    print(i)
