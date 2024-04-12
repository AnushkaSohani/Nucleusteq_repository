def rev(l1):
    l1.reverse()
    return l1


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)


resList=rev(l1)
print(resList)