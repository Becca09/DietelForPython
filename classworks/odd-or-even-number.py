number = int(input('enter a number: '))
while number != 1:
    if number % 2 != 0:
        number = (number * 3) + 1
    elif number % 2 == 0:
        number = number // 2
    print(number, end=' ')

# it keeps looping the number till the solution gets to 1
# if the number is an even number it runs the elif first
# if the number is odd it runs the if first


# and then keeps looping through both till the last number is 1
