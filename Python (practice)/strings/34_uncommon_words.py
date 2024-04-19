def uncommon(s1,s2):

    res=[]

    for i in s1:
        if i not in s2:
            res.append(i)
    
    for i in s2:
        if i not in s1:
            res.append(i)
        
    return res

s1=input("Enter string 1 ")
s2=input("Enter string 2 ")
s1=s1.split(" ")
s2=s2.split(" ")

res=uncommon(s1,s2)
print(res)