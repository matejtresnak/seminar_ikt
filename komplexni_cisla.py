import math

class Komplexni_cislo:
    def __init__(self, a, b, uhel=None):
        self.a = a
        self.b = b
"""
    @classmethod
    def Gon_exp(size, arg):
        realna_cast = size*math.cos(math.radians(arg))
        komplexni_cast = size*math.sin(math.radians(arg))
        instance = Komplexni_cislo(cls, )
"""
    @staticmethod
    def Velikost(x):
        realna_cast = x.a
        komplexni_cast = x.b
        return (realna_cast**2+komplexni_cast**2)**(1/2)
    
    @staticmethod
    def Soucet(x,y):
        realna_cast = x.a + y.a
        komplexni_cast = x.b + y.b
        vysledek = Komplexni_cislo(realna_cast, komplexni_cast)
        return vysledek
    
    @staticmethod
    def Rozdil(x,y):
        realna_cast = x.a - y.a
        komplexni_cast = x.b - y.b
        vysledek = Komplexni_cislo(realna_cast, komplexni_cast)
        return vysledek

    @staticmethod
    def Soucin(x,y):
        realna_cast = x.a * y.a - x.b * y.b
        komplexni_cast = x.a * y.b + x.b * y.a
        vysledek = Komplexni_cislo(realna_cast, komplexni_cast)
        return vysledek

    @staticmethod
    def Podil(x,y):
        realna_cast = (x.a*y.a+x.b*y.b)/(y.a**2+y.b**2)
        komplexni_cast = (x.b*y.a-x.a*y.b)/(y.a**2+y.b**2)
        vysledek = Komplexni_cislo(realna_cast, komplexni_cast)
        return vysledek

    def __str__(self):
        if self.b > 0:
            return str(self.a) + "+" + str(self.b) + "i"
        elif self.b < 0:
            return str(self.a) + "+(" + str(self.b) + ")i"
        else:
            return str(self.a)


x = Komplexni_cislo(-6, 4)
print(str(x))

velikost_x = Komplexni_cislo.Velikost(x)
print("velikost:" + str(velikost_x))

y = Komplexni_cislo(1, -1)
print(str(y))

velikost_y = Komplexni_cislo.Velikost(y)
print("velikost: " + str(velikost_y))

soucet = Komplexni_cislo.Soucet(x,y)
print("soucet: " + str(soucet))

rozdil = Komplexni_cislo.Rozdil(x,y)
print("rozdil: " + str(rozdil))

soucin = Komplexni_cislo.Soucin(x,y)
print("soucin: " + str(soucin))

podil = Komplexni_cislo.Podil(x,y)
print("podil: " + str(podil))
