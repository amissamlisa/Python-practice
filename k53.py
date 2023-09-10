#1からｎまでの奇数の個数を求める
x = int(input('nの値:'))
g = -1
y = 0
for m in range(1,x+1,2):
    g += 1
    if m == 2*g + 1:
        y = y + 1
print('1から'+ str(x) + 'までの奇数の個数: ' + str(y))
#１からｎまでの奇数の和を求める
u = 1
i = 3
while i <= x:
    u = u + i
    i = i + 2
print('1から'+ str(x) + 'までの奇数の和: ' + str(u))