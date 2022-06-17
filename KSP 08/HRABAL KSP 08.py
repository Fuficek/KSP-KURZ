'''Matěj Hrabal P1B 2022 KSP 08 Vstupy a výstupy.'''

import math #import modulu math

#funkce pro zjištění zda je číslo prvočíslo
def isprime(N):
    prime_num = True
    for j in range(2, N):
        if (N % j) == 0:
            prime_num = True
            return True
            break
#odstraneni prvniho znaku
def remove_first_letter(list_of_strings):
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i][1:] #odstraneni prvniho znaku
    return list_of_strings   #vraceni listu
#odstraneni posledniho znaku
def remove_last_letter(list_of_strings):
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i][:-1] #odstraneni posledniho znaku
    return list_of_strings #vraceni listu

#hlavni funkce
def main():
    N = input("Zadejte N: ") #zadání N
    if any(char.isalpha() for char in str(N)):
        exit("Nesmí být písmeno")
    else:
        N = int(N)
    if N < 0:
        exit("Nesmí být záporné číslo") #kontrola zda N není záporné
    elif N == 0:
        exit("Nesmí být nulové číslo")
    elif N != int(N):
        exit("Nesmí být desetinné číslo")
    odmocnina = math.ceil(math.sqrt(N)) #odmocnina
    y = odmocnina // 2
    x = odmocnina // 2

    radek = " " * odmocnina + " " #vytvoření řádku
    sloupce = [] #vytvoření listu pro sloupce
    for i in range(odmocnina):
        sloupce.append(radek) #vložení řádku do listu

    sloupce[y] = sloupce[y][:x] + "X" + sloupce[y][x+1:] #zapíšeme X do středu tabulky

    smer = 0 #definovaní smeru [0=vpravo, 1=nahoru, 2=doleva, 3= dolu]
    for i in range(2,N+1):
        if smer == 0: #smer vpravo
            x += 1
            if sloupce[y-1][x] == " ":
                smer = 1 #zmena smeru na nahoru
        elif smer == 1: #smer nahoru
            y -= 1
            if sloupce[y][x-1] == " ":
                smer = 2 #zmena smeru na doleva
        elif smer == 2: #smer doleva
            x -= 1
            if sloupce[y+1][x] == " ":
                smer = 3 #zmena smeru na dolu
        elif smer == 3: #smer dolu
            y += 1
            if sloupce[y][x+1] == " ":
                smer = 0 #zmena smeru na vpravo
        if isprime(i) is True: #pokud je číslo prvočíslo
            sloupce[y] = sloupce[y][:x] + "." + sloupce[y][x+1:] #zapíšeme . do tabulky
        else: #pokud je číslo neprvočíslo
            sloupce[y] = sloupce[y][:x] + "#" + sloupce[y][x+1:] #zapíšeme # do tabulky

    #pokud je poslední sloupec prázdný, tak ho odstraním
    if sloupce[y][-1] == " ":
        sloupce = remove_last_letter(sloupce)
    #pokud je první sloupec prázdný, tak ho odstraním
    if sloupce[y][0] == " ":
        sloupce = remove_first_letter(sloupce)
    #pokud poslední řádek obsahuje jen " ", tak ho odstraním
    if sloupce[-1] == " " * len(sloupce):
        sloupce = sloupce[:-1]

    #zapíše spirálu do souboru
    soubor = input("Zadej název souboru pro zápis spirály: ") #zadání názvu souboru
    d = open(soubor, "w") #otevření souboru
    for spirala in sloupce:
        d.write(spirala + "\n") #zapis spirály do souboru
    d.close() #zavření souboru
    print(f"Spirála byla úspěšně zapsána do souboru {soubor}") #vypisování názvu souboru
#spustení programu
if __name__ == "__main__":
    main()