# ======LEAP=YEAR===============================================================
def leap(yer):
    yer = int(yer)
    if yer % 4 != 0:
        return False
    elif yer % 4 == 0:
        if yer % 100 == 0:
            if yer % 400 == 0:
                return True
            else:
                return False
        elif yer % 100 != 0:
            return True
# ======MONTH=OVERVIEW==========================================================
# MONTH  01 02 03 04 05 06 07 08 09 10 11 12
# DAYS   31 2? 31 30 31 30 31 31 30 31 30 31
# ======NUMBER=OF=DAYS==========================================================
def dan(dt1):
    ad1,mo1,ye1 = map(str, dt1.split('/'))
    ad1,mo1,ye1 = int(ad1),int(mo1),int(ye1)
    m31 = (1,3,5,7,8,10,12)
    m30 = (4,6,9,11)
    mFe = 2
    dm1 = 0
    rm1 = range(1,mo1)
    for i in rm1:
        if i in m31:
            dm1 += 31
        elif i in m30:
            dm1 += 30
        elif i == mFe and leap(ye1) == True:
            dm1 += 29
        elif i == mFe and leap(ye1) == False:
            dm1 += 28
    dy1 = 0
    ry1 = range(1,ye1)
    for i in ry1:
        if leap(i) == False:
            dy1 += 365
        if leap(i) == True:
            dy1 += 366
    das = ad1 + dm1 + dy1
    print('Number of days from start of Gregorian era: '+str(das))
# ======CALL======================================
def hom():
    print('Press "q" for quit.')
    while True:
        dt1 = input('\nEnter the gregorian date in format "DD/MM/YY":  ')
        dt1 = dt1.lower()
        if dt1 == 'q':
            break
        elif dt1.isalpha() or dt1.isdecimal(): # incorrect Error handling
            print('\n   >>> Incorrect input <<<')
            continue
        else:
            dan(dt1)
hom()
