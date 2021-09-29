"""
uživatel zadá: a,b - to je přímka
bod [x,y], leží na přímce?
ax + b = y
"""

a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
x = float(input("Zadej x: "))
y = float(input("Zadej y: "))

if a*x + b == y:
    print("ano")
else:
    print("ne")
