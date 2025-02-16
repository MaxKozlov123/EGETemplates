alf1='АО'
alf2='ПРБЛ'
c=0
for l1 in alf1:
    for l2 in alf2:
        for l3 in alf1:
            for l4 in alf2:
                for l5 in alf1:
                    for l6 in alf2:
                        for l7 in alf1:
                            for l8 in alf2:
                                w=l1+l2+l3+l4+l5+l6+l7+l8
                                if w.count('А')==3 and w.count('П')==1 and w.count('Р')==1 and w.count('Б')==1 and w.count('О')==1 and w.count('Л')==1:
                                    c+=1
print(c*2)

