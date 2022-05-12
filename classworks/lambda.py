# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# print(add.__name__)
# print(sub.__name__)


# def add(a, b):
#     return a + b
#
#
# def sub(c, d):
#     return d - c
#
#
# def mul(a, t):
#     return a * t
#
#
# def operate(x, y, fun):
#     return fun(x, y)
#
#
# val_sub = operate(5, 24, lambda x, y: y - x)
# val_add = operate(5, 24, lambda x, y: y + x)
# val_mul = operate(5, 24, lambda x, y: y * x)
# div = operate(5, 24, lambda x, y: y / x)
#
# print(val_sub)
# print(val_add)
# print(val_mul)
# print(div)
#
#
# def multiple(x, func):
#     return func(x)
#
#
# square = multiple(10, lambda x: x ** 2)
# cube = multiple(10, lambda x: x ** 3)
# print(square)
# print(cube)


# All AND ANY
# print(all([1, 2, 3, 0, 6, 0]
#           ))
# print(any((True, False, True)))
#
# names = ["Amaka", "Segun", "comb", "samson", "foil"]
#
# print(all((name.istitle() for name in names)))
from functools import reduce

persons = [
    {"name": "Omosetan Omorele", "age": 30, "Year_of_exp": 4, "language": ["Python", "Java"]},
    {"name": "John Doe", "age": 25, "Year_of_exp": 2, "language": ["Javascript", "C#"]},
    {"name": "Amaka Stephen", "age": 19, "Year_of_exp": 5, "language": ["Python"]},
    {"name": "Florence Seyi", "age": 37, "Year_of_exp": 12, "language": ["Python", "HTML"]},
    {"name": "Yemisi Tolani", "age": 40, "Year_of_exp": 4, "language": ["Kotlin", "GOlang"]}
]

print(any(True if person["age"] <= 20 else False for person in persons))
print(any(person["age"] <= 20 for person in persons))
print([person["age"] <= 20 and "Python" in person["language"] for person in persons])
print([person["name"] for person in persons if person["age"] <= 20 and "Python" in person["language"]])

# **************************************************************************************************************

map_object = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
lst1 = list(map_object)
lst2 = list(map_object)
print("1", lst1)
print("2", lst2)


# filter,  filter returns all the value that matches the condition, in this example the method says the numbers in x
# divided by two and has a remainder zero, so then filter makes it return only those numbers
def isEven(x):
    return x % 2 == 0


filter_obj = list(filter(isEven, range(1, 10)))
print(filter_obj)

# reduce, sums all the number with themselves and return them as one value, same as multiplication,
# division and subtraction

reduce_ = reduce(lambda x, y: x + y, range(1, 11))
print(reduce_)

from functools import reduce

fruits = ["Apple", "Pear", "Pineapple", "Orange", "Watermelon", "Banana", "Cucumber"]
longest = reduce(lambda x, y: x if len(x) >= len(y) else y, fruits)
print(longest)
print(max(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key= lambda  x: x[-1]))
