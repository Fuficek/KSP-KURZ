soubor = open("03.in", "r")

pocet_cisel_n = int(soubor.readline())

seznam_A = []

for i in range (pocet_cisel_n):
    prvky_A = int(soubor.readline())
    seznam_A.append(prvky_A)

print(seznam_A)

pocet_cisel_m = int(soubor.readline())


seznam_B = []

for i in range (pocet_cisel_m):
    prvky_B = int(soubor.readline())
    seznam_B.append(prvky_B)

print(seznam_B)

pocet_dvojic = 0
for x in seznam_A:
    for y in seznam_B:
        if x == y:
            pocet_dvojic+=1

print(pocet_dvojic)

print(type(pocet_dvojic))

pocet_dvojic2 = str(pocet_dvojic)

vystup = open("out2.txt", "w")
vystup.write(pocet_dvojic2)
vystup.close()