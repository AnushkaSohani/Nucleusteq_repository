def maxFreq(s):
    dict={}
    for i in s:
        freq=s.count(i)
        dict.update({i:freq})
    
    # print(dict)

    maximum=max(dict.values())
    # print(maximum)

    for x,y in dict.items():
        if y==maximum:
            return x


s=input("Enter a string ")
s=list(s)

x=maxFreq(s)
print(x)