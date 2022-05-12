import math

digit = int(input("Enter a five digit number: "))
for i in range(0, 5):
    print(f'{math.floor(digit % (10 ** (5 - i)) / (10 ** (5 - 1 - i)))}', end='  ')
