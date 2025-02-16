cifra1='0246'
cifra2='357'
c=0
l=0
for l1 in cifra1:
    for l2 in cifra2:
        for l3 in cifra1:
            for l4 in cifra2:
                for l5 in cifra1:
                    w=l1+l2+l3+l4+l5
                    if w.count('0')==1 and w.count('2')==1 and w.count('3')==1 and w.count('5')==1 and w.count('6')==1 and w.count('7')==1 and w.count('4')==1:
                        l+=1
print(l*2)