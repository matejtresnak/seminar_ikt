#100=2*2*5*5
#Eratosthenovo síto

n = 1000

delitele = list()
i = 2
while (n>1):
    while (n%i == 0):
        delitele.append(i)
        n = n/i
        print(n)
    i += 1

print(delitele)


pocty = {}

for i in delitele:
    if i not in pocty:
        pocty[i] = 1
    else:
        pocty[i] += 1

vystup = str(n) + " = "
i = 0
while i<len(delitele):
    vystup += str(delitele[i])+"^"
    cetnost = delitele.count(delitele[i])
    i += cetnost
    vystup += str(cetnost)
    if i<len(delitele):
        vystup += "*"
print(vystup[0:len(vystup)])
"""
soucin = ""
for i in pocty:
    soucin += str(i)


print(soucin)
"""
