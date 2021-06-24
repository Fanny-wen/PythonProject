import traceback
import sys


def func1():
    raise Exception('error')


def main():
    try:
        func1()
    except Exception as e:
        a, b, c = sys.exc_info()
        # print(a, b, c)
        print(traceback.print_tb(c))
        # traceback.print_exc()
        print("=" * 100)
        # print(traceback.format_exc())


if __name__ == "__main__":
    main()
