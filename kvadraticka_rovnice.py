#ax + b = 0
#x=(-b)/a

while(True):
    try:
        a = float(input("zadej a: "))
        b = float(input("zadej b: "))
        c = float(input("zadej c: "))
        break
    except:
        continue

def kvadraticka_rovnice(a, b, c):
    a=a
    b=b
    c=c
    d= b*b-4*a*c
    if d > 0:
        x_1=(-b+pow(d, 0.5))/(2*a)
        x_2=(-b-pow(d, 0.5))/(2*a)
        return (x_1, x_2)
    if d == 0:
        x_1=(-b)/(2*a)
        return x_1
    if d < 0:
        x_1="nemá řešení"
        return x_1
        

print(kvadraticka_rovnice(a, b, c))
