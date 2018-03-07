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
# ======MONTH=DAYS===============================================
def mon(mod,yer):
    m31 = (1,3,5,7,8,10,12)
    m30 = (4,6,9,11)
    res = 0
    for i in range(1,mod):
        if i in m31:
            res += 31
        elif i in m30:
            res += 30
        elif i == 2 and leap(yer) == True:
            res += 29
        elif i == 2 and leap(yer) == False:
            res += 28
    return res
# ======YEAR=DAYS=======================================================
def yed(yer):
    res = 0
    for i in range(1,yer):
        if leap(i) == False:
            res += 365
        if leap(i) == True:
            res += 366
    return res
# ======MONTH=TABLE======================================
# MONTH  01 02 03 04 05 06 07 08 09 10 11 12
# DAYS   31 2? 31 30 31 30 31 31 30 31 30 31
# ======NUMBER=OF=DAYS====================================
def dan(dt1,dt2):
    ad1,mo1,ye1 = map(int, dt1.split('/'))
    ad2,mo2,ye2 = map(int, dt2.split('/'))
    dm1 = mon(mo1,ye1)
    dm2 = mon(mo2,ye2)
    dy1 = yed(ye1)
    dy2 = yed(ye2)
    das = dy2 - dy1 + dm2 - dm1 + ad2 - ad1 + 1
    print('\nThe period (in days) between these dates is: '+str(das))
# ======CALL======================================
def hom():
    while True:
        dt1 = input('\nEnter the first date in format "DD/MM/YYYY":  ')
        dt2 = input('Enter the second date in format "DD/MM/YYYY": ')
        dan(dt1,dt2)
hom()
