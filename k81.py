from random import randint as rs
n = int(input('n:'))
num_list = []
if n < 1 or n > 30:
    print('想定外の値が入力されました')
else:
    for i in range(1,n+1):
        rn =  rs(1,10)
        tp = print(rn) 
        num_list.append(rn)
        num_list = num_list 
    print(num_list)
    print(tuple(num_list[0:n+1:n-1]))