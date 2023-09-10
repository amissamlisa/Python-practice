x = int(input('nの値:'))
for i in range(1,x+1):
    print(' ' * (x - i) + '!' * ((i-1) * 2 + 1))
    