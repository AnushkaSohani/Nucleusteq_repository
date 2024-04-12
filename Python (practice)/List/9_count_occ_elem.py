def countOcc(l1,x):
    count=0
    for i in l1:
        if i==x:
            count=count+1
        
    return count


l1=[]
n=int(input("Enter size of list "))
for i in range(n):
    x=int(input("Enter element in the list "))
    l1.append(x)

x=int(input("Enter an element to count its occurrences in the list "))

count=countOcc(l1,x)
print(count)