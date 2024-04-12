def countpos(l1):
    ce=0
    for i in l1:
        if(i>=0):
            ce=ce+1

    return ce

def countneg(l1):
    co=0
    for i in l1:
        if(i<0):
            co=co+1

    return co
    

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

ce=countpos(l1)
co=countneg(l1)
print("Positive = ",ce,"Negative = ",co)