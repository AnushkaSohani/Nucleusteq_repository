def removeEven(l1,n):
    for i in l1:
        if(i%2==0):
            l1.remove(i)
    print(l1)
    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)


removeEven(l1,n)