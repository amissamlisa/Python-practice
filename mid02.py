n = int(input('個数:'))
for i in range(1,n+1):
    if i % 2 != 0:
        print('@' * 1,end='')
    else:
        print('+' * 1,end = '')
    
print('\n出力終了')