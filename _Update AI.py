# ======
import os
import shutil
# ======INITIALIZATION==========================================================
shutil.copy('Anund.per','__Base__')
# ======RENAME=LIST=============================================================
sez = ['Anund','Beowulf','Ernest','Grettir','Harald']
for i in sez:
    i = str(i)
    i = i+'.per'
    shutil.copy('__Base__',i)
# ======CLOSING=================================================================
os.remove('__Base__')
# ======QUIT====================================================================
input('Press ENTER for quit.')
