def consecCommon(l1,n):
    res=[]
    for i in range(n-2):
        for j in range(i+1,i+2):
            if l1[i]==l1[j] and l1[j]==l1[j+1]:
                if l1[i] not in res:
                    res.append(l1[i])

    print(res)


l1=[1, 1,  64, 1, 64, 64, 22,11,11,11, 22]
n=len(l1)
val=consecCommon(l1,n)
# print(val)