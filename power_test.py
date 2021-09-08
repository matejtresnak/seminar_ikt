import math

def power_test(a, b):
    x = math.log(a, b)
    y = math.log(b, a)
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
