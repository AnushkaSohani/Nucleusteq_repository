def strNeighbour(l1,n):
    res=[]
    for i in range(n-1):
        for j in range(i+1,i+2):
            strong=max(l1[i],l1[j])
            # print(strong)
            res.append(strong)
    return res

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

res=strNeighbour(l1,n)
print(res)