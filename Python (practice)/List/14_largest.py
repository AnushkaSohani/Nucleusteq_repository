def largest(l1):
    m=max(l1)
    return m

l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=float(input("Enter element in the list "))
    l1.append(x)

m=largest(l1)
print(m)