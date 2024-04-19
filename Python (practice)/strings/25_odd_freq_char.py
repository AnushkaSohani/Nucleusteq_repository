def oddFreq(l):
    
    dict={}
    for i in l:
        freq=l.count(i)
        if(freq%2!=0):
            dict.update({i:freq})

    dict=list(dict)
    return dict
    
s=input("Enter a string ")
l=list(s)
# print(s)
newlist=oddFreq(l)
print(newlist)