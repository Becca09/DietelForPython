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
hug = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(hug))

# random.shuffle(hug)
# print(hug)
