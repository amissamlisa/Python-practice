from random import randint 

#すべてのメニューをまとめたリストを作成する
menu_list = ['menuA','menuB','menuC','menuD','menuE',]
#それぞれのメニューにおける空のリストを作成する
menuA = []
menuB = []
menuC = []
menuD = []
menuE = []
order_num = int(input('注文者数の数: ')) #数字として扱いたい　int
for i in range(1, order_num + 1): #注文者数分のメニューの出力行う
    rn = randint(0,4)  #0～4までの乱数を生成 
    st = str(i) + '人目のメニュー: ' + menu_list[rn] #menu_listのインデクスをランダムに
    print(st)
    #インデクス番号からそれぞれのメニューのリストに順番の数字を追加
    if rn == 0:
        menuA.append(i)
    elif rn == 1:
        menuB.append(i)
    elif rn == 2:
        menuC.append(i)
    elif rn == 3:
        menuD.append(i)
    else:
        menuE.append(i)

print('オーダー一覧')
#辞書の作成
menu_dict = {'menuA':menuA,'menuB':menuB,'menuC':menuC,'menuD':menuD,'menuE':menuE,}

print(menu_dict)

num_per_one = int(input('ひとつのメニューを作れる個数: '))

j = 1 
while j <= order_num:
    #menu_dictのキーと値（リスト）をとり出す
    for key,li in menu_dict.items():
        if len(li) < num_per_one and menu_dict[key] != [] and j in li: #リストの値の要素の数が一つのメニューを作れる個数より小さいとき
            print(str(key) + 'を作ります:' + str(li))
    
            for f in range(0,len(li)):
                li.remove(li[0])
        elif len(li) >=  num_per_one and menu_dict[key] != [] and j in li:#リストの値の要素の数が一つのメニューを作れる個数以上のとき
            extracted_li = li[:num_per_one] 
            print(str(key) + 'を作ります:' + str(extracted_li))
            
            for s in range(0,num_per_one):
                li.remove(extracted_li[s])
    j = j + 1   