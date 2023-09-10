#練習問題
m = int(input('試行回数: '))
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
import random 
u = 0
for v in range(1,m+1):
    for j in range(0,2):
        rn = random.randint(1,6)
        u = u + rn
    if u == 2:
        b += 1
    elif u == 3:
        c += 1
    elif u == 4:
        d += 1
    elif u == 5:
        e += 1
    elif u == 6:
        f += 1
    elif u == 7:
        g += 1
    elif u == 8:
        h += 1
    elif u == 9:
        i += 1
    elif u == 10:
        j += 1
    elif u == 11:
        k += 1
    elif u == 12:
        l += 1
    u = 0
   
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)
#print(g)
#print(h)
#print(i)
#print(j)
#print(k)
#print(l)
max_3 = b

if max_3 < c:
    max_3 = c
if max_3 < d:
    max_3 = d
if max_3 < e:
    max_3 = e
if max_3 < f:
    max_3 = f
if max_3 < g:
    max_3 = g
if max_3 < h:
    max_3 = h
if max_3 < i:
    max_3 = i
if max_3 < j:
    max_3 = j
if max_3 < k:
    max_3 = k
if max_3 < l:
    max_3 = l


c_dict = {b:2,c:3,d:4,e:5,f:6,g:7,h:8,i:9,j:10,k:11,l:12}

print('最もよく出た数字:',str(c_dict[max_3]))
print('出現確率:',str(max_3 / m * 100) + '%')