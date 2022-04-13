# co je integrál??
# y = x^2
def VratHodnotu(x):
    return x**2

def ObdelnikovaMetoda(a, b):
    hodnota = (b-a)*pow((a+b)/2,2)
    return hodnota
print(ObdelnikovaMetoda(1, 3))
print()

def LichobeznikovaMetoda(a, b):
    f_a = VratHodnotu(a)
    f_b = VratHodnotu(b)
    hodnota = (b-a) *(f_a+f_b)/2
    return hodnota
print(LichobeznikovaMetoda(1, 3))
print()

#h= (b-a)/n=(4-1)/3= 1
#S=h[f(x0+0,5h­)+f(x1+0,5h)+f(x2+0,5h)]

def SlozenaObdelnikovaMetoda(a,b,n):
    h = (b-a)/n
    vysledek = 0
    for i in range(n):
        vysledek += ObdelnikovaMetoda(a+i*h,a+(i+1)*h)
        #vysledek += VratHodnotu((2*a+i*h+(i+1)*h)/2)
        #vysledek += VratHodnotu((2*a+(2*i+1)*h)/2)
    #return vysledek*h
    return vysledek
print(SlozenaObdelnikovaMetoda(1,3,50000))
print()

def SlozenaLichobeznikovaMetoda(a,b,n):
    h = (b-a)/n
    vysledek = VratHodnotu(a)+VratHodnotu(b)
    vysledek = 0
    for i in range(1,n):
        vysledek += VratHodnotu(a+i*h)
    vysledek = vysledek * 2
    vysledek += VratHodnotu(a)+VratHodnotu(b)
    vysledek = vysledek*h/2
    return vysledek
print(SlozenaLichobeznikovaMetoda(1,3,50))
print()
