#練習問題037
print('リストstudent')
stu_li = ['18115000', '18115005','18115010']
print(stu_li)
print('修正したリスト')
stu_li_f = []
for i in range(0,len(stu_li)):
    stu_li_2 = stu_li[i].replace('1811','1812',1)
    stu_li_f.append(stu_li_2)
print(stu_li_f)