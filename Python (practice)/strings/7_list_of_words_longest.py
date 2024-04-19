l1=[]
n=int(input("Enter length of string "))
for i in range(n):
    x=input(f"Enter value {i} ")
    l1.append(x)

print(l1)
length=len(l1[0])
for i in range(n):
    if(length<=len(l1[i])):
        length=len(l1[i])
        maxLenWord=l1[i]
    
print("Max length is ",length)
print("Max length word is ",maxLenWord)