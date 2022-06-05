soubor = open("04.in", "r")

num = int(soubor.readline())

cisla = []

print(num)

for x in range(num):
    cislo = int(soubor.readline())
    cisla.append(cislo)

    for y in range(2, cislo): 
        resid = cislo % y


        if resid == 0: 
           vystup = open("out01.txt", "w")
           vystup.write("SLOZENE")
           vystup.close()
           break 
    
    else:
        vystup = open("out01.txt", "w")
        vystup.write("PRVOCISLO")
        vystup.close() 