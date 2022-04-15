p = 1000
r = 0.07
i = 10
while i <= 30:  # while 10 is less than 30
    a = p * pow(1 + r, i)
    print("The amount you will have after", i, "years is", a)  # solve this
    i += 10  # then come here again and add 10 t0 10, stop till it's 30
