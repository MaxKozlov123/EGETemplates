alf='ABCX'
c=0
for l1 in alf:
    for l2 in alf:
        for l3 in alf:
            for l4 in alf:
                for l5 in alf:
                    w=l1+l2+l3+l4+l5
                    if w.count('X')==1:
                        c+=1
print(c)
