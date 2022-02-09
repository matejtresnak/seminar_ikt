import copy

class Polynom:
    def __init__(self, koeficienty):
        self.koeficienty = koeficienty
    def __str__(self):
        pol_out = ""
        for i in range(len(self.koeficienty)):
            if self.koeficienty[i] != 0:
                if self.koeficienty[i] > 0 and i != 0:
                    pol_out += "+"
                if i == 0:
                    pol_out += str(self.koeficienty[i])
                else:
                    if self.koeficienty[i] == -1:        
                        pol_out += "-"
                    elif self.koeficienty[i] == 1:
                        pol_out += ""
                    else:
                        pol_out += str(self.koeficienty[i])
            if i == 1 and self.koeficienty[i] != 0:
                pol_out += "x"
            elif i > 1:
                pol_out += "x^" + str(i)
        if pol_out == 0:
            pol_out += "0"
        return pol_out
    def VycisliHodnotu(self,bod):
        hodnota = 0
        for i in range(len(self.koeficienty)):
            hodnota += self.koeficienty[i] * pow(bod,i)
        return hodnota
    def VratStupen(self):
        stupen = 0
        for i in range(len(self.koeficienty)-1,-1,-1):
            if self.koeficienty[i] != 0:
                return i
        return 0
    def NasobSkalarem(self, skalar):
        koef = list()
        for i in range(len(self.koeficienty)):
            koef.append(self.koeficienty[i]*skalar)
        return Polynom(koef)
    @staticmethod
    def Secti(p1, p2):
        koef_p1 = copy.deepcopy(p1.koeficienty)
        koef_p2 = copy.deepcopy(p2.koeficienty)
        delka = len(koef_p1) = len(koef_p2)
        if len(koef_p2) > len(koef_p1):
            delka = len(koef_p1) = len(koef_p2)
            for i in range(delka):
                koef_p1.append(0)
        else:
            for i in range(delka):
                koef_p2.append(0)
        for i in range(len(koef_p1)):
            koef.append(koef_p1[i] + koef_p2[i])
        return Polynom(koef)
    @staticmethod
    def Odecti(p1, p2):
        return Polynom.Secti(p1,)
        
p1 = Polynom([1,0,1])
print(str(p1.VratStupen))
Polynom.Secti(p1, p1)
