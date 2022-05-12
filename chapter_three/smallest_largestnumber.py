print("enter 5 numbers,")
num1 = int(input("Enter the first  number: "))
count = 1
addition = num1
smallest = num1
largest = num1
product = num1
average = 1

while count <= 4:
    num = int(input("Use enter to space them, input 4 more numbers: "))
    addition += num
    product = product * num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    count += 1
    average = product / 5

print("the sum of the numbers is ", addition)
print("the largest of the numbers is ", largest)
print("the smallest of the numbers is ", smallest)
print("the product of the numbers is ", product)
print("the average of the numbers is ", average)

# LINE 1: users are to enter five numbers LINE 2: Takes in the first number LINE 3 : the counter is initialized to 1


# LINE 4-7: the variables are automatically initialized to the first number because that is what has been inputted so
# far, so it becomes the lowest, highest.  sum, and product(because there is nothing else to add  it up with and also
# multiply with)


# LINE 8: shows that the average is initialized to 1

# LINE 10 -18 runs the while loop which says the counter hasn't run upto 4 more times keep doing the things in it,
# (that is keep collecting 1 more number till you have done that 4 times and do the things in it)

# in addition,  the rest of the numbers are summed up with the first number
# in product,  the rest of the numbers are multiplied  with the first number
# in largest,  the if statement checks if the other numbers inputted are higher than the first. if so, it automatically
# makes the next highest number the largest number
# in smallest,  the if statement checks if the other numbers inputted are lower than the first. if so, it automatically
# # makes the next lower number the smallest number

# Line 19 calculates the average
  