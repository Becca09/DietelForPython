# def divide(a, b):
#     if b == 0:
#         raise ValueError("Denominator cannot be zero")
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError("At least you see watin we writ up ")
#     return a / b
#
#
# print(divide(2, 2))
# num = int(input("Enter the numerator: "))
# den = int(input("enter the denominator: "))
# while True:
#     try:
#         print(divide(num, den))
#         break
#     except (ValueError, TypeError):
#         print("wrong value")
#         num = int(input("Enter the numerator: "))
#         den = int(input("enter the denominator: "))

try:
    print("life's good")
    print([1, 2, 3][4])
    print("After life")

except ZeroDivisionError as e:
    print("ZeroError", e)
except IndexError as e:
    print("IndexError", e)
else:
    print("I run only when their is no error")
finally:
    print("i run every time")
