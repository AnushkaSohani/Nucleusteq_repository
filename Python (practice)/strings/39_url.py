def url(s):
    res=[]
    key="http"
    s=s.split(" ")
    for i in s:
        # print(i)
        if key in i:
            ind=i.index(key)
            u=i[ind:]
            # print(u)

            res.append(u)
    return res

s=input("ENter a string ")
res=url(s)
print(res)