# ======BASE=LEVEL==============================================================
def nux(num):
    res = ''
    if num in range(1,10):
        res = str(num)
    elif num == 10:
        res = 'A'
    elif num == 11:
        res = 'B'
    else:
        res = '0'
    return res
# ======NEXT=LEVELS=============================================================
def rex(num,e):
    res, a = '', 0
    if num in range(1,12):
        res = '0'*e+nux(num)
    elif num in range(12,12**e):
        res = '0'+rex(num,e-1)
    elif num in range(12**e,12**(e+1)):
        while num > 12**e-1:
            num -= 12**e
            a += 1
        if a in range(1,10):
            res = str(a)+rex(num,e-1)
        elif a == 10:
            res = 'A'+rex(num,e-1)
        else:
            res = 'B'+rex(num,e-1)
    else:
        res = '0'*(e+1)
    return res
# ======GET=LEVEL===============================================================
def get(num,e):
    a, x = 0, num
    while x > 12**e-1:
        x -= 12**e
        a += 1
        if a == 12:
            a = 0
            e = get(num,e+1)
    if a >= 1:
        return e+1
    else:
        return e
# ======DUODECIMAL=CONVERTER====================================================
def con(num):
    e, res = get(num,1), ''
    if e == 1:
        res = nux(num)
    else:
        res = rex(num,e-1)
    print(res)
# ======HOME=PAGE===============================================================
def hom():
    while True:
        print('| DUODECIMAL (number) |  QUIT (q) |')
        ans = input('Please enter a input: ')
        if ans == 'q':
            break
        else:
            con(int(ans))
hom()
# Záporná čísla, skrze absolutní hodnotu.
# Exception of Errors
