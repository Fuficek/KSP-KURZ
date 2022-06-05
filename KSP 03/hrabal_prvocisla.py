import math


f=open('03.in')
t=open('out.txt', 'w')
obsah = f.readlines()

def prvocislo(cislo):
    b = 2
    while b<=math.sqrt(cislo):
        if cislo%b<1:
            return False
        b=b+1
    return cislo>1
run=0
N = int(obsah[0])
for i in range(N+1):
    cislo_from_user = int(obsah[0+run])
    if prvocislo(cislo_from_user) == True:
        t.write("PRVOCISLO\n")
    if prvocislo(cislo_from_user) == False:
        t.write("SLOZENE\n")
    run=run+1



    '''FUNGUJE JEN MUSÍŠ SMAZAT PRVNÍ ČÍSLO ZE VSTUPU!!!'''