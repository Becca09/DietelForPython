x = int(input('input number: '))
factor = 1
sum_of_factors = 0;

# while factor < x:
#     if x % factor == 0:
#       print(factor, "is a factor of", x)
#     factor +=1
while factor <= (x // 2) :
    if x % factor == 0:
        sum_of_factors += factor
    factor +=1
print(sum_of_factors)
if sum_of_factors == x:
    print(x, "is a perfect number")
elif sum_of_factors > x:
    print(x, " is an abundant number")
else:
    print(x, "is a deficient number")
    