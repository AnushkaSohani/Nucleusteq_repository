def printDup(l1,n):
    res=[]

    for i in range(n):
        for j in range(i+1,n):
            if l1[i]==l1[j]:
                if l1[i] not in res:
                    res.append(l1[i])               
    print(res)
                
l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

print(l1)

printDup(l1,n)