print('とある科目の成績を判定します')
score = int(input('得点: '))
actual_score_tuple = (0,60,70,80,90)
grade_tuple = ('XX','C','B','A','AA')
t = list(zip(actual_score_tuple,grade_tuple))
print(t)
if t[4][0] <=  score:
    print('成績:' + str(t[4][1]))
elif t[3][0] <= score:
    print('成績:' + str(t[3][1]))
elif t[2][0] <= score:
    print('成績:' + str(t[2][1]))
elif t[1][0] <= score:
    print('成績:' + str(t[1][1]))
else:
    print('成績:' + str(t[0][1]))