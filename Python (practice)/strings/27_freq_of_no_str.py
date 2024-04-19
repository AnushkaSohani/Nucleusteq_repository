def noFreq(s):
    count=0
    for i in s:
        if(i.isnumeric()):
            count=count+1

    return count

s=input("Enter a string ")
c=noFreq(s)
print(c)