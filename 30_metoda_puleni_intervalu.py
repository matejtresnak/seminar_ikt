#x**3 - 5x**2 +5x
"""
def faktorial(n):
    if (n>1):
        return n*faktorial(n-1)
    return 1

print(faktorial(5))

"""

def vrat_funkcni_hodnotu(a):
    return pow(a, 3)-5*(a,2)+5*a

def puleni_intervalu(a,b):
    global a
    global b
    s = (a+b)/2
    f_a = vrat_funkcni_hodnotu(a)
    f_b = vrat_funkcni_hodnotu(b)
    f_s = vrat_funkcni_hodnotu(s)
    if (f_a*f_s < 0):
        b = s
    if (f_b*f_s < 0):
        a = s
    if f_s == 0:
        a = b
    
a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
f_a = vrat_funkcni_hodnotu(a)
f_b = vrat_funkcni_hodnotu(b)
if (f_a*f_b) < 0:
    while (abs(a-b)>0.0001):
        puleni_intervalu(a,b)
else:
    print("nenašel jsem kořen")
