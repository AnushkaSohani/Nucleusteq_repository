str=input("Enter a string ")

x=str.find("not")
y=str.find("poor")

print("Not is found at index",x)
print("Poor is found at index",y)

if(y>x and x!=-1 and y!=-1):
    str=str.replace(str[x:y+4],'good')

print("Resulting string is------------>",str)
