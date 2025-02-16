def S(n):
    a=0
    while n!=0:
        a=a+n%10
        n//=10
    return a
def F(a):
    b = bin(a)[2:]
    for _ in range(3):
        if S(int(b,2))%2==0:
            b+='0'
        else:
            b+='1'
    return int(b,2)
for i in range(1,1000):
    r=F(i)
    print(i,r,r//i)