num1 = float(input("Enter a number"))
num2 = float(input("Enter a number"))
num3 = float(input("Enter a number"))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(" Order of number is ", num1, num2, num3)
    elif num3 >= num2:
        print(" Order of number is ", num1, num3, num2)

if num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(" Order of number is ", num2, num1, num3)
    elif num3 >= num1:
        print(" Order of number is ", num2, num3, num1)

if num3 >= num1 and num3 >= num2:
    if num2 >= num1:
        print(" Order of number is ", num2, num1, num3)
    elif num1 >= num2:
        print(" Order of number is ", num2, num3, num1)
