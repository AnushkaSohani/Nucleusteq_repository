def summation(l1):
    res=[]
    
    for i in l1:
        sum=0
        while(i!=0):
            a=i%10
            sum=sum+a
            i=i//10
        res.append(sum)

    print(res)


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

summation(l1)