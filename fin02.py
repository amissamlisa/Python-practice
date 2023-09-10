def c(n,f,l):
    for i in range(1,n+1):
        if i % 2 != 0:
            print(f * 1,end='')
        else:
            print(l * 1,end = '')


n = int(input('個数:'))
f = input('記号1: ')
l = input('記号2: ')

c(n,f,l)
print('\n出力終了')