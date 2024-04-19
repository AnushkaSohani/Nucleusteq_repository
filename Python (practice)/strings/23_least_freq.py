def leastFreq(l):
    d={}
    for i in l:
        freq=l.count(i)
        d.update({i:freq})
    
    # print(d)

    minimum=min(d.values())
    # print(minimum)

    for x,y in d.items():
        if y==minimum:
            return x


s=input("Enter a string ")
l=list(s)
# print(s)
x=leastFreq(l)
print(x)