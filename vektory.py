import math

class Bod:
    def __init__(self, name, x, y, z=None):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
    @property
    def Name(self):
        return self.name
    @property
    def X(self):
        return self.x
    @property
    def Y(self):
        return self.y
    @property
    def Z(self):
        return self.z
    def __str__(self):
        if (self.Z == None):
            return str(self.Name) + "[" + str(self.X) + "," + str(self.Y) + "]"
        else:
            return str(self.Name) + "[" + str(self.X) + "," + str(self.Y) + "," + str(self.Z) + "]"

class Vektor:
    def __init__(self,name,x,y,z=None):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
    @classmethod
    def ZBodu(cls,name,A,B):
        x = B.X - A.X
        y = B.Y - A.Y
        if (A.Z != None and B.Z != None):
            z = B.Z - A.Z
        elif A.Z == None and B.Z != None or A.Z != None and B.Z == None:
            print("chyba ve vstupu")
            return None
        else:
            z = None
        instance = cls(name,x,y,z)
        return instance
    @property
    def Name(self):
        return self.name
    @property
    def X(self):
        return self.x
    @property
    def Y(self):
        return self.y
    @property
    def Z(self):
        return self.z
    @property
    def Velikost(self):
        if self.Z == None:
            return pow(pow(self.X,2) + pow(self.Y,2),0.5)
        else:
            return pow(pow(self.X,2) + pow(self.Y,2) + pow(self.Z,2),0.5)
    @staticmethod
    def SkalarniSoucin(v1,v2):
        if v1.Z == None and v2.Z == None:
            return (v1.X*v2.X + v1.Y*v2.Y)
        else:
            return (v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z)
    @staticmethod
    def OdchylkaVektoru(v1,v2):
        alpha_rad = math.acos(Vektor.SkalarniSoucin(v1,v2) / (v1.Velikost*v2.Velikost))
        return alpha_rad*180/math.pi
    @staticmethod
    def VektorovySoucin(v1,v2):
        if v1.Z == None or v2.Z == None:
            print("chyba ve vstupu")
        else:
            x = (v1.Y*v2.Z - v1.Z*v2.Y)
            y = (v1.Z*v2.X - v1.X*v2.Z)
            z = (v1.X*v2.Y - v1.Y*v2.X)
            return Vektor(str(v1.Name)+ "x" + str(v2.Name), x,y,z)
    @staticmethod
    def SmisenySoucin(u,v,w):
        return (Vektor.SkalarniSoucin(w,(Vektor.VektorovySoucin(u,v))))
    
        
        
    def __str__(self):
        if (self.Z == None):
            return str(self.Name) + "(" + str(self.X) + "," + str(self.Y) + ")"
        else:
            return str(self.Name) + "(" + str(self.X) + "," + str(self.Y) + "," + str(self.Z) + ")"
    
#u x v = (u2v3 - u3v2; u3v1 - u1v3; u1v2 - u2v1)  
    

#main
A = Bod("A", 2, 3,5)
print(str(A))

B = Bod("B", -4, 3,1)
print(str(B))

print()

u = Vektor("u",5,-2,1)
print(str(u))
print(u.Velikost)

print()

v = Vektor.ZBodu("v",A,B)
print(str(v))
print(v.Velikost)

w = Vektor("w",20,-14,8)

print()

skalarni_soucin = Vektor.SkalarniSoucin(u,v)
print(str(skalarni_soucin))

print()

print(Vektor.OdchylkaVektoru(u,v))

print()

print(Vektor.VektorovySoucin(u,v))

print()

print(Vektor.SmisenySoucin(u,v,w))
