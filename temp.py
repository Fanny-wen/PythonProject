import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("func name: {}".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@log
def my_now():
    print("111")


my_now()
print(my_now.__name__)
