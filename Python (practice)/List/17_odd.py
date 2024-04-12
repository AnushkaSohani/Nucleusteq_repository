def printOdd(l1):
    res=[]
    for i in l1:
        if(i%2!=0):
            res.append(i)

    return res

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

res=printOdd(l1)
print(res)