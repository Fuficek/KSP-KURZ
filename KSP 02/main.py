
f=open('C:/Users/Matěj/Documents/schul/ZAL/KSP/ctení_vstupu/05.in')
obsah=f.readlines()


x = obsah[0]
l = len(x)-1
a = int(obsah[1])
b = int(obsah[2])
c = int(obsah[3])
d = int(obsah[4])


#print(x[a:a+b])
#print(x[c:l-d])

print(x[l-1])
print(a)
print(b)
print(c)
print(d)


f=open('C:/Users/Matěj/Documents/schul/ZAL/KSP/susssy.txt', "w")
f.write(x[a:a+b]+"\n")
f.write(x[c:l-d]+"\n")
f.close()
