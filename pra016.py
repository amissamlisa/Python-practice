n = int(input('n:'))
x = 0
for i in range(3,n+1):
    co = 0
    for j in range(1,i):
        if i % j == 0:
            co += 1
    if co == 1:
        print(i)
        x += 1
print('素数の数: ' + str(x))