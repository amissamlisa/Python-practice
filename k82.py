print('各月の日数を出力します')
month = int(input('月: '))
#日にちのタプルをつくる
day_tuple = (31,28,31,30,31,30,31,31,30,31,30,31)
#月のタプルをつくる
month_tuple = (1,2,3,4,5,6,7,8,9,10,11,12)
#データをまとめる
md = tuple(zip(month_tuple,day_tuple))
#print(md)
print(str(month) + '月は' + str(md[month-1][1]) + '日まであります')