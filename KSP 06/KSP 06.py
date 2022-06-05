def num_conversion(cislo, base):
    global collection
    collection = []
    while cislo != 0:
        zbytek = cislo % base
        cislo = cislo // base
        collection.append(zbytek)
    return collection

def pocet_zeros(collection):
    global zeros
    zeros = 0
    for cislo in collection:
        if cislo == 0:
            zeros += 1
        else:
            break
    return zeros

cislo = int(input("Zadej číslo: "))
max_pocet_nul = 0
zeros = 0
base = 2
breakstatement = True
collection = []

while True:
    zeros = pocet_zeros(collection)
    collection = num_conversion(cislo, base)
    if zeros > max_pocet_nul:
        max_pocet_nul = zeros
        vysledek = base
    base += 1
    if len(collection) <= max_pocet_nul:
        print("Soustava ve které má číslo největší počet nul:", vysledek-1)
        breakstatement = False
        print(breakstatement)
        break

#Je to hodně kostrbatý kód a řádek 2 - 7 je z minulého cvičení. A řádek 11 - 15 mi pomohl přítel který mě učí programovat.
#kód jinak chápu