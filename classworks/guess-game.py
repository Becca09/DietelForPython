i = 1
while i != -1:
    number = int(input('enter a number between 1 - 50: '))
    if number > 15:
        print("too high")
    elif number < 15:
        print(" Too low")
    elif number == 15:
        print("Correct")
        break
i += 1
