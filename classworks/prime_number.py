# number = int(input("Enter any number: "))
# count = 0
# factor = 1
# while factor < number:
#     if number % factor == 0:
#         count += 1
#     factor += 1
# if count > 1:
#     print("It is not a prime number")
# else:
#     print("it is a prime number")
import math

number = int(input("Enter any number: "))
new_num = math.ceil(math.sqrt(number))
count = 2
while count <= new_num:
    if number % count == 0:
        print("It is not a prime number")
        break
    count += 1
else:
    print("It is a prime number")