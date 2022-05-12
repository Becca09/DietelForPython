status = True
total = 0
while status:
    miles_driven = int(input("Enter the miles driven (enter -1 to end): "))
    if miles_driven == -1:
        break
    gallon_used = int(input("Enter gallons used: "))
    miles_per_gallon = miles_driven * gallon_used
    total = total + miles_per_gallon
    print(f'The miles per gallon is {miles_per_gallon:.3f} miles_per_gallon')
    print()
    print("Do you want to make more entry? ")
    response = int(input("""Enter (1 or 2)
        1.--> Yes
        2.--> No  """))
    if response == 1:
        status = True
    elif response == 2:
        status = False
print()
print(f'The overall average miles/gallon was {total:.3f} miles_per_gallon')