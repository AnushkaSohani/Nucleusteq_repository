def listofDict(l1,key,lenL1,lenKey):
    res=[]
    l=0
    k=0
    while(l!=lenL1):
        while(k!=lenKey):
            res.append({key[k]:l1[l]})           
            k=k+1            
            break
        l=l+1
        if(k==lenKey and l1!=lenL1):
            k=0

    print(res)

        
l1 = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key =  ['name','number'] 
lenL1=len(l1)
lenKey=len(key)
listofDict(l1,key,lenL1,lenKey)