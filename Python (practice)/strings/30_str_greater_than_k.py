def greaterThan(s,l):
    res=""
    for i in s.split(" "):
        if(len(i)>l):
            res=res+" "+i
        
    return res

s=input("Enter a string ")
l=int(input("Enter length "))
res=greaterThan(s,l)
print(res)