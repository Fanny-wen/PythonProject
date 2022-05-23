import string
from Python标准库._random._sample import get_random_str

my_string = get_random_str(length=32)

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)
print(string.punctuation)
# -----------------------------------------------------
print("=" * 100)
formatter = string.Formatter()

data1 = ("Pi = ", 3.1415926)
strtmp1 = "This is a test:{}{:.4f}"
print(formatter.format(strtmp1, *data1))

data2 = {"Key1": 3.1415926, "Key2": "Pi = "}
strtmp2 = "This is a test:{Key2}{Key1}"
# print(formatter.format(strtmp2, **data2))
