def s(st):
    if st == st[::-1]:
        x = 'True'
    else:
        x = 'False'
    return x


st = input('文字列: ')
print(s(st))
