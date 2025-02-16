def F(n):
    a=''
    while n!=0:
        a=str(n%3)+a
        n//=3
    return a
for i in range(1000):
    b=F(i)+str(i%3)
    b=int(b,3)
    if b>=1000 and b<10000:
        print(b)
        break




