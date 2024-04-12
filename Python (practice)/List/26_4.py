def removeMul(l1,l2,m,n):
    l2.sort(reverse=True)
    for j in l2:
        l1.remove(l1[j])
    print(l1)
    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

# print(l1)

l2=[]
m=int(input("Enter size  "))
for i in range(m):
    y=int(input("Enter index whose element is to be removed from list "))
    l2.append(y)

# print(l2)

removeMul(l1,l2,m,n)