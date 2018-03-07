# ======IMPORTING===============================================================
from agescx import *
from random import choice
# ======CONVERTER=3=============================================================
def rin(old,new,cac=99):
    a = 0
    for u in xen.units: # > exchange units 2 <
        if u.type == old:
            a += 1 # count
            u.type = new # exchange
            if cac == 99:
                continue
            else:
                u.angle = choice(cac) # angle converter
        else:
            continue
    if a != 0:
        print('%d units[%d] replaced by units[%d].\n'%(a,old,new)+'-'*42)
# ======LIST=OF=UNITS===========================================================
def rix():
# Narja's
    # rin(859,580) # Flower Bed
    # rin(835,551) # Mustang
    # rin(833,257) # Kalkun
    # rin(240,822) # Javelina OLD
    # rin(818,14) # Plant
    # rin(816,479) # Macaw
    # rin(258,812) # Jaguar OLD
    # rin(284,399) # Tree TD > Tree A
    # rin(401,399)
    # rin(415,242) # Tree Stump
    # rin(77,38) # Elite Sword > Knight
    # rin(317,553) # E Conquistor > E Cataphract
    # rin(38,77) # Knight > Elite Sword
    # rin(38,39) # Knight > Raider
    # rin(39,38) # Raider > Knight
    # rin(553,38) # Elite Cataphract > Knight
    # rin(349,351) # Oak Tree > Palm Tree
    # rin(809,242) # Stump
    # rin(351,414,(1,3,6,7,9,10,11,12)) # Palm > Jungle Tree
    # rin(351,414,(3,6,7)) # Palm > 3_Jungle Tree
    # rin(348,414,(3,6,7)) # Bamboo > 3_Jungle
    # rin(709,462,(3,4,5)) # Cactus
    # rin(623,395) # Rock
# Others
    # rin(865,208) # Rubble 3*3
    # rin(864,207) # Rubble 2*2
    # rin(863,206) # Rubble 1*1
    # rin(858,497) # Broken Cart
    # rin(855,245) # Old Stone Head
    # rin(838,453) # King Sancho
    # rin(814,342) # Horse, WCL Scout
    # rin(785,427) # Wood Tower
    # rin(745,313) # Mountain 4
    # rin(744,312) # Mountain 3
    # rin(740,253) # Bridge A--Broken Bottom
    # rin(739,252) # Bridge A--Broken Top
    # rin(723,433) # Crater
    # rin(715,189) # Yurt Taiga Cooker
    # rin(714,188) # Yurt Taiga Cutter
    # rin(713,187) # Yurt Taiga Weaver
    # rin(667,507) # Gate4 3 Bars
    # rin(626,183) # Pavilion Knight
    # rin(625,182) # Pavilion Page
    # rin(624,184) # Pavilion King
    # rin(438,22) # Raft
    # rin(64,90) # Gate2 3 Bars
# ======MASS=CONVERTER=2========================================================
def qel(scx):
    print('Loaded from %s.scx'%(scx))
    global xen
    xen = Scenario('%s.scx'%(scx))
    print('-'*42)
    rix()
    print('Saved into %s.scx'%(scx))
    xen.save('%s.scx'%(scx))
    print('='*42)
# ======EXCHANGE=LIST===========================================================
print('='*42)
# qel('0 Pandora')
# qel('1 Gwynheim')
# qel('1 Istar')
# qel('1 Nansac')
# qel('1 Narnia Ariver')
# qel('1 Sumeeru')
# qel('1 Xaphira - Anarchy')
# qel('1 Xaphira - Aliances')
# qel('1 Xaphira - Besieged')
# ======QUIT====================================================================
input('Press ENTER for quit.')
