def close(s):
    pattern=["ape","apple","peach","puppy"]

    res=[]
    c=0
    for i in pattern:
        i=set(i)
        if i.issubset(s):
            res.append(pattern[c])
        
        c=c+1

    return res

s=input("Enter a string ")
s=set(s)
res=close(s)
print(res)