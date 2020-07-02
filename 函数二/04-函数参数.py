"""
位置参数：test('TOM',23,'女')
关键字参数：test('TOM',age=13,gender='男')
缺省参数：der test(name,age,gender='男'):
不定长参数：也叫可变参数。用于不缺确定调用的时候会传递多少个参数的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
包裹(packing)位置参数:
    def user_info(*args):
    user_info('tom',12)

注意：传进去的所有参数都会被args变量收集，它会根据传进去参数的位置合并为一个元组，args是元组类型，这就是包裹位置传递

包裹关键字参数:
    def user_info(**kwargs):
    user_info(name='TOM',age=34,id=12)
"""


def test_args(*args):
    print(args)  # ('tom', 12, '男')


def test_kwargs(**kwargs):
    print(kwargs)  # {'name': 'jerry', 'age': 23, 'gender': '女'}


test_args('tom', 12, '男')
test_kwargs(name='jerry', age=23, gender='女')
