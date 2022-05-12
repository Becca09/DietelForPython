# lst = list('abcde')
# print(lst)
# print(' '.join(lst))
#
# a = list("abcdefghijklm")
# print(a[9])
# print(a[::-1])
# print(' '.join(a[::-1]))
# print(a * 2)
# print(a + [1, 3, 5, 7, 9])
#
# print('f' in a)
# print('q' in a)
#
# list_of_list = [1, 2, [3, 4, 5], 6]
# print(list_of_list[2])
#
# my_dict = {
#     'name': "segun",
#     'age': 12,
#     'sex': "male",
#     'hobby': ['python', 'java'],
#     'is_wide_beater': False
# }
# # print(my_dict)
# # for key in my_dict:
# #     print(key, '-->', my_dict[key])
#
# print(my_dict.items())
# print(my_dict)
#
# print(my_dict['name'])
#
# for key in my_dict.keys():
#     print(key, '-->', my_dict[key])
#
# for value in my_dict.values():
#     print(value)
#
# for key, value in my_dict.items():
#     print(key, '-->', value)
#
# print(my_dict.items())
#
# prof = dict(name='Segun', age=12)
# print(prof)
#
# print()
#
# fruits = ['apple', 'banana', 'cucumber', 'pear']
# print(fruits)
#
# # fruits.append("orange")
# # print(fruits)
# #
# # fruits.extend("orange")
# # print(fruits)
# print()
#
# fruits.insert(-1, "grape")
# print(fruits)
#
# print()
#
# fruits.insert(len(fruits), "grape")
# print(fruits)
#
# print()
#
# print(fruits.pop())
# print(fruits)
#
# print()
#
# fruits.remove('apple')
# print(fruits)
#
# print()
#
# print(fruits.clear())
# print(fruits.count('apple'))
#
# print()
#
# fruits.copy()
# print(fruits)
#
# print()
#
# fruits.reverse()
# print(fruits)
#
# print()
#
# fruits.sort()
# print(fruits)

import random

#
# print(random.randint(0, 10))

# random.seed(76)
# a = random.randint(0, 10)
# print(a)
#
# b = random.randrange(0, 10, 2)
# print(b)
#
# hug = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.choice(hug))

# random.shuffle(hug)
# print(hug)

# list comprehension
# lst = []
# for i in range(1, 11):
#     lst.append(i ** 2)
# print(lst)
#
# list_ = [i ** 2 for i in range(1, 11)]
# print(list_)
# import sys
#
# even_list_ = [i for i in range(2, 11, 2)]
# print(even_list_)
# #
# # even_and_squared_odds = [a if a % 2 == 0 else a ** 2 for a in range(1, 11)]
# # print(even_and_squared_odds)
# #
# # lst_input = [int(input("Enter a number: ")) for num in range(1, 4)]
# # print(lst_input)
#
# list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
# print(list_nested_for)
#
# length_names = [len(name) for name in ['wale', 'adebayo', 'funmilayo', 'yemi']]
# print(length_names)
#
# upper_names = [name.upper() for name in ['wale', 'adebayo', 'funmilayo', 'yemi']]
# print(upper_names)
#
# # lists of dictionary
# list_of_dicts = [{key: value} for key, value in zip(upper_names, even_list_)]
# print(list_of_dicts)
#
# # generator and list comprehension
# generator = (num for num in range(1, 10 ** 5))
# lst_comprehension = [num for num in range(1, 10 ** 5)]
# set_comprehension = {num for num in range(1, 10 ** 5)}
#
# # dict_comprehension = {k: v for k, v in zip(range(1, 10 ** 5))}
# print(sys.getsizeof(lst_comprehension))
# print(sys.getsizeof(generator))
# print(sys.getsizeof(set_comprehension))
# # print(sys.getsizeof(dict_comprehension))
#
#
# s1 = {1, 2, 3, 5}
# s2 = {4, 3, 2, 5}
#
# s1.pop()
# print("pop", s1)
#
# # intersection
# print(s1 & s2)
#
# # intersection update
# s1 &= s2
# # or
# s1 = s1 & s2
# print(s1)
#
# # union
# print(s1 | s2)
#
# # update
# s1 |= s2
# print(s1)
#
# # subset and superset
# s1 = {1, 2, 3, 5}
# s2 = {1, 2, 5}
# print(s1 > s2)
# print(s1 < s2)
#
# dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
# print(dict_play["name"])
#
# # if name not found, return argument in get
# dict = {"age": 32, "influenced": "Samson"}
# print(dict.get("name", "Samson"))
#
# dict.pop("age")
#
# dict.update()
#
# # dict.popitem()
# print(dict)
#
# print({}.fromkeys("hello", "UNKNOWN"))
#
#
# def get_first(s: str) -> str:
#     return s[0]
#
#
# l = [get_first(val) for val in ["Hello", "Wale", "Fine", "Boy"]]
# print(l)

lst = []
for i in range(65, 91):
    lst.append(chr(i))
print(lst)

# list comprehension
lst2 = [chr(i) for i in range(65, 91)]
print(lst2)
