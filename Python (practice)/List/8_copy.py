def copying(l1):
    l2=l1.copy()
    return l2


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

l2=copying(l1)
print("l2 after copying: ",l2)