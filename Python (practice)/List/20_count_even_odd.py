def counte(l1):
    ce=0
    for i in l1:
        if(i%2==0):
            ce=ce+1

    return ce

def counto(l1):
    co=0
    for i in l1:
        if(i%2!=0):
            co=co+1

    return co
    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

ce=counte(l1)
co=counto(l1)
print("Even = ",ce,"Odd = ",co)