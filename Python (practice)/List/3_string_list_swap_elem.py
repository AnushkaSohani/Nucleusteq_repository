def swapElem(list1,n,a,b):
    for i in range(n):
        list1[i]=list1[i].replace(b,'-')
        list1[i]=list1[i].replace(a,'*')
        list1[i]=list1[i].replace('*',b)
        list1[i]=list1[i].replace('-',a)

    return list1

list1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=input("Enter element in the list ")
    list1.append(x)

print(list1)

a=input("Enter the character you want to replace ")
b=input("Enter the character you want to replace the old character with ")

resList=swapElem(list1,n,a,b)
print(resList)
