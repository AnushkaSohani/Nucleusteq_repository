def strSub(sub,str):

    res=[]
    for i in sub:
        if i in str:
            res.append("True")
        else:
            res.append("False")
      
    print(res)

sub=[]
m=int(input("Enter length of substring list "))
for i in range(m):
    y=input("Enter substring ")
    sub.append(y)

print(sub)

str=[]
n=int(input("Enter length of string list "))
for i in range(n):
    x=input("Enter string ")
    str.append(x)

print(str)
str=" ".join(str)
# print(sub,str)

strSub(sub,str)
