text = "wikipedie".upper()
print(text)
heslo = "bagrbagr".upper()
sifra = ""
desifra = ""

for i in range(len(text)):
    sifra += chr((ord(text[i]) + ord(heslo[i % len(heslo)]))% 26 + 65)
print(sifra)

for i in range(len(sifra)):
    desifra += chr((ord(sifra[i]) - ord(heslo[i % len(heslo)]))% 26 + 65)
print(desifra)
