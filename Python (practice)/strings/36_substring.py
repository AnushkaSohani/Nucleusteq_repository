def checkSub(s,sub):
    res=-1
    if sub in s:
        res=1
    
    return res

s=input("Enter a string ")
sub=input("Enter a substring ")
res=checkSub(s,sub)
if(res==1):
    print("Substring")
else:
    print("Not a substring")