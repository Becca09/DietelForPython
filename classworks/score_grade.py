n_str = input('enter a number ')
n = int(n_str)
if n > 70:
    print('Grade A')
elif 60 <= n < 70:
    print('Grade B')
elif 50 <= n < 60:
    print('Grade C')
elif 40 <= n < 50:
    print('Grade D')
else:
    print('Grade F')


