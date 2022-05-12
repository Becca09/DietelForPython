p = 1000
r = 0.07
for i in range(1, 31):
    print(f'The amount you will have after year {i} is {p * pow(1+r, i):.3f}')
