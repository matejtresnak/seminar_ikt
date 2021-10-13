x = 2
y = 1

for i in range(2,10):
    for j in range(1,i):

        a = 2*i*j
        b = i*i-j*j
        c = i*i+j*j
        lst.sort()
        
        print(str(a)+","+str(b)+","+str(c))
