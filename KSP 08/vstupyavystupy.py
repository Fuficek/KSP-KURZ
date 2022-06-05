'''Matěj Hrabal P1B 2022'''

import math

def isprime(N):
    prime_num = True
    for j in range(2, N):
        if (N % j) == 0:
            prime_num = True
            return True
            break

f=open("01.in")
obsah = f.readlines()
N=int(obsah[0])

odmocnina = math.ceil(math.sqrt(N))
y = 0
y = odmocnina // 2
x = odmocnina // 2

#Vytvareni herniho pole
radek = " " * odmocnina
sloupce = []
for i in range(odmocnina):
    sloupce.append(radek)
#Zapíšeme X do středu tabulky
sloupce[y] = sloupce[y][:x] + "X" + sloupce[y][x+1:]
smer = 0 #0=vpravo, 1=nahoru, 2=doleva, 3= dolu

for i in range(2,N+1):
    if smer == 0:
        x += 1
        if sloupce[y-1][x] == " ":
            smer = 1

    elif smer == 1:
        y -= 1
        if sloupce[y][x-1] == " ":
            smer = 2

    elif smer == 2:
        x -= 1
        if sloupce[y+1][x] == " ":
            smer = 3

    elif smer == 3:
        y += 1
        if sloupce[y][x+1] == " ":
            smer = 0

    if isprime(i) == True:
        sloupce[y] = sloupce[y][:x] + "." + sloupce[y][x+1:]
    else:
        sloupce[y] = sloupce[y][:x] + "#" + sloupce[y][x+1:]


soubor = input("Zadej název souboru pro zápis spirály: ")
d=open(soubor,"w")
for spirala in sloupce:
    d.write(spirala +"\n")
d.close()
