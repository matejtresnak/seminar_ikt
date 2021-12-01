#urceni nejvetsiho spolecneho delitele

a = 40902
b = 24140
c = b

while b > 0:
    c = b
    b = a % b
    a = c

    print(a)
    
