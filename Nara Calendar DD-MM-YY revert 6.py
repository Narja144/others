# ======ERAS====================================================================
# Start of era Ra == 14/06/89
# Start of era Ne == 01/02/07
era = 726266 # is year one Ra
ene = 732707 # is year one Ne
# ======MONTH=OVERVIEW==========================================================
# MONTH  01 02 03 04 05 06 07 08 09 10 11 12
# DAYS   31 2? 31 30 31 30 31 31 30 31 30 31
# ======GET=MONTH===============================================================
def dam(mon):
    if mon in (1,3,5,7,8,10,12):
        return 0
    elif mon in (4,6,9,11):
        return 1
    else:
        return 2
# ======MINUS=DAYS==============================================================
def daq(mon,yer):
    if dam(mon) == 0:
        return 31
    elif dam(mon) == 1:
        return 30
    elif dam(mon) == 2:
        if leap(yer) == False:
            return 28
        else:
            return 29
# ======REVERT=DAYS=3===========================================================
def day(dat,yer):
    mon = 1
    while True:
        daf = daq(mon,yer)
        if dat > daf:
            dat -= daf
            mon += 1
        else:
            break
    dat = '%d/%d/'%(dat,mon)
    return dat
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
# ======REVERT=YEARS============================================================
def rev(dat):
    yer = 0
    while dat > 365:
        yer += 1
        if leap(yer) == True:
            dat -= 366
            if dat  >= 0:
                continue
            else:
                dat += 366
                yer -= 1
                break
        else:
            dat -= 365
    if dat != 0:
        yer += 1 # zero year not exist in gregorian
    return dat,yer
# ======REVERT=GREGORIAN=DATE=2=================================================
def dax(dat):
    if dat[-1] == '*':
        dat = int(dat[0:-1]) + ene
    elif dat.isnumeric() == True:
        dat = int(dat) + era
    elif dat[-3:] == ' ne':
        dat = int(dat[0:-3]) + ene
    elif dat[-3:] == ' ra':
        dat = int(dat[0:-3]) + era
    else:
        print('\n   >>> Incorrect input <<<')
        fed()
    dat,yer = rev(dat)
    dat = day(dat,yer)
    print('%s%d'%(dat,yer))
# ======
def fed():
    while True: # extra func for hom() in dax()
        dat = input('\nEnter a naryan date in format "YYYY":  ')
        dat = dat.lower()
        if dat == 'q':
            quit()
        elif dat == '0' or dat.isalpha() == True: # incorrect Error handling
            print('\n   >>> Incorrect input <<<')
            continue
        else:
            dax(dat)
# ======HOME====================================================================
def hom():
    print('''Type:\n"q"    for quit,\n"144"  for brahmian era,
"144*" for nordic era.''')
# 144 Ne for nordic era
# 144 Ra for brahmian era
    fed()
hom()
