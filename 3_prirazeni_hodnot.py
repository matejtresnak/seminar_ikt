def method_1(x,y):
    tmp = x
    x = y
    y = tmp
    print("x=" + str(x))
    print("y=" + str(y))

def method_2(x, y):
    x = x+y
    y = x-y
    x = x-y
    print("x=" + str(x))
    print("y=" + str(y))

def method_3(x, y):
    x = x*y
    y = x/y
    x = x/y
    print("x=" + str(x))
    print("y=" + str(y))

def method_4(x,y):
    x,y = y,x
    print("x=" + str(x))
    print("y=" + str(y))

#u metody 2, 3 muzeme pretect limit int

method_4(5,10)
