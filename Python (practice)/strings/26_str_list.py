def spcificFreq(l,c):
    emp=[]
    dict={}

    for i in l:
        for j in i:
            emp.append(j)

    # print(emp) 

    for k in emp:
        if k in c:
            freq=emp.count(k)
            dict.update({k:freq})

    return dict

l=[]
c=[]
n=int(input("Enter length of list "))
for i in range(n):
    x=input("Enter a string ")
    l.append(x)

# print(l)

n=int(input("Enter no of char whose freq you need to find "))
for i in range(n):
    y=input("Enter character ")
    c.append(y)

# print(c)

dict=spcificFreq(l,c)
print(dict)