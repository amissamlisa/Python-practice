#練習問題026
st = input('入力: ')

if '長' in st:
    ch_sh = st.replace('長','短')
    print(ch_sh)
elif '短' in st:
    ch_lo = st.replace('短','長')
    print(ch_lo)