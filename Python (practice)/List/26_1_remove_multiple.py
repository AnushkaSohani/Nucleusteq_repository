def removeMul(l1,l2,m,n):
    for i in l2:
        if i in l1:
            l1.remove(i)

    print(l1)
    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

# print(l1)

l2=[]
m=int(input("Enter size of list "))
for i in range(m):
    y=int(input("Enter element in the list "))
    l2.append(y)

# print(l2)

removeMul(l1,l2,m,n)