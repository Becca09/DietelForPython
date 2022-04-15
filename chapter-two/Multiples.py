number1 = int(input('Enter a multiple number: '))
number2 = int(input('Enter a  number: '))

if number1 % number2 == 0:
    print(number2, "is a multiple of ", number1)
else:
    print(number2, "is not a multiple of ", number1)
