dict1 = {'name': 'TOM', 'age': 24, 'gender': '男'}

for key in dict1.keys():
    print(key)  # name age gender

for value in dict1.values():
    print(value)  # TOM 24 男

for item in dict1.items():
    print(item)  # ('name', 'TOM') ('age', 24) ('gender', '男')
