#caesarova sifra
text = "abc"
posun = 3
sifra = ""
for i in range(len(text)):
    sifra += chr(ord(text[i])+posun)
print(sifra)

desifra = ""
for i in range(len(sifra)):
    desifra += chr(ord(sifra[i])-posun)

print(desifra)


#sifra pozpatku
text = "abc"
sifra = ""
for i in range(len(text)):
    sifra += chr(ord(text[len(text)-i-1]))
print(sifra)

desifra = ""
for i in range(len(sifra)):
    desifra += chr(ord(sifra[len(sifra)-i-1]))
print(desifra)


#sifra objedno písmeno
text = "abcdefgh"
sifra = ""
for i in range(0, len(text), 2):
    sifra += text[i]
for i in range(1, len(text), 2):
    sifra += text[i]
print(sifra)

desifra = ""
suda_poz = ""
licha_poz = ""
if (len(sifra)%2 == 0):
    mez = int(len(sifra)/2)
else:
    mez = int(len(sifra)/2+1)
suda_poz += sifra[0:mez]
licha_poz += sifra[mez:]
print(suda_poz)
print(licha_poz)
i = 0
for i in range(len(licha_poz)):
    desifra += suda_poz[i]
    desifra += licha_poz[i]
if len(suda_poz)>len(licha_poz):
    desifra += suda_poz[-1]
print(desifra)
