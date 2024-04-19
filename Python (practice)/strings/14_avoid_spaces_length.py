def length(str1):
    c=0
    for i in str1:
        if(i!=" "):
            c=c+1
    return c



str1=input("Enter a string ")
c=length(str1)
print("Count = ",c)