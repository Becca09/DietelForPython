# def get_digit(number: int, position: int) -> int:
#     """
#     return digit at position in number, counting from right
#     >>> get_digit(234, 0)
#     4
#     >>> get_digit(234, 2)
#     2
#     >>> "hello"
#     'hello'
#     >>> '2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
#     5
#     Traceback (most recent call last):
#         ...
#     TypeError: can only concatenate str (not "int") to str
#     """
#     return number // (10 ** position) % 10
#
#
# get = get_digit(234, 2)
# print(get)

num = 1


def function():
    global num
    num += 1
    print(num)


def func1():
    num = 2


def func2():
    num = 3
    print(num)


# positional argument
def add(a: int = 5, b: str = "colour") -> tuple[int, str]:
    return a, b


print(add(3, "3"))
print(add(3))
print(add())

print(add(a=5, b="you"))


def mutable_ish(a=None):
    if a is None:
        a = []
    a.append('python')
    return a


print(mutable_ish())
print(mutable_ish([1, 2, 3, 4]))


# tuple packing
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


lst = [7, 9, 3, 10, 56]
print(add(*[1, 2, 3, 4, 5]))
print(add(*lst))


def true_false(age):
    if age >= 18:
        return True
    return False


def dict_pack_unpack(*args, **kwargs):
    print("kwargs", kwargs)
    print("Args", args)


# dict_pack_unpack(4, 5, "goal", name="shola", age=45, sex="male")

def sub(a, b, /, c):
    print(a, b, c)


sub(1, 3, c=4)

d = dict(a=1, b=2, c=4)
print(d)
dict_pack_unpack(**d)


