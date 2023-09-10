print('0 : グー , 1 : チョキ, 2 : パー')
import random
rn = random.randint(0,2)
#print(str(rn))#乱数生成を表示
rps = int(input('手を選択: '))
#コンピュータの手を表示
if rn == 0:
     print('コンピュータ: グー')
elif rn == 1:
    print('コンピュータ: チョキ')
else:
    print('コンピュータ: パー')
#勝ち負けあいこの判断表示
if rn == rps:
    print('あいこです')
elif rn == 0 and rps == 1 or rn == 1 and rps == 2 or rn == 2 and rps == 0:
    print('あなたの負けです')
else:
    print('あなたの勝ちです')