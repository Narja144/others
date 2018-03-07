# ======IMPORTING===============================================================
from agescx import *
from random import choice
# ======CONVERTER=3=============================================================
# def rin(old,new,cac=99):
def lid():
    a = 0
    lis = []
    for u in xen.units: # > exchange units 2 <
        lis += [u.type]
    # print(sorted(lis))
    return lis
# ======UNIQIFY===============
def niq(): # order preserving
   seq = lid()
   qec = []
   for i in seq:
       if i not in qec:
           qec.append(i)
   # return qec
   print(sorted(qec))
# ======SORT===============
# def qin():

# from collections import Counter
# c = Counter(car_list)
# cars = [model for model in c if c[model] == 1 ]
# print cars
# ['honda', 'ford']

# cars = [...] # A list of Car objects.
# models = {car.model for car in cars}

    #     if u.type == old:
    #         a += 1 # count
    #         u.type = new # exchange
    #         if cac == 99:
    #             continue
    #         else:
    #             u.angle = choice(cac) # angle converter
    #     else:
    #         continue
    # if a != 0:
    #     print('%d units[%d] replaced by units[%d].\n'%(a,old,new)+'-'*42)
# ======MASS=CONVERTER=2========================================================
def qel(scx):
    print('Loaded from %s.scx'%(scx))
    global xen
    xen = Scenario('%s.scx'%(scx))
    print('-'*42)
    niq()
    # rin(709,462,(3,4,5)) # Cactus
    # rin(38,82)
    # rin(859,580) # Flower Bed
    # rin(816,479) # Macaw
    # rin(835,551) # Mustang
    # rin(822,240) # Javelina
    # rin(818,241) # Plant
    # rin(809,242) # Stump
    # rin(833,257) # Kalkun
    # rin(812,258) # Jaguar
    # print('Saved into %s.scx'%(scx))
    # xen.save('%s.scx'%(scx))
    print('='*42)
# ======EXCHANGE=LIST===========================================================
print('='*42)
qel('0 Pandora')
# qel('0 First Battle of Panipat')
# qel('0 The Forest Kingdom 1 (2017_02_25)')
# qel('0 The two worlds')
# qel('0 Wind of the North')
# qel('0 Yellow River Burning Bright')
qel('1 Gwynheim')
qel('1 Istar')
qel('1 Nansac')
qel('1 Narnia Ariver')
qel('1 Sumeeru')
qel('1 Xaphira - Anarchy')
# qel('1 Xaphira - Aliances')
# qel('1 Xaphira - Besieged')
# ======QUIT====================================================================
input('Press ENTER for quit.')
