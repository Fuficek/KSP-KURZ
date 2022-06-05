f=open("03.in")
obsah = f.readlines()
numA=int(obsah[0])
numB=int(obsah[1])
print("CisloA = ", numA)
print("CisloB = ", numB)

def b_p_divider(nA,nB):
    if nA < nB:
        smaller = nA
    else:
        smaller = nB
    for i in range(2,smaller+1):
        if nA % i == 0 and nB % i == 0:
            divider = i
    return divider

def b_p_divider_better(u,w):
    while w != 0:
        r = u % w
        u = w
        w = r
    return u

def b_p_divider_rekurz(u,w):
    if w == 0:
        return u
    return b_p_divider_rekurz(w,u % w)

def s_p_multiplier(nA,nB):
    multiplier = 0
    for i in range(1,nA*nB+1):
        if i % nA == 0 and i % nB == 0:
            multiplier = i
            break
    return multiplier

def s_p_multiplier_better(nA,nB):
    if nA < nB:
        bigger = nB
    else:
        bigger = nA
    multiplier = 1
    for i in range(bigger,nA*nB+1,bigger):
        if i % nA == 0 and i % nB == 0:
            multiplier = i
            break
    return multiplier

def s_p_multiplier_nsd(nA,nB):
    return nA*nB / b_p_divider(nA,nB)

print("Největší společný dělitel je:", b_p_divider(numA,numB), "*Vypočítáno horší metodou*")
print("Největší společný dělitel je:", b_p_divider_better(numA,numB) , "*Vypočítáno lepší metodou*")
print("Největší společný dělitel je:", b_p_divider_rekurz(numA,numB) , "*Vypočítáno rekurzivni metodou*")
print("Největší společný dělitel je:", s_p_multiplier(numA,numB), "*Vypočítáno horší metodou*")
print("Největší společný dělitel je:", s_p_multiplier_better(numA,numB),"*Vypočítáno lepší metodou*")
print("Největší společný dělitel je:", s_p_multiplier_nsd(numA,numB),"*Vypočítáno pomocí nsd*")
f.close()

