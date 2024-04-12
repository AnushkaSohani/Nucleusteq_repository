def checkExistence(list1,a):
    f=0
    if a in list1:
        f=1
    return f
    

list1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    list1.append(x)

a=int(input("Enter the number you want to search "))
f=checkExistence(list1,a)
if(f==1):
    print("Found")
else:
    print("Not found")