import marshal


def largest(l1):
    m=max(l1)
    return m

def secLargest(l1,m):
    secmax=l1[0]
    for i in l1:
        if(i<m and i>secmax):
            secmax=i

    print(secmax)


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

m=largest(l1)
secLargest(l1,m)
