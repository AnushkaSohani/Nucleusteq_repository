def uppperCase(str1):
    n=len(str1)
    st1=str1[n//2:]
    str1=str1[0:n//2]+st1.upper()
    return str1


str1=input("Enter a string ")
str1=uppperCase(str1)
print(str1)