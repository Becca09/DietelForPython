i = 1
while i <= 100:
    if i % 15 == 0:
        print('fizz buzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    i += 1

# name = " Ebube"
# print(name[:: -1])
#
# n = 1231
# n = str(n)
# print(n == n[:: -1])
#
# for i in range(1, 11):
#     print("*" * i)
# print()
# for i in range(11, 0, -1):
#     print("*" * i)
#
# a_str = 'spam'
# a_str[1] = 'l'
# new_str = a_str[:1] + 'l' + a_str[2:]
# print(new_str)
#
#
