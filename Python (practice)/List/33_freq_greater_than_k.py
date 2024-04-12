def gtk(l1,k):
    res=[]
    d={}
    for i in l1:
        freq=l1.count(i)
        d.update({i:freq})

    print(d)

    for key,value in d.items():
        if(value>k):
            res.append(key)
        
    print(res)

l1 = [1,3,2,3,1,2,3,2,1,2,2]
k=3
gtk(l1,k)