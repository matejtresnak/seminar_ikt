"""
rodné číslo: rrmmddxxxx
706020
20.10.1970

"""
def vrat_datum_narozeni(rodne_cislo):
    if len(rodne_cislo) != 6:
        return "chyba"
    else:
        den = int(rodne_cislo[4:6])
        mesic = int(rodne_cislo[2:4])
        rok = int(rodne_cislo[0:2])

        lst = list()
        if den < 1 or den > 31:
            return "chyba"
        lst.append(str(den))
        pohlavi = "muž"
        if (mesic > 12):
            pohlavi = "žena"
            mesic -= 50
        if mesic < 0 or mesic > 12:
            return "chyba"
        lst.append(str(mesic))
        if rok<21:
            rok += 2000
        else:
            rok += 1900
        lst.append(str(rok))
        datum = ".".join(lst)
        return datum


rodne_cislo = str(input("zadej rodné číslo: "))
datum = vrat_datum_narozeni(rodne_cislo)
if rodne_cislo == "":
    print("chyba")
else:
    print(datum)
