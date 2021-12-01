import math

def power_test(a, b):
    x = math.log(a, b)
    if (x - int(x) < 0.0000005):
        x = int(x)
    y = math.log(b, a)
    if (y - int(y) < 0.0000005):
        y = int(y)
    if x == int(x):
        print(x)
        return True
    else:
        if y == int(y):
            print(y)
            return True
        else:
            return False

print(power_test(512, 2))
