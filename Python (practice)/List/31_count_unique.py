def unique(l1):
    res=[]
    for i in l1:
        if i not in res:
            res.append(i)

    c=len(res)
    return c


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

c=unique(l1)
print(c)
