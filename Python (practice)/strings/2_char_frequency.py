str=input("Enter a string ")
n=len(str)
if(n>=2):
    res=str[0:2]  + str[n-2:]
    print(res)

else:
    print("Empty string")
