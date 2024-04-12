def mult(l1):

    mul=1
    for i in l1:
        mul=mul*i
    
    return mul


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

m=mult(l1)
print(m)