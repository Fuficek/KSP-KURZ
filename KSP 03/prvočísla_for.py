t=open('out.txt', 'w')

num1 = int(input("Zadejte počet čísel: "))
x = 0 

while x < num1: 
    num2 = int(input("Zadej číslo: "))
    y = 2

    while y < num2 :
        resid= num2%y
        
        if resid == 0:
            t.write("SLOZENE\n")
            break
        y = y + 1 
    
    else: 
        t.write("PRVOCISLO\n")
    x = x + 1 
