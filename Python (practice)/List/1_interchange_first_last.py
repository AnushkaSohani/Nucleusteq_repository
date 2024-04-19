# interchange first and last element of a list.

def interchange(l,n):

    t=l[0]
    l[0]=l[n-1]
    l[n-1]=t

    return l

l=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l.append(x)

print(l)

resList=interchange(l,n)
print(resList)