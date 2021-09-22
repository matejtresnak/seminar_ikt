#ax + b = 0
#x=(-b)/a

while(True):
    try:
        a = float(input("zadej a: "))
        b = float(input("zadej b: "))

        break
    except:
        continue

def linearni_rovnice(a, b):
    a=a
    b=b
    if a != 0:
        x=-b/a
        if a > 0:
            znamenko_a = "+"
        if a < 0:
            znamenko_a = "-"
        a=abs(a)
        clen_1 = "{znamenko_a}{a}x".format(znamenko_a=znamenko_a,a=a)

        if b > 0:
            znamenko_b = "+"
        if b < 0:
            znamenko_b = "-"
        b=abs(b)
        clen_2 = "{znamenko_b}{b}}".format(znamenko_b=znamenko_b,b=b)
        rovnice = clen_1 + clen_2
        
    if a == 0 and b == 0:
        x="nekonečno řešení"
    if a == 0 and b != 0:
        x="neni řešní"


    return x, rovnice

print(linearni_rovnice(a, b))
