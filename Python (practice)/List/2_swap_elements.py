# swapping elements of given positions.

def swap(list1,n,a,b):

    t=list1[a-1]
    list1[a-1]=list1[b-1]
    list1[b-1]=t

    return list1

list1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    list1.append(x)

print(list1)

a=int(input("Enter position 1 "))
b=int(input("Enter position 2 "))


resList=swap(list1,n,a,b)
print(resList)
