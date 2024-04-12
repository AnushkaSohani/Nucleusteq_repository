def removeConsec(l1,k):
    res=[]
  
    for i in l1:
        ans=1
        if k in i:
            n=len(i)
            for item in range(n-1):
                # print(i[item])
                if i[item]==k and i[item+1]==k :
                    ans=0
                    break

            if(ans==1):
                res.append(i)
        
        else:
            res.append(i)

    print(res)

l1 =[(6, 5, 6, 3,6), (5, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
k=6
removeConsec(l1,k)