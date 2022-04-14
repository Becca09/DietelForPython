product = []
quantity = []
price = []
total = []
design = "x"
dashes = "-"

counter = 0

name = 'florenceAncCo Limited'
address = '12 cocoa house agbado'
PhoneNumber = ' 07023567890'
email = 'flocrenceco@gmail.com'

status = True

while status:
    product_name = str(input("what are you buying?"))
    product.append(product_name)

    no_of_product = int(input("how many are you buying? "))
    quantity.append(no_of_product)

    product_price = int(input("how much is it?"))
    price.append(product_price)

    total_amount = product_price * no_of_product
    total.append(total_amount)
    counter += 1
    stillBuying = int(input("""
    still buying?
                1 --> yes
                2 --> no """))
    if stillBuying == 1:
        status = True
    elif stillBuying == 2:
        status = False

grandTotal = sum(total)

print(design * 70)
print(dashes * 70)
print('              ', name)
print('             ', address)
print('              ', PhoneNumber, email)
print( dashes * 70)
print( dashes * 70)
print('                 ', 'product'   '   qty'  '   price'  '   total')
for i in range(0, counter):
    print(f' {product[i]:>22}   {quantity[i]:>4}    {price[i]:>4}   {total[i]:>4} ')

print(design * 70)
print('                    ', 'total ', '             ', grandTotal)
print(dashes * 70)
print('                          ', ' Thank you for coming ')
print(design * 70)
