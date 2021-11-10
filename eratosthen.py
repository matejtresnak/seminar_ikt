#vypíše všechna prvnočísla menší než n

n = 1000

prvocisla = list()

for i in range(n+1):
    prvocisla.append(True)
for i in range(2, len(prvocisla)):
    j = 2
    if prvocisla[i] == False:
        continue
    while i*j<len(prvocisla):
        prvocisla[i*j] = False
        j += 1
print(prvocisla[2:])

for i in range(2, len(prvocisla)):
    if prvocisla[i] == True:
        print(i)
