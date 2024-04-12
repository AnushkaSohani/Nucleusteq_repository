def sumList(l1):
    s=sum(l1)
    return s

def average(s,n):
    av=s/n
    return av

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

s=sumList(l1)
print("Sum = ",s)
av=average(s,n)
print("Average = ",av)