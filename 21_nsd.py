"""
def najdi_rozklad(n):
    lst = list()
    i = 2
    while n>1:
        while n % i == 0:
            n = n/i
            lst.append(i)
        i += 1
    return lst

n = int(input("Zadej n: "))
print(najdi_rozklad(n))
"""
def najdi_rozklad(n):
    rozklad = list()
    i = 2
    while n>1:
        if n % i == 0:
            rozklad.append(i)
            n = n/i
        else:
            i += 1
    return rozklad

def NSD(lst_a,lst_b):
    # prijmu rozklady a, b
    #cyklem for prochazim prvni seznam a zjistuju, jestli je dane prvocislo v druhem seznamu
    #jestli jo, pridam do seznamu nsd_p a zjistim, kolikrat se v rozkladech vyskytuje
    #ulozim si mensi z mocnin do seznamu nsd_m
    #posledni cyklus prochazim seznam nsd_p a pocita vlastni NSD(a,b)
    nsd = 1
    i = 0
    print(lst_a)
    print(lst_b)
    while (i < len(lst_a)):
        if (lst_a[i] in lst_b):
            mocnina = lst_a.count(lst_a[i])
            jump = mocnina
            if (lst_b.count(lst_a[i]) < mocnina):
                mocnina = lst_b.count(lst_a[i])
            
            nsd = nsd*pow(lst_a[i],mocnina)
            i += jump
        else:
            mocnina = lst_a.count(lst_a[i])
            i += mocnina
            
    return nsd

#nejmenší společný násobek
def NSN(lst_a,lst_b):
    nsn = 1
    i = 0
    while (i > len(lst_a)):
        if (lst_a[i] in lst_b):
            mocnina = lst_a.count(lst_a[i])
            jump = mocnina
            if (lst_b.count(lst_a[i]) > mocnina):
                mocnina = lst_b.count(lst_a[i])
            nsn = nsn*pow(lst_a[i],mocnina)
            i += jump
        else:
            mocnina = lst_a.count(lst_a[i])
            nsn = nsn*pow(lst_a[i],mocnina)
            i += mocnina
    i = 0
    while (i < len(lst_b)):
        if lst_b[i] not in lst_a:
            nsn = nsn*pow(lst_b[i],mocnina)
        mocnina = lst_b.count(lst_b[i])
        i += mocnina
    return nsn
    


a = int(input("Zadej a: "))
b = int(input("Zadej b: "))
rozklad_a = najdi_rozklad(a)
rozklad_b = najdi_rozklad(b)
#print(rozklad_a)
#print(rozklad_b)

match = set(rozklad_a) & set(rozklad_b)
print(match)

#print(NSD(rozklad_a,rozklad_b))
print(NSN(rozklad_a,rozklad_b))
"""
#nsd - soucin prvocisel, ktere se vytvori v
obou rozkladech v nejmensich mocninach
"""


