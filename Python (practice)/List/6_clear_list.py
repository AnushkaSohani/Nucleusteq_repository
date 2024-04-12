def clearList(list1):
    list1.clear()
    return list1

list1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    list1.append(x)

resList=clearList(list1)
print(resList)