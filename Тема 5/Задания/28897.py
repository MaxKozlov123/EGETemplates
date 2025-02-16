for n in range(1000):
    b=bin(n)[2:]
    b=b+str(b.count('1')%2)
    b = b + str(b.count('1') % 2)
    R=int(b,2)
    if R>125:
        print(n)
        break
