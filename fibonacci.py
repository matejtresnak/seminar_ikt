#uživatel zadá n, vypíšeme prvních 5 členů fib posloupnosti

a1 = 0
a2 = 1
n = int(input("zadej n: "))
lst = list()
lst.append(0)
lst.append(1)
for i in range(2, n, 1):
    lst.append(lst[i-1]+lst[i-2])
print(lst)
