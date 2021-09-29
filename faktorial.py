"""
fce, která vrátí faktoriál
"""

import math

def faktorial_1(n): #nefunguje
    opakovani = n
    while opakovani != 1:
        opakovani -= 1
        vysledek = (opakovani + 1) * opakovani  
        print(vysledek)
    return vysledek

def faktorial_2(n):
    if (n<0):
        return math.nan
    soucin = 1
    while n>0:
        soucin *=n
        n -= 1
    return soucin

def faktorial_3(n):
    if (n>1):
        return n*faktorial_3(n-1)
    return 1



    
print(faktorial_3(5))
