def length(list1):
    count=0
    for i in list1:
        count=count+1
    return count

list1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=input("Enter element in the list ")
    list1.append(x)

# print(list1)
c=length(list1)
print(c)