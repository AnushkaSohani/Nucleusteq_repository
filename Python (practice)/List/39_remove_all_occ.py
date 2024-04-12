def removeOcc(l1,item):
    res=[]
    for i in l1:
        if i!=item:
            res.append(i)

    return res

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

item=int(input("Enter item to be removed from the list "))

l1=removeOcc(l1,item)
print(l1)