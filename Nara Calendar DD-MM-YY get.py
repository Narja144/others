# ======LEAP=YEAR===============================
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
# ======ERAS====================================================================
# Start of era Ra == 14/06/89
# Start of era Ne == 01/02/07
era = 726266 # is year zero Ra
ene = 732707 # is year zero Ne
# ======NUMBER=OF=DAYS==========================================================
def dan(dat):
    if dat[-1] == '+':
        per = ''
        dat = dat[0:-1]
    elif dat[-1] == '*':
        per = '19'
        dat = dat[0:-1]
    else:
        per = '20'
    ad1,mo1,ye1 = map(str, dat.split('/'))
    ye1 = per + ye1
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
    rer = das - era
    ren = das - ene
    print('\nIn the Nordic era is year: '+str(ren)+" Ne\nIn the Brahma's era is year: "+str(rer)+' Ra')
# ======CALL======================================
def hom():
    print('''Type:\n"q"           for quit,\n"DD/MM/YY"    for date DD/MM/20YY
"DD/MM/YY*"   for date DD/MM/19YY\n"DD/MM/YYYY+" for date DD/MM/YYYY''')
    while True:
        dat = input('\nEnter the gregorian date in format "DD/MM/YY":  ')
        dat = dat.lower()
        if dat == 'q':
            break
        elif dat.isalpha() or dat.isdecimal(): # incorrect Error handling
            print('\n   >>> Incorrect input <<<')
            continue
        else:
            dan(dat)
hom()
