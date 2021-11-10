zprava = "zluta"
posun = 3
sifra = ""

print()

for i in range(len(zprava)):
    if i < posun: #tady řešíme aby cyklus skončil až vyškrtáme všechny pismena
        sifra += zprava[i]
        for j in range(i+posun,len(zprava),posun):
            print(zprava[i])
            if j<len(zprava):
                sifra += zprava[j]
                print(zprava[j])
                print(sifra)
                
print(sifra)
print()

desifra = list()
desifra = [None]*len(sifra)
i = 0
ukazatel = 0
while ukazatel < len(zprava):
    desifra[i] = sifra[ukazatel]
    j = 1
    while i+j*posun < len(sifra):
        desifra[i+j*posun] = sifra[ukazatel+1]
        j += 1
        ukazatel += 1
    i += 1
    ukazatel += 1

print(desifra)
        
