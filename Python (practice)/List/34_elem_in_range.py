def inRange(l1,i,j):
    r=1
    for elem in l1:
        if (elem<i or elem>j):
            r=0
            break
    return r

l1=[4, 5, 6, 7, 2, 10]
i=3
j=10
r=inRange(l1,i,j)
if(r==1):
    print("In range",i,"to",j)
else:
    print("Not in range ",i,"to",j)