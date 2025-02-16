alf='АМРТ'
c=0
for l1 in alf:
    for l2 in alf:
        for l3 in alf:
            for l4 in alf:
                c+=1
                w=l1+l2+l3+l4
                if c==250:
                    print(w)
                    break