def removeMul(l1,n,s,e):
    del l1[s:e]
    print(l1)

    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

s=int(input("Enter start index "))
e=int(input("Enter end index "))


removeMul(l1,n,s,e)