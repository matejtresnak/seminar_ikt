bity_ASCII = 9

zprava = "Jak se máš?"

def Koduj_ASCII(text):
    kody = list()
    for i in range (len(text)):
        kody.append(ord(text[i]))
    return kody

def Dec_To_Bin(dec):
    bin_num = list()
    while (dec>0):
        bin_num.append(int(dec % 2))
        dec = int(dec/2)
    bin_num = bin_num[::-1]
    return bin_num

#print(Dec_To_Bin(70))

kody_DEC = Koduj_ASCII(zprava)
kody_BIN = list()

for i in range(len(kody_DEC)):
    kody_BIN.append(Dec_To_Bin(kody_DEC[i]))
    if (len(kody_BIN[i])<bity_ASCII):
        for j in range(bity_ASCII-len(kody_BIN[i])):
            kody_BIN[i].insert(0, 0)
kod = ""
for i in range(len(kody_BIN)):
    for j in range(len(kody_BIN[i])):
        kod += str(kody_BIN[i][j])
        
print(zprava)
print(kod)
print()

########### STRANA PŘÍJEMCE
def Rozdel_Retezec(kod, pocet):
    kody_Bin = list()
    for i in range(0, len(kod), pocet):
        kody_Bin.append(kod[i:i+pocet])
    return kody_Bin

def Bin_To_Dec(bin_num):
    dec_num = 0
    for i in range(len(bin_num)):
        bit = int(bin_num[i])
        if bit == 1:
            dec_num += pow(2, len(bin_num)-i-1)
    return dec_num

kody_bin = Rozdel_Retezec(kod, bity_ASCII)
kody_dec = list()
for i in range(len(kody_bin)):
    kody_dec.append(Bin_To_Dec(kody_bin[i]))
    
dekod = ""
for i in range(len(kody_dec)):
    dekod += chr(kody_dec[i])

print(dekod)


