number = int(input("Enter a number"))
digitOne = number // 10000 % 10
digitTwo = number // 1000 % 10
digitThree = number // 100 % 10
digitFour = number // 10 % 10
digitFive = number % 10

print(number)
print(str(digitOne), '     ', str(digitTwo), '      ', str(digitThree), '     ', str(digitFour), '     ', str(digitFive))
print(digitOne, digitTwo, digitThree, digitFour, digitFive, sep= '       ')

