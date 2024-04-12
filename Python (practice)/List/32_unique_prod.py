def unique(l1):
    res=[]
    for i in l1:
        if i not in res:
            res.append(i)

    prod=1
    for j in res:
        prod=prod*j

    return prod


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

prod=unique(l1)
print(prod)
