def printEven(start,end):
    res=[]
    for i in range(start,end+1):
        if(i%2==0):
            res.append(i)

    return res

start=int(input("Enter start "))
end=int(input("Enter end "))

res=printEven(start,end)
print(res)